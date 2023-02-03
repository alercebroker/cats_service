from src.models.model_conesearch import ModelConesearch
from src.models.model_cross_match import ModelCrossMatch
import pandas as pd


def parse_conesearch(match, catalog_columns, column_units):
    model = ModelConesearch(match, catalog_columns, column_units)

    try:
        df = pd.DataFrame(match, columns=catalog_columns)
    except ValueError as ex:
        return {}

    df.columns = model.rename_duplicated_columns()
    result = model.replace_nan_inf_and_convert_degrees(df)

    return result


def parse_crossmatch(
    match, catalog, ra, dec, catalog_columns, column_units, map_ra_dec
):
    model = ModelCrossMatch(
        match, catalog, ra, dec, catalog_columns, column_units, map_ra_dec
    )

    try:
        # dataframe to match columns to values
        df = pd.DataFrame(match, columns=catalog_columns)
        # add distance column to df
        df["distance"] = None
    except BaseException:
        return {}

    result = model.check_ra_dec_instance(df)

    return model.format_result_with_units(result)
