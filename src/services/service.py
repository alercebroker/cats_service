from catsHTM import cone_search
from src.models.parse import parse_conesearch, parse_crossmatch


class ConesearchDto:
    def __init__(self, catalog, ra, dec, radius, path):
        self.catalog = catalog
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.path = path


class ConesearchAllDto:
    def __init__(self, catalogs, ra, dec, radius, path):
        self.catalogs = catalogs
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.path = path


class CrossmatchDto:
    def __init__(self, catalog, ra, dec, radius, path, map_ra_dec, radius_dict):
        self.catalog = catalog
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.path = path
        self.map_ra_dec = map_ra_dec
        self.radius_dict = radius_dict


class CrossmatchAllDto:
    def __init__(self, catalogs, ra, dec, radius, path, map_ra_dec, radius_dict):
        self.catalogs = catalogs
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.path = path
        self.map_ra_dec = map_ra_dec
        self.radius_dict = radius_dict


def service_get_conesearch(conesearch_dto):
    """
    This function returns all the conesearch matches, given a request, for a
    specific catalog. It uses the catsHTM conesearch function for this.

    Args:
        conesearch_dto (ConesearchDto): contains catalog, ra, dec, radius and path.
        path (string): path of the catalog.

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


def service_get_conesearch_all(conesearch_all_dto):
    """
    This functions returns the conesearch matches, given a request,
    for all catalogs. It uses the 'service_get_conesearch' function
    to generate this result.

    Args:
        catalogs (list): name of the available catalogs.
        params (ConesearchAllInput): contains the ra, dec, and radius.
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


def service_get_crossmatch(crossmatch_dto):
    """
    This function returns all the crossmatch matches, given a request, for a
    specific catalog. It uses the catsHTM conesearch function for this.

    Args:
        params (CrossmatchInput): contains the catalog, ra, dec, and radius.
        path (string): path of the catalog.
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


def service_get_crossmatch_all(crossmatch_all_dto):
    """
    This functions returns the crossmatch matches, given a request,
    for all catalogs. It uses the 'service_get_crossmatch' function
    to generate this result.

    Args:
        catalogs (list): name of the available catalogs.
        params (CrossmatchAllInput): contains the ra, dec, and radius.
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
