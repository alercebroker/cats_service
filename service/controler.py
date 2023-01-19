from service.presenter import json,catname, catname_all
import os 
from math import radians
from service.service import service_get_conesearch, service_get_crossmatch, service_get_conesearch_all, service_get_crossmatch_all
from service.constants import radius_dict, map_ra_dec, catalog_map

def controller_conesearch(catalog, ra, dec, radius):

    try:
        # get arguments
        catalog = catalog
        # convert ra and dec to radians
        ra = radians(float(ra))
        dec = radians(float(dec))
        radius = float(radius)
        path = os.environ["DATA_PATH"]
    except BaseException:
        return json("Request contains one or more invalid arguments.")

    return json(catname(service_get_conesearch(catalog, ra, dec, radius, path), catalog_map, catalog))


def controller_conesearch_all(ra, dec, radius):

    catalogs = os.environ["CATALOGS"].split(",")
    try:
        ra = radians(float(ra))
        dec = radians(float(dec))
        radius = float(radius)
        path = os.environ["DATA_PATH"]
    except BaseException:
        return "Request contains one or more invalid arguments."
    return json(catname_all(service_get_conesearch_all(catalogs, ra, dec ,radius, path), catalog_map))



def controller_crossmatch(catalog, ra, dec, radius):

    try:
        # get arguments
        catalog = catalog
        # convert ra and dec to radians
        ra = radians(float(ra))
        dec = radians(float(dec))
        path = os.environ["DATA_PATH"]
    except BaseException:
        return json("Request contains one or more invalid arguments.")
    radius = None
    try:
        radius = float(radius)
    except BaseException:
        # if no radius was provided, use the default value
        radius = float(radius_dict.get(catalog,50))

    return json(service_get_crossmatch(catalog, ra, dec, radius, path,map_ra_dec))



def controller_crossmatch_all(ra, dec, radius):

    catalogs = os.environ["CATALOGS"].split(",")
    try:
        ra = radians(float(ra))
        dec = radians(float(dec))
        path = os.environ["DATA_PATH"]
    except BaseException:
        return json("Request contains one or more invalid arguments.")

    # check if a value for radius was provided
    try:
        radius = float(radius)
    except BaseException:
        # if no radius was provided, use the default value
        radius = float(radius_dict.get(50))
    return json(catname_all(service_get_crossmatch_all(catalogs, ra, dec ,radius,path, map_ra_dec),catalog_map))

