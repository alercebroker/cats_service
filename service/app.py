from astropy.coordinates import SkyCoord
from astropy import units
from catsHTM import cone_search
from flask import Flask, request, jsonify, flash, redirect, url_for
from flask_cors import CORS
from math import radians, degrees
from werkzeug.utils import secure_filename
import numpy as np
import os
import pandas as pd

app = Flask(__name__)
CORS(app)

# path where the HDF5 files are
path = os.environ['DATA_PATH']
# list of catalogs available in catsHTM
catalogs = [
    'FIRST',
    'TMASS',
    'TMASSxsc',
    'DECaLS',
    'GAIADR1',
    'GAIADR2',
    'GALEX',
    'HSCv2',
    'IPHAS',
    'NEDz',
    'SDSSDR10',
    'SDSSoffset',
    'SpecSDSS',
    'SAGE',
    'IRACgc',
    'UKIDSS',
    'VISTAviking',
    'VSTatlas',
    'VSTkids',
    'AKARI',
    'APASS',
    'NVSS',
    'Cosmos',
    'PTFpc',
    'ROSATfsc',
    'SkyMapper',
    'UCAC4',
    'WISE',
    'XMM',
    'AAVSO_VSX',
    'unWISE',
    'SWIREz',
    'Simbad_PM200',
    'CRTS_per_var']
# statistically defined radiuses, not advertised ones
radius_dict = {
    'ROSATfsc': 50,
    'XMM': 8,
    'APASS': 2,
    'DECaLS': 0.1,
    'GAIADR1': 0.1,
    'GAIADR2': 0.1,
    'NVSS': 10.8,
    'SDSSoffset': 0.1,
    'SkyMapper': 0.4}
# catsHTM catalog name to real name
catalog_map = {
    "TMASS": "2MASS",
    "CRTS_per_var": "CRTS",
    "GAIADR1": "GAIA/DR1",
    "GAIADR2": "GAIA/DR2",
    "SDSSDR10": "SDSS/DR10",
    "TMASSxsc": "2MASSxsc"
}


@app.route('/')
def welcome():
    '''
    This function returns information about the API.

    Args:
        None

    Returns:
        A string that includes a link to the API documentation.
    '''
    return '''Welcome to the Cats service.
    The documentation can be found here: link.'''


@app.route('/conesearch')
def conesearch():
    '''
    This function returns the cone search result, it uses an auxiliary
    function to generate the result.

    Args:
        None

    Returns:
        A jsonified string with the cone search result.
    '''
    try:
        # get arguments
        catalog = request.args.get('catalog')
        # convert ra and dec to radians
        ra = radians(float(request.args.get('ra')))
        dec = radians(float(request.args.get('dec')))
        radius = float(request.args.get('radius'))
    except BaseException:
        return jsonify('Request contains one or more invalid arguments.')
    return jsonify(conesearch(catalog, ra, dec, radius))


def conesearch(catalog, ra, dec, radius):
    '''
    This function returns the cone search result.

    Args:
        catalog (string): catalog name according to the available catalog
        in the docs.
        ra (float): ra coordinate of the point to search in degrees.
        dec (float): dec coordinate of the point to search in degrees.
        radius (float): radius to search in arcsec.
    Returns:
        A jsonified string with the cone search result.
    '''
    # call catsHTM cone search
    match, catalog_columns, column_units = cone_search(
        catalog, ra, dec, radius, path)
    if match.size == 0:
        return {}
    try:
        df = pd.DataFrame(match, columns=catalog_columns)
    except ValueError as ex:
        return {}
    results = {}
    result_with_catname = {}
    # generate dictionaries with response values and replace when neccessary
    for column, unit in zip(catalog_columns, column_units):
        values = []
        for value in df[column].values.tolist():
            if np.isnan(value):
                value = None
            elif value == np.inf:
                value = "infinity"
            elif unit_is_rad(unit):
                value = degrees(value)
            values.append(value)
        if unit_is_rad(unit):
            results[column] = {"units": "deg", "values": values}
        else:
            results[column] = {"units": unit, "values": values}
    # append and get catalog real name
    result_with_catname[catalog_map.get(catalog, catalog)] = results
    return result_with_catname


@app.route('/conesearch_all')
def conesearch_all():
    '''
    This function returns the result of running a cone search over all
    available catalogs. It uses an auxiliary function to generate this
    results.

    Args:
        None

    Returns:
        A jsonified string with the cone search results for all catalogs.
    '''
    global catalogs
    # ra and dec to radians
    try:
        ra = radians(float(request.args.get('ra')))
        dec = radians(float(request.args.get('dec')))
        radius = float(request.args.get('radius'))
    except BaseException:
        return jsonify('Request contains one or more invalid arguments.')
    result = []
    # append the results of each catalog
    for catalog in catalogs:
        partial_result = conesearch(catalog, ra, dec, radius)
        if partial_result != {}:
            result.append(partial_result)
    final_result = {}
    final_result['catalogs'] = result
    return jsonify(final_result)


@app.route('/crossmatch')
def crossmatch():
    '''
    This function returns the result of running a crossmatch in one catalog.
    It uses an auxiliary function to compute the results.

    Args:
        None

    Returns:
        A jsonified string with the crossmatch result.
    '''
    global radius_dict
    try:
        catalog = request.args.get('catalog')
        ra = radians(float(request.args.get('ra')))
        dec = radians(float(request.args.get('dec')))
    except BaseException:
        return jsonify('Request contains one or more invalid arguments.')
    try:
        radius = float(request.args.get('radius'))
    except BaseException:
        radius = float(radius_dict.get(catalog, 50))

    return jsonify(crossmatch(catalog, ra, dec, radius))

@app.route('/test_cone')
def test_cone():
    # call catsHTM cone search
    match, catalog_columns, columns_units = cone_search(
        catalog, ra, dec, radius, path)
    try:
        df = pd.DataFrame(match, columns=catalog_columns)
        # add distance column to df
        df['distance'] = None
    except BaseException:
        return []
    matches = []
    columns_units = np.append(columns_units, 'arcsec')

    for index, row in df.iterrows():
        obj = dict(zip(catalog_columns, row.values))
        matches.append(obj)
    # this object is a list with one dictionary containing the ra, dec of the
    # closest matching object
    try:
        closest_ra_dec = get_min_distance(matches, catalog, ra, dec)
    except BaseException:
        return {}
    # get all the fields of the matching object
    ra_cat, dec_cat = map_ra_dec(catalog)
    result = {}
    for index, row in df.iterrows():

        if isinstance(row[ra_cat], float):
            ra_equal = row[ra_cat] == closest_ra_dec[0]["ra"]
        else:
            ra_equal = (row[ra_cat].iloc[0] == closest_ra_dec[0]["ra"])

        if isinstance(row[dec_cat], float):
            dec_equal = row[dec_cat] == closest_ra_dec[0]["dec"]
        else:
            dec_equal = (row[dec_cat].iloc[0] == closest_ra_dec[0]["dec"])
        if ra_equal and dec_equal:
            # add distance to result
            row['distance'] = closest_ra_dec[0]['distance']
            result = row.to_dict()
            break

    result_with_units = {}
    for key, unit in zip(result, columns_units):
        value = result[key]
        if unit_is_rad(unit):
            # convert unit to deg
            result_with_units[key] = {'value': None if np.isnan(
                value) else degrees(value), 'unit': 'deg'}
        else:
            result_with_units[key] = {
                'value': None if np.isnan(value) else value, 'unit': unit}
    # replace inf
    result_with_units = {
        key: (
            val if val['value'] != np.inf else {
                'value': 'infinity',
                'unit': val['unit']}) for key,
        val in result_with_units.items()}
    return result_with_units

def crossmatch(catalog, ra, dec, radius):
    '''
    This function returns the crossmatch result.

    Args:
        catalog (string): catalog name according to the available catalog
        in the docs.
        ra (float): ra coordinate of the point to search in degrees.
        dec (float): dec coordinate of the point to search in degrees.
        radius (float): radius to search in arcsec.
    Returns:
        A jsonified string with the crossmatch result.
    '''
    # call catsHTM cone search
    match, catalog_columns, columns_units = cone_search(
        catalog, ra, dec, radius, path)
    try:
        df = pd.DataFrame(match, columns=catalog_columns)
        # add distance column to df
        df['distance'] = None
    except BaseException:
        return []
    matches = []
    columns_units = np.append(columns_units, 'arcsec')

    for index, row in df.iterrows():
        obj = dict(zip(catalog_columns, row.values))
        matches.append(obj)
    # this object is a list with one dictionary containing the ra, dec of the
    # closest matching object
    try:
        closest_ra_dec = get_min_distance(matches, catalog, ra, dec)
    except BaseException:
        return {}
    # get all the fields of the matching object
    ra_cat, dec_cat = map_ra_dec(catalog)
    result = {}
    for index, row in df.iterrows():

        if isinstance(row[ra_cat], float):
            ra_equal = row[ra_cat] == closest_ra_dec[0]["ra"]
        else:
            ra_equal = (row[ra_cat].iloc[0] == closest_ra_dec[0]["ra"])

        if isinstance(row[dec_cat], float):
            dec_equal = row[dec_cat] == closest_ra_dec[0]["dec"]
        else:
            dec_equal = (row[dec_cat].iloc[0] == closest_ra_dec[0]["dec"])
        if ra_equal and dec_equal:
            # add distance to result
            row['distance'] = closest_ra_dec[0]['distance']
            result = row.to_dict()
            break

    result_with_units = {}
    for key, unit in zip(result, columns_units):
        value = result[key]
        if unit_is_rad(unit):
            # convert unit to deg
            result_with_units[key] = {'value': None if np.isnan(
                value) else degrees(value), 'unit': 'deg'}
        else:
            result_with_units[key] = {
                'value': None if np.isnan(value) else value, 'unit': unit}
    # replace inf
    result_with_units = {
        key: (
            val if val['value'] != np.inf else {
                'value': 'infinity',
                'unit': val['unit']}) for key,
        val in result_with_units.items()}
    return result_with_units


@app.route('/crossmatch_all')
def crossmatch_all():
    global catalogs
    global radius_dict
    try:
        ra = radians(float(request.args.get('ra')))
        dec = radians(float(request.args.get('dec')))
    except BaseException:
        return jsonify('Request contains one or more invalid arguments.')
    # check if a value for radius was provided
    radius = None
    try:
        radius = float(request.args.get('radius'))
    # if not, use default
    except BaseException:
        pass
    result = []
    for catalog in catalogs:
        if radius:
            partial_result = crossmatch(catalog, ra, dec, radius)
        else:
            partial_result = crossmatch(
                catalog, ra, dec, float(
                    radius_dict.get(
                        catalog, 50)))
        if partial_result:
            if catalog in catalog_map:
                catalog = catalog_map[catalog]
            result_catname = {catalog: partial_result}
            result.append(result_catname)
    return jsonify(result)


def map_ra_dec(catalog):
    if catalog == 'HSCv2':
        return 'MatchRA', 'MatchDec'
    elif catalog == 'XMM':
        return 'RA', 'DEC'
    elif catalog == 'SDSSoffset':
        return 'ra', 'dec'
    else:
        return 'RA', 'Dec'


def unit_is_rad(unit):
    return unit == 'rad'

# receives a list of dictionaries and the original catalog, ra and dec


def get_min_distance(matches, catalog, ra, dec):
    ra_cat, dec_cat = map_ra_dec(catalog)
    distances = []
    if catalog == 'XMM':
        unit = units.degree
    else:
        unit = units.radian
    for match in matches:
        point_cat = SkyCoord(
            ra=float(match[ra_cat]) * unit,
            dec=float(match[dec_cat]) * unit
        )
        point_requested = SkyCoord(
            ra=float(ra) * unit,
            dec=float(dec) * unit
        )
        distances.append(
            dict(
                distance=point_requested.separation(point_cat).arcsecond,
                ra=match[ra_cat],
                dec=match[dec_cat]))
    # get minimum distance
    if distances:
        min_distance = min([float(x['distance']) for x in distances])
        # list with a dictionary with the min distance, ra and dec
        return list(filter(lambda x: x['distance'] == min_distance, distances))
    return None


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')
