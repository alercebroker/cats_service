from src.presentation.presenter import json, catname, catname_all
import os
from math import radians
from src.services.service import (
    service_get_conesearch,
    service_get_crossmatch,
    service_get_conesearch_all,
    service_get_crossmatch_all,
)
from src.controllers.constants import radius_dict, map_ra_dec, catalog_map


def controller_conesearch(catalog, request):

    try:
        # get arguments
        catalog = catalog
        # convert ra and dec to radians
        request["ra"] = radians(float(request["ra"]))
        request["dec"] = radians(float(request["dec"]))
        request["radius"] = float(request["radius"])
        path = os.environ["DATA_PATH"]
    except BaseException:
        return json("Request contains one or more invalid arguments.")

    return json(
        catname(service_get_conesearch(catalog, request, path), catalog_map, catalog)
    )


def controller_conesearch_all(request):

    catalogs = os.environ["CATALOGS"].split(",")
    try:
        request["ra"] = radians(float(request["ra"]))
        request["dec"] = radians(float(request["dec"]))
        request["radius"] = float(request["radius"])
        path = os.environ["DATA_PATH"]
    except BaseException:
        return "Request contains one or more invalid arguments."
    return json(
        catname_all(service_get_conesearch_all(catalogs, request, path), catalog_map)
    )


def controller_crossmatch(catalog, request):

    try:
        # get arguments
        catalog = catalog
        # convert ra and dec to radians
        request["ra"] = radians(float(request["ra"]))
        request["dec"] = radians(float(request["dec"]))
        path = os.environ["DATA_PATH"]
    except BaseException:
        return json("Request contains one or more invalid arguments.")

    return json(service_get_crossmatch(catalog, request, path, map_ra_dec, radius_dict))


def controller_crossmatch_all(request):

    catalogs = os.environ["CATALOGS"].split(",")
    try:
        request["ra"] = radians(float(request["ra"]))
        request["dec"] = radians(float(request["dec"]))
        path = os.environ["DATA_PATH"]
    except BaseException:
        return json("Request contains one or more invalid arguments.")

    # check if a value for radius was provided

    return json(
        catname_all(
            service_get_crossmatch_all(
                catalogs, request, path, map_ra_dec, radius_dict
            ),
            catalog_map,
        )
    )
