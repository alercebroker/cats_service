import pandas as pd
import numpy as np
from astropy import units
from astropy.coordinates import SkyCoord
from math import radians, degrees


class ModelCrossMatch:
    def __init__(
        self, match, catalog, ra, dec, catalog_columns, column_units, map_ra_dec
    ):
        self.match = match
        self.catalog = catalog
        self.ra = ra
        self.dec = dec
        self.catalog_columns = catalog_columns
        self.column_units = column_units
        self.map_ra_dec = map_ra_dec

    def check_ra_dec_instance(self, df):
        matches = []
        # append distance unit
        self.column_units = np.append(self.column_units, "arcsec")
        for index, row in df.iterrows():
            obj = dict(zip(self.catalog_columns, row.values))
            matches.append(obj)
        # this object is a list with a dictionary containing
        # the ra, dec of the closest matching object
        try:
            closest_ra_dec = self.get_min_distance(
                matches, self.catalog, self.ra, self.dec
            )
        except BaseException:
            return {}
        # get all the fields of the matching object
        ra_cat, dec_cat = self.map_ra_dec.get(self.catalog, ("RA", "Dec"))
        result = {}
        for index, row in df.iterrows():
            # check type of ra
            if isinstance(row[ra_cat], float):
                ra_equal = row[ra_cat] == closest_ra_dec[0]["ra"]
            else:
                ra_equal = row[ra_cat].iloc[0] == closest_ra_dec[0]["ra"]
            # check type of dec
            if isinstance(row[dec_cat], float):
                dec_equal = row[dec_cat] == closest_ra_dec[0]["dec"]
            else:
                dec_equal = row[dec_cat].iloc[0] == closest_ra_dec[0]["dec"]
            if ra_equal and dec_equal:
                # add distance to result
                row["distance"] = closest_ra_dec[0]["distance"]
                result = row.to_dict()
                break

        return result

    def get_min_distance(self, matches, catalog, ra, dec):
        """
        Get the element with the minimum distance between the cone search matches.
        Args:
            matches (list): list of cone search matches for a catalog.
            catalog (string): name of the catalog.
            ra (float): ra coordinate of the point to search in degrees.
            dec (float): dec coordinate of the point to search in degrees.
        Returns:
            A list containing the closest element (distance, ra, dec).
        """
        ra_cat, dec_cat = self.map_ra_dec.get(catalog, ("RA", "Dec"))
        # XMM special case
        if catalog == "XMM":
            unit = units.degree
        else:
            unit = units.radian
        distances = []
        # get distance between points in arcseconds
        for match in matches:
            point_cat = SkyCoord(
                ra=float(match[ra_cat]) * unit, dec=float(match[dec_cat]) * unit
            )
            point_requested = SkyCoord(ra=float(ra) * unit, dec=float(dec) * unit)
            distances.append(
                dict(
                    distance=point_requested.separation(point_cat).arcsecond,
                    ra=match[ra_cat],
                    dec=match[dec_cat],
                )
            )
        # get minimum distance
        if distances:
            min_distance = min([float(x["distance"]) for x in distances])
            # list with a dictionary with the min distance, ra and dec
            return list(filter(lambda x: x["distance"] == min_distance, distances))
        return None

    def format_result_with_units(self, result):
        results_list = []
        result_with_units = {}

        for key, unit in zip(result, self.column_units):
            value = result[key]
            if self.unit_is_rad(unit):
                # convert unit to deg
                result_with_units = {
                    "attribute_name": key,
                    "unit": "deg",
                    "value": None if np.isnan(value) else degrees(value),
                }
            else:
                result_with_units = {
                    "attribute_name": key,
                    "unit": unit,
                    "value": None if np.isnan(value) else value,
                }
            results_list.append(result_with_units)

        # replace inf
        for attribute in results_list:
            if attribute["value"] == np.inf:
                attribute["value"] = "infinity"

        return results_list

    def unit_is_rad(self, unit):
        """
        Checks if unit is rad, and returns True or False accordingly.
        Args:
            unit (string): the unit.
        Returns:
            A boolean stating if the input units was radian or not.
        """
        return unit == "rad"
