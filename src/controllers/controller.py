import os
from math import radians
from src.services.service import (
    service_get_conesearch,
    service_get_crossmatch,
    service_get_conesearch_all,
    service_get_crossmatch_all,
)
from src.controllers.constants import radius_dict, map_ra_dec


def controller_conesearch(params):
    # get arguments
    # convert ra and dec to radians
    params.ra = radians(params.ra)
    params.dec = radians(params.dec)
    path = os.environ["DATA_PATH"]

    return service_get_conesearch(params, path)


def controller_conesearch_all(params):
    catalogs = os.environ["CATALOGS"].split(",")
    params.ra = radians(params.ra)
    params.dec = radians(params.dec)
    path = os.environ["DATA_PATH"]

    return service_get_conesearch_all(catalogs, params, path)


def controller_crossmatch(params):
    # get arguments
    # convert ra and dec to radians
    params.ra = radians(params.ra)
    params.dec = radians(params.dec)
    path = os.environ["DATA_PATH"]

    return service_get_crossmatch(params, path, map_ra_dec, radius_dict)


def controller_crossmatch_all(params):
    catalogs = os.environ["CATALOGS"].split(",")
    params.ra = radians(params.ra)
    params.dec = radians(params.dec)
    path = os.environ["DATA_PATH"]

    return service_get_crossmatch_all(catalogs, params, path, map_ra_dec, radius_dict)
