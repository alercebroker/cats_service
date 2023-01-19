from service.presenter import json,catname, catname_all
import os 
from math import radians
from service.service import service_get_conesearch, service_get_crossmatch, service_get_conesearch_all, service_get_crossmatch_all
from service.constants import radius_dict, map_ra_dec, catalog_map

def controller_conesearch(request):

    try:
        # get arguments
        catalog = request.args.get("catalog")
        # convert ra and dec to radians
        ra = radians(float(request.args.get("ra")))
        dec = radians(float(request.args.get("dec")))
        radius = float(request.args.get("radius"))
        path = os.environ["DATA_PATH"]
    except BaseException:
        return json("Request contains one or more invalid arguments.")

    return json(catname(service_get_conesearch(catalog, ra, dec, radius, path), catalog_map, catalog))


def controller_conesearch_all(request):

    catalogs = os.environ["CATALOGS"].split(",")
    try:
        ra = radians(float(request.args.get("ra")))
        dec = radians(float(request.args.get("dec")))
        radius = float(request.args.get("radius"))
        path = os.environ["DATA_PATH"]
    except BaseException:
        return "Request contains one or more invalid arguments."
    return json(catname_all(service_get_conesearch_all(catalogs, ra, dec ,radius, path), catalog_map))



def controller_crossmatch(request):

    try:
        # get arguments
        catalog = request.args.get("catalog")
        # convert ra and dec to radians
        ra = radians(float(request.args.get("ra")))
        dec = radians(float(request.args.get("dec")))
        path = os.environ["DATA_PATH"]
    except BaseException:
        return json("Request contains one or more invalid arguments.")

    try:
        radius = float(request.args.get("radius"))
    except BaseException:
        # if no radius was provided, use the default value
        radius = float(radius_dict.get(50))
        
    return json(service_get_crossmatch(catalog, ra, dec, radius, path,map_ra_dec))



def controller_crossmatch_all(request):

    catalogs = os.environ["CATALOGS"].split(",")
    try:
        ra = radians(float(request.args.get("ra")))
        dec = radians(float(request.args.get("dec")))
        path = os.environ["DATA_PATH"]
    except BaseException:
        return json("Request contains one or more invalid arguments.")

    # check if a value for radius was provided
    radius = None
    try:
        radius = float(request.args.get("radius"))
    except BaseException:
        # if no radius was provided, use the default value
        radius = float(radius_dict.get(50))
    return json(catname_all(service_get_crossmatch_all(catalogs, ra, dec ,radius,path, map_ra_dec),catalog_map))

