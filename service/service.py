from catsHTM import cone_search
from service.parse import parse_conesearch, parse_crossmatch

def service_get_conesearch(catalog, ra, dec, radius, path):

    match, catalog_columns, column_units = cone_search(catalog, ra, dec, radius, path)
    print(match, catalog_columns, column_units)
    results = parse_conesearch(match, catalog_columns, column_units)
    return results


def service_get_conesearch_all(catalogs, ra, dec ,radius, path):

    result = []
    # append the results of each catalog
    final_result = {}
    for catalog in catalogs:
        partial_result = service_get_conesearch(catalog, ra, dec, radius, path)
        if partial_result != {}:
            result.append(partial_result)
        final_result[catalog] = result
        result = []

    return final_result


def service_get_crossmatch(catalog, ra, dec, radius, path,map_ra_dec):

    match, catalog_columns, column_units = cone_search(catalog, ra, dec, radius, path)
    if match.size != 0:
        return parse_crossmatch(match, catalog, ra, dec, catalog_columns, column_units,map_ra_dec)

    else:
        return {}

def service_get_crossmatch_all(catalogs, ra, dec ,radius, path, map_ra_dec,radius_dict):

    result = []

    final_result = {}

    for catalog in catalogs:
        if radius == None:
            radius_aux = float(radius_dict.get(catalog,50))
        else: 
            radius_aux = radius
        partial_result = service_get_crossmatch(catalog, ra, dec, radius_aux, path, map_ra_dec)
        # append the partial result if it is not empty
        if partial_result != {}:
            result.append(partial_result)
        final_result[catalog] = result
        result = []
    return final_result

