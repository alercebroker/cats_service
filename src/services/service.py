from catsHTM import cone_search
from ..models.parse import parse_conesearch, parse_crossmatch


def service_get_conesearch(request, path):
    """
    This function returns all the conesearch matches, given a request, for a
    specific catalog. It uses the catsHTM conesearch function for this.

    Args:
        catalog (string): name of the catalog.
        request (dict): contains the ra, dec, and radius.
        path (string): path of the catalog.

    Returns:
        A list containing all the matches.
    """
    match, catalog_columns, column_units = cone_search(
        request.catalog, request.ra, request.dec, request.radius, path
    )

    if len(match) != 0:
        return parse_conesearch(match, catalog_columns, column_units)
    else:
        return []


def service_get_conesearch_all(catalogs, request, path):
    """
    This functions returns the conesearch matches, given a request,
    for all catalogs. It uses the 'service_get_conesearch' function
    to generate this result.

    Args:
        catalogs (list): name of the available catalogs.
        request (dict): contains the ra, dec, and radius.
        path (string): path of the catalogs.

    Returns:
        A dictionary containing the matches for each catalog.
    """
    # append the results of each catalog
    final_result = {}
    for catalog in catalogs:
        request.catalog = catalog
        partial_result = service_get_conesearch(request, path)
        if partial_result != {}:
            final_result[catalog] = partial_result

    return final_result


def service_get_crossmatch(request, path, map_ra_dec, radius_dict):
    """
    This function returns all the crossmatch matches, given a request, for a
    specific catalog. It uses the catsHTM conesearch function for this.

    Args:
        catalog (string): name of the catalog.
        request (dict): contains the ra, dec, and radius.
        path (string): path of the catalog.
        map_ra_dec (dict): map for request ra, dec to adjust to catalog ra, dec.
        radius_dict (dict): contains the default radius to use on each catalog.

    Returns:
        A list containing all the matches.
    """
    if request.radius == None:
        request.radius = float(radius_dict.get(request.catalog, 50))

    match, catalog_columns, column_units = cone_search(
        request.catalog, request.ra, request.dec, request.radius, path
    )
    if len(match) != 0:
        return parse_crossmatch(
            match,
            request.catalog,
            request.ra,
            request.ra,
            catalog_columns,
            column_units,
            map_ra_dec,
        )

    else:
        return []


def service_get_crossmatch_all(catalogs, request, path, map_ra_dec, radius_dict):
    """
    This functions returns the crossmatch matches, given a request,
    for all catalogs. It uses the 'service_get_crossmatch' function
    to generate this result.

    Args:
        catalogs (list): name of the available catalogs.
        request (dict): contains the ra, dec, and radius.
        path (string): path of the catalogs.
        map_ra_dec (dict): map for request ra, dec to adjust to catalog ra, dec.
        radius_dict (dict): contains the default radius to use on each catalog.

    Returns:
        A dictionary containing the matches for each catalog.
    """
    final_result = {}
    for catalog in catalogs:
        request.catalog = catalog
        partial_result = service_get_crossmatch(request, path, map_ra_dec, radius_dict)
        # append the partial result if it is not empty
        if partial_result != {}:
            final_result[catalog] = partial_result
    return final_result
