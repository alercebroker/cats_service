import pandas as pd
import numpy as np
from math import radians, degrees

class ModelConesearch:

    def __init__(self, match, catalog_columns,column_units):
        self.match = match
        self.catalog_columns = catalog_columns
        self.column_units = column_units
    
    def rename_duplicated_columns(self):
        duplicated_columns = [ col for col in self.catalog_columns if list(self.catalog_columns).count(col) > 1 ]
        ran = 0
        for col in duplicated_columns:
            for idx in range(ran, len(self.catalog_columns)):
                if self.catalog_columns[idx] == col:
                    self.catalog_columns[idx] = f"{col}_{self.column_units[idx]}"
                    ran = idx
                    break
        return self.catalog_columns
    
    def replace_nan_inf_and_convert_degrees(self,df):
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
                attribute_dict = {"attribute_name": column, "unit": "deg", "values": values}
            else:
                attribute_dict = {"attribute_name": column, "unit": unit, "values": values}
            results.append(attribute_dict)
        return results


    def return_format(self):
        try:
            df = pd.DataFrame(self.match, columns = self.catalog_columns)
        except ValueError as ex:
            return {}
            
        df.columns = self.rename_duplicated_columns()
        return self.replace_nan_inf_and_convert_degrees(df)
    
    def unit_is_rad(self,unit):

        return unit == "rad"