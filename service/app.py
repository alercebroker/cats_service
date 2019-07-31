from catsHTM import cone_search
from flask import Flask, request, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd
from astropy.coordinates import SkyCoord
from astropy import units

app = Flask(__name__)

path = '/home/ubuntu/catalogsHTM/'
catalogs = ['FIRST', 'TMASS', 'TMASSxsc', 'DECaLS', 'GAIADR1', 'GAIADR2', 'GALEX', 'HSCv2', 'IPHAS', 'NEDz', 'SDSSDR10', 'SDSSoffset', 'SpecSDSS', 'SAGE', 'IRACgc', 'UKIDSS', 'VISTAviking', 'VSTatlas', 'VSTkids', 'AKARI', 'APASS', 'NVSS', 'Cosmos', 'PTFpc', 'ROSATfsc', 'SkyMapper', 'UCAC4', 'WISE', 'XMM', 'AAVSO_VSX', 'unWISE', 'SWIREz', 'Simbad_PM200', 'CRTS_per_var']

@app.route('/')
def welcome():
    return 'Welcome to the crossmatch service'

@app.route('/conesearch')
def conesearch():
    #get arguments
    catalog = request.args.get('catalog')
    ra = float(request.args.get('ra'))
    dec = float(request.args.get('dec'))
    radius = float(request.args.get('radius'))

    return jsonify(conesearch(catalog, ra, dec, radius))

def conesearch(catalog, ra, dec, radius):
    match, catalog_columns, columns_units = cone_search(catalog, ra, dec, radius, path)
    try:
        df = pd.DataFrame(match, columns=catalog_columns)
    except ValueError as ex:
        return []
    results = []
    for index, row in df.iterrows():
        obj = dict(zip(catalog_columns, row.values))
        results.append(obj)
    return results

@app.route('/allmatches')
def allmatches():
    global catalogs
    ra = float(request.args.get('ra'))
    dec = float(request.args.get('dec'))
    radius = float(request.args.get('radius'))

    result = []
    for catalog in catalogs:
        partial_result = conesearch(catalog, ra, dec, radius)
        if partial_result == []:    
            continue
        else:
            result_catname = {catalog: partial_result}  
            result.append(result_catname)
    return jsonify(result)


@app.route('/crossmatch')
def crossmatch():
    catalog = request.args.get('catalog')
    ra = float(request.args.get('ra'))
    dec = float(request.args.get('dec'))
    radius = float(request.args.get('radius'))

    return jsonify(crossmatch(catalog, ra, dec, radius))

def crossmatch(catalog, ra, dec, radius):
    match, catalog_columns, columns_units = cone_search(catalog, ra, dec, radius, path)
    try:
        df = pd.DataFrame(match, columns=catalog_columns)
    except:
        return []
    matches = []
    for index, row in df.iterrows():
        obj = dict(zip(catalog_columns, row.values))
        matches.append(obj)
    # this object is a list with one dictionary containing the ra, dec of the closest matching object
    try:
        closest_ra_dec = get_min_distance(matches, catalog, ra, dec)
    except:
        return []
    # get all the fields of the matching object
    ra_cat, dec_cat = map_ra_dec(catalog)
    result = {}
    for index, row in df.iterrows():
        if row[ra_cat] == closest_ra_dec[0]['ra'] and row[dec_cat] == closest_ra_dec[0]['dec']:
            result = row.to_dict()
            break
    result_with_units = {}
    for key, unit in zip(result, columns_units):
        result_with_units[key] = {'value': result[key], 'unit': unit}
    return result_with_units

@app.route('/crossmatch_all')
def crossmatch_all():
    global catalogs
    ra = float(request.args.get('ra'))
    dec = float(request.args.get('dec'))
    radius = float(request.args.get('radius'))
    
    result = []
    for catalog in catalogs:
        partial_result = crossmatch(catalog, ra, dec, radius)
        if partial_result:
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

#receives a list of dictionaries and the original catalog, ra and dec
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
        distances.append(dict(distance=point_requested.separation(point_cat).arcsecond, ra=match[ra_cat], dec=match[dec_cat])) #distance, object ra, object dec
    #get minimum distance
    if distances:
        min_distance = min([float(x['distance']) for x in distances])
        # list with a dictionary with the min distance, ra and dec
        return list(filter(lambda x: x['distance'] == min_distance, distances))
    return None

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
