import os
from math import radians
from src.services.service import (
    service_get_conesearch,
    service_get_crossmatch,
    service_get_conesearch_all,
    service_get_crossmatch_all,
)
from src.controllers.constants import radius_dict, map_ra_dec
from src.services.dtos import (
    ConesearchDto,
    ConesearchAllDto,
    CrossmatchDto,
    CrossmatchAllDto,
)


def controller_conesearch(params):
    # get arguments
    # convert ra and dec to radians

    conesearch_dto = ConesearchDto(
        params.catalog,
        radians(params.ra),
        radians(params.dec),
        params.radius,
        os.environ["DATA_PATH"],
    )

    return service_get_conesearch(conesearch_dto)


def controller_conesearch_all(params):

    conesearch_all_dto = ConesearchAllDto(
        os.environ["CATALOGS"].split(","),
        radians(params.ra),
        radians(params.dec),
        params.radius,
        os.environ["DATA_PATH"],
    )

    return service_get_conesearch_all(conesearch_all_dto)


def controller_crossmatch(params):
    # get arguments
    # convert ra and dec to radians
    params.ra = radians(params.ra)
    params.dec = radians(params.dec)
    path = os.environ["DATA_PATH"]

    crossmatch_dto = CrossmatchDto(
        params.catalog,
        radians(params.ra),
        radians(params.dec),
        params.radius,
        os.environ["DATA_PATH"],
        map_ra_dec,
        radius_dict,
    )

    return service_get_crossmatch(crossmatch_dto)


def controller_crossmatch_all(params):
    crossmatch_all_dto = CrossmatchAllDto(
        os.environ["CATALOGS"].split(","),
        radians(params.ra),
        radians(params.dec),
        params.radius,
        os.environ["DATA_PATH"],
        map_ra_dec,
        radius_dict,
    )

    return service_get_crossmatch_all(crossmatch_all_dto)
