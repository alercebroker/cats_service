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
    'TMASS': '2MASS',
    'CRTS_per_var': 'CRTS',
    'GAIADR1': 'GAIA/DR1',
    'GAIADR2': 'GAIA/DR2',
    'SDSSDR10': 'SDSS/DR10',
    'TMASSxsc': '2MASSxsc'}
# map ra, dec to catalog ra, dec name
map_ra_dec = {
    'HSCv2': ('MatchRA', 'MatchDec'),
    'XMM': ('RA', 'DEC'),
    'SDSSoffset': ('ra', 'dec')}


@app.route('/')
def welcome():
    '''
    This function returns information about the API.

    Args:
        None

    Returns:
        HTML text with a link to the API documentation.
    '''
    return '''<!DOCTYPE html>
              <html>
              <head>
              <title>ALeRCE Cats Service</title>
              </head>
              <body>
              <h3>Welcome to the Cats Service</h3>
              <p>Documentation can be found
              <a href="https://alerceapi.readthedocs.io/en/latest/catshtm.html">
              here</a>.</p>
              </body>
              </html>'''


@app.route('/conesearch')
def conesearch():
    '''
    This function returns the cone search result, it uses an auxiliary
    function to generate the result.

    Args:
        None

    Returns:
        The JSON representation of the cone search result for a single catalog.
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
    Returns the cone search result. It uses an auxiliary
    function.

    Args:
        catalog (string): catalog name according to the available catalog
        in the docs.
        ra (float): ra coordinate of the point to search in degrees.
        dec (float): dec coordinate of the point to search in degrees.
        radius (float): radius to search in arcsec.
    Returns:
        A dictionary containing the cone search result for a single catalog.
    '''
    # call catsHTM cone search
    match, catalog_columns, column_units = cone_search(
        catalog, ra, dec, radius, path)
    # no results, empty dictionary
    if match.size == 0:
        return {}
    # generate dictionaries with response values
    results = format_cone_results(match, catalog_columns, column_units)
    # add catalog real name and append to final result
    result_with_catname = {}
    result_with_catname[catalog_map.get(catalog, catalog)] = results
    return result_with_catname


def format_cone_results(match, catalog_columns, column_units):
    '''
    This function formats the cone search result. It replaces nan and infinity
    values, and add column names and units.

    Args:
        match (numpy ndarray): array contaning the values for the cone search
        result, this array is the output of catsHTM 'cone_search' function.
        catalog_columns (numpy ndarray): the columns of the catalog according
        to catsHTM.
        column_units (numpy ndarray): the units associated to each column.
    Returns:
        A dictionary containing the formatted cone search results for a
        catalog.
    '''
    try:
        # create a dataframe to match the columns to the values
        df = pd.DataFrame(match, columns=catalog_columns)
    except ValueError as ex:
        return {}
    results = {}
    # generate dictionaries with response values and replace when neccessary
    for column, unit in zip(catalog_columns, column_units):
        values = []
        for value in df[column].values.tolist():
            # replace nan and infinity
            if np.isnan(value):
                value = None
            elif value == np.inf:
                value = "infinity"
            # convert radians to degrees
            elif unit_is_rad(unit):
                value = degrees(value)
            values.append(value)
        if unit_is_rad(unit):
            results[column] = {"units": "deg", "values": values}
        else:
            results[column] = {"units": unit, "values": values}
    return results


@app.route('/conesearch_all')
def conesearch_all():
    '''
    This function returns the result of running a cone search over all
    available catalogs. It uses the 'conesearch' function to generate this
    results.

    Args:
        None

    Returns:
        The JSON representation of the cone search results for all catalogs.
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
    This function returns the result of running a crossmatch over one catalog.
    It uses an auxiliary function to compute the results.

    Args:
        None
    Returns:
        The JSON representation of the crossmatch result.
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


def crossmatch(catalog, ra, dec, radius):
    '''
    This function returns the crossmatch result for a catalog.

    Args:
        catalog (string): catalog name according to the available catalog
        in the docs.
        ra (float): ra coordinate of the point to search in degrees.
        dec (float): dec coordinate of the point to search in degrees.
        radius (float): radius to search in arcsec.
    Returns:
        A dictionary with the crossmatch result.
    '''
    # call catsHTM cone search
    match, catalog_columns, columns_units = cone_search(
        catalog, ra, dec, radius, path)
    return format_crossmatch_results(match, catalog_columns, column_units)


def format_crossmatch_results(match, catalog_columns, column_units):
    '''
    This function formats the crossmatch result of a catalog.

    Args:
        match (numpy ndarray): array contaning the values for the cone search
        result, this array is the output of catsHTM 'cone_search' function.
        catalog_columns (numpy ndarray): the columns of the catalog according
        to catsHTM.
        column_units (numpy ndarray): the units associated to each column.
    Returns:
        A dictionary with the crossmatch result.
    '''
    try:
        # dataframe to match columns to values
        df = pd.DataFrame(match, columns=catalog_columns)
        # add distance column to df
        df['distance'] = None
    except BaseException:
        return []
    matches = []
    # append distance unit
    columns_units = np.append(columns_units, 'arcsec')
    for index, row in df.iterrows():
        obj = dict(zip(catalog_columns, row.values))
        matches.append(obj)
    # this object is a list with a dictionary containing
    # the ra, dec of the closest matching object
    try:
        closest_ra_dec = get_min_distance(matches, catalog, ra, dec)
    except BaseException:
        return {}
    # get all the fields of the matching object
    ra_cat, dec_cat = map_ra_dec.get(catalog, ('RA', 'Dec'))
    result = {}
    for index, row in df.iterrows():
        # check type of ra
        if isinstance(row[ra_cat], float):
            ra_equal = row[ra_cat] == closest_ra_dec[0]["ra"]
        else:
            ra_equal = (row[ra_cat].iloc[0] == closest_ra_dec[0]["ra"])
        # check type of dec
        if isinstance(row[dec_cat], float):
            dec_equal = row[dec_cat] == closest_ra_dec[0]["dec"]
        else:
            dec_equal = (row[dec_cat].iloc[0] == closest_ra_dec[0]["dec"])
        if ra_equal and dec_equal:
            # add distance to result
            row['distance'] = closest_ra_dec[0]['distance']
            result = row.to_dict()
            break
    # add units to the results
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
    '''
    This function returns the crossmatch result for all catalogs.

    Args:
        None
    Returns:
        The JSON representation of the crossmatch result for all catalogs.
    '''
    global catalogs
    global radius_dict
    # get request parameters
    try:
        ra = radians(float(request.args.get('ra')))
        dec = radians(float(request.args.get('dec')))
    except BaseException:
        return jsonify('Request contains one or more invalid arguments.')
    # check if a value for radius was provided
    radius = None
    try:
        radius = float(request.args.get('radius'))
    except BaseException:
        # if no radius was provided, use the default value
        radius = float(radius_dict.get(catalog, 50))
    result = []
    for catalog in catalogs:
        partial_result = crossmatch(catalog, ra, dec, radius)
        # append the partial result if it is not empty
        if partial_result:
            if catalog in catalog_map:
                # get the official name of the catalog
                catalog = catalog_map.get(catalog, catalog)
            result_catname = {catalog: partial_result}
            result.append(result_catname)
    return jsonify(result)


def unit_is_rad(unit):
    '''
    Checks if unit is rad, and returns True or False accordingly.

    Args:
        unit (string): the unit.
    Returns:
        A boolean stating if the input units was radian or not.
    '''
    return unit == 'rad'


def get_min_distance(matches, catalog, ra, dec):
    '''
    Get the element with the minimum distance between the cone search matches.

    Args:
        matches (list): list of cone search matches for a catalog.
        catalog (string): name of the catalog.
        ra (float): ra coordinate of the point to search in degrees.
        dec (float): dec coordinate of the point to search in degrees.
    Returns:
        A list containing the closest element (distance, ra, dec).
    '''
    ra_cat, dec_cat = map_ra_dec.get(catalog, ('RA', 'Dec'))
    # XMM special case
    if catalog == 'XMM':
        unit = units.degree
    else:
        unit = units.radian
    distances = []
    # get distance between points in arcseconds
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
