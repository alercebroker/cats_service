import pandas as pd
import numpy as np
from math import radians, degrees


class ModelConesearch:
    def __init__(self, match: list, catalog_columns: list, column_units: list):
        self.match = match
        self.catalog_columns = catalog_columns
        self.column_units = column_units

    def rename_duplicated_columns(self):
        """
        This function search for and rename duplicated catalog columns.

        Returns
            A list with the renamed columns.
        """
        duplicated_columns = [
            col
            for col in self.catalog_columns
            if list(self.catalog_columns).count(col) > 1
        ]
        ran = 0
        for col in duplicated_columns:
            for idx in range(ran, len(self.catalog_columns)):
                if self.catalog_columns[idx] == col:
                    self.catalog_columns[idx] = f"{col}_{self.column_units[idx]}"
                    ran = idx
                    break
        return self.catalog_columns

    def replace_nan_inf_and_convert_degrees(self, df):
        """
        This function replaces nan values to None, and inf values to "infinity".
        If the unit is in radians it converts the value from radians to degrees.

        Args:
            df (pd.DataFrame): contains the matches and catalog columns.

        Returns:
            A list containing each attribute name, its unit and values.
        """
        results = []
        for column, unit in zip(self.catalog_columns, self.column_units):
            attribute_dict = {}
            values = []
            for value in df[column].values.tolist():
                # replace nan and infinity
                if np.isnan(value):
                    value = None
                elif np.isinf(value):
                    value = "infinity"
                # convert radians to degrees
                elif self.unit_is_rad(unit):
                    value = degrees(value)
                values.append(value)
            if self.unit_is_rad(unit):
                attribute_dict = {
                    "attribute_name": column,
                    "unit": "deg",
                    "values": values,
                }
            else:
                attribute_dict = {
                    "attribute_name": column,
                    "unit": unit,
                    "values": values,
                }
            results.append(attribute_dict)
        return results

    def unit_is_rad(self, unit):
        """
        Checks if unit is rad, and returns True or False accordingly.
        Args:
            unit (string): the unit.
        Returns:
            A boolean stating if the input units was radian or not.
        """
        return unit == "rad"
