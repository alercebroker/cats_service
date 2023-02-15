from catsHTM import cone_search
from src.models.parse import parse_conesearch, parse_crossmatch
from src.services.dtos import (
    ConesearchDto,
    ConesearchAllDto,
    CrossmatchDto,
    CrossmatchAllDto,
)


def service_get_conesearch(conesearch_dto: ConesearchDto):
    """
    This function returns all the conesearch matches, given a request, for a
    specific catalog. It uses the catsHTM conesearch function for this.

    Args:
        conesearch_dto (ConesearchDto): contains:
            catalog (string): name of the catalog, e.g., FIRST, AAVSO_VSX
            ra (float): ra coordinate of the point to search in degrees.
            dec (float): dec coordinate of the point to search in degrees.
            radius (float): radius of the point to search in arsec.
            path (string): path of the catalogs.

    Returns:
        A list containing all the matches.
    """
    match, catalog_columns, column_units = cone_search(
        conesearch_dto.catalog,
        conesearch_dto.ra,
        conesearch_dto.dec,
        conesearch_dto.radius,
        conesearch_dto.path,
    )

    if len(match) != 0:
        return parse_conesearch(match, catalog_columns, column_units)
    else:
        return []


def service_get_conesearch_all(conesearch_all_dto: ConesearchAllDto):
    """
    This functions returns the conesearch matches, given a request,
    for all catalogs. It uses the 'service_get_conesearch' function
    to generate this result.

    Args:
        conesearch_all_dto (ConesearchAllDto): contains:
            catalogs (list): name of the available catalogs.
            ra (float): ra coordinate of the point to search in degrees.
            dec (float): dec coordinate of the point to search in degrees.
            radius (float): radius of the point to search in arsec.
            path (string): path of the catalogs.

    Returns:
        A dictionary containing the matches for each catalog.
    """
    # append the results of each catalog
    final_result = {}
    for catalog in conesearch_all_dto.catalogs:

        conesearch_dto = ConesearchDto(
            catalog,
            conesearch_all_dto.ra,
            conesearch_all_dto.dec,
            conesearch_all_dto.radius,
            conesearch_all_dto.path,
        )

        partial_result = service_get_conesearch(conesearch_dto)
        if partial_result != {}:
            final_result[catalog] = partial_result

    return final_result


def service_get_crossmatch(crossmatch_dto: CrossmatchDto):
    """
    This function returns all the crossmatch matches, given a request, for a
    specific catalog. It uses the catsHTM conesearch function for this.

    Args:
        crossmatch_dto (CrossmatchDto): contains:
            catalog (string): name of the catalog, e.g., FIRST, AAVSO_VSX
            ra (float): ra coordinate of the point to search in degrees.
            dec (float): dec coordinate of the point to search in degrees.
            radius (float): radius of the point to search in arsec.
            path (string): path of the catalogs.
            map_ra_dec (dict): map for params ra, dec to adjust to catalog ra, dec.
            radius_dict (dict): contains the default radius to use on each catalog.

    Returns:
        A list containing all the matches.
    """
    if crossmatch_dto.radius == None:
        crossmatch_dto.radius = float(
            crossmatch_dto.radius_dict.get(crossmatch_dto.catalog, 50)
        )

    match, catalog_columns, column_units = cone_search(
        crossmatch_dto.catalog,
        crossmatch_dto.ra,
        crossmatch_dto.dec,
        crossmatch_dto.radius,
        crossmatch_dto.path,
    )
    if len(match) != 0:
        return parse_crossmatch(
            match,
            crossmatch_dto.catalog,
            crossmatch_dto.ra,
            crossmatch_dto.ra,
            catalog_columns,
            column_units,
            crossmatch_dto.map_ra_dec,
        )

    else:
        return []


def service_get_crossmatch_all(crossmatch_all_dto: CrossmatchAllDto):
    """
    This functions returns the crossmatch matches, given a request,
    for all catalogs. It uses the 'service_get_crossmatch' function
    to generate this result.

    Args:

        crossmatch_all_dto (CrossmatchAllDto): contains:
            catalogs (list): name of the available catalogs.
            ra (float): ra coordinate of the point to search in degrees.
            dec (float): dec coordinate of the point to search in degrees.
            radius (float): radius of the point to search in arsec.
            path (string): path of the catalogs.
            map_ra_dec (dict): map for params ra, dec to adjust to catalog ra, dec.
            radius_dict (dict): contains the default radius to use on each catalog.

    Returns:
        A dictionary containing the matches for each catalog.
    """
    final_result = {}
    for catalog in crossmatch_all_dto.catalogs:
        crossmatch_dto = CrossmatchDto(
            catalog,
            crossmatch_all_dto.ra,
            crossmatch_all_dto.dec,
            crossmatch_all_dto.radius,
            crossmatch_all_dto.path,
            crossmatch_all_dto.map_ra_dec,
            crossmatch_all_dto.radius_dict,
        )

        partial_result = service_get_crossmatch(crossmatch_dto)
        # append the partial result if it is not empty
        if partial_result != {}:
            final_result[catalog] = partial_result
    return final_result
