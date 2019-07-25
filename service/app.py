from catsHTM import cone_search
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

path = '/home/ubuntu/catalogsHTM/'
#cat_dirs =['2MASS', '2MASSxsc', 'DECaLS/DR5', 'GAIA/DR1', 'GAIA/DR2', 'GALEX/DR6Plus7', 'HST/HSCv2', 'IPHAS/DR2', 'NED/20180502', 'SDSS/DR10', 'SDSS/DR14offset', 'SpecSDSS/DR14', 'Spitzer/SAGE', 'Spitzer/IRACgc', 'UKIDSS/DR10', 'VISTA/Viking/DR2', 'VST/ATLAS/DR3', 'VST/KiDS/DR3']

cat_dirs = ['XMM', 'ROSATfsc']

@app.route('/conesearch')
def conesearch():
    catalog = request.args.get('catalog')
    ra = float(request.args.get('ra'))
    dec = float(request.args.get('dec'))
    radius = float(request.args.get('radius'))

    match, catalog_columns, columns_units = cone_search(catalog, ra, dec, radius, path)
    df = pd.DataFrame(match, columns=catalog_columns)
    results = []
    for index, row in df.iterrows():
        obj = dict(zip(catalog_columns, row.values))
        results.append(obj)
    return jsonify(results)

@app.route('/crossmatch')
def crossmatch():
    ra = float(request.args.get('ra'))
    dec = float(request.args.get('dec'))
    radius = float(request.args.get('radius'))

    result = []
    for catalog in cat_dirs:
        match, catalog_columns, columns_units = cone_search(catalog, ra, dec, radius, path)
        df = pd.DataFrame(match, columns=catalog_columns)
        partial_result = []
        for index, row in df.iterrows():
            obj = dict(zip(catalog_columns, row.values))
            partial_result.append(obj)
        # add catalog tag 
        result_catname = {catalog: partial_result} 
        result.append(result_catname)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
