from fastapi.encoders import jsonable_encoder


def json(final_result):
    return jsonable_encoder(final_result)

def catname(results, catalog_map, catalog):
    result_with_catname = {}
    result_with_catname["cat_name"] = catalog_map.get(catalog, catalog)
    result_with_catname["cat_fields"] = results
    return result_with_catname

def catname_all(final_result,catalog_map):

    result_catname = []
    final_result_catname = {}
    for key in final_result:
        result_catname.append(catname(final_result[key], catalog_map, key))
    
    final_result_catname["catalogs"] = result_catname

    return final_result_catname



    