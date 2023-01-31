from catsHTM import cone_search
from ..models.parse import parse_conesearch, parse_crossmatch


def service_get_conesearch(catalog, request, path):
    
    match, catalog_columns, column_units = cone_search(catalog, request["ra"], request["dec"], request["radius"], path)
    results = parse_conesearch(match, catalog_columns, column_units)  
    return results


def service_get_conesearch_all(catalogs,request, path):

    # append the results of each catalog
    final_result = {}
    for catalog in catalogs:
        partial_result = service_get_conesearch(catalog,request, path)

        if partial_result != {}:
            final_result[catalog] = partial_result

    return final_result


def service_get_crossmatch(catalog,request, path,map_ra_dec,radius_dict):

    if request["radius"] == None: 
        request["radius"] = float(radius_dict.get(catalog,50))

    print(f"catalogo_recibido:{catalog}")
    match, catalog_columns, column_units = cone_search(catalog, request["ra"], request["dec"], request["radius"], path)
    print(f"y el match de eso es:{match}")
    if len(match) != 0:
        return parse_crossmatch(match, catalog, request["ra"], request["dec"], catalog_columns, column_units,map_ra_dec)

    else:
        return {}

def service_get_crossmatch_all(catalogs,request, path, map_ra_dec,radius_dict):

    final_result = {}
    for catalog in catalogs:
        if request["radius"] == None:
            request_aux ={
                "ra" : request["ra"],
                "dec" : request["dec"],
                "radius": float(radius_dict.get(catalog,50))
            }
        else: 
            request_aux = request
        partial_result = service_get_crossmatch(catalog, request_aux, path, map_ra_dec,radius_dict)
        # append the partial result if it is not empty
        if partial_result != {}:
            final_result[catalog] = partial_result
    return final_result


