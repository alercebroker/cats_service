from src.models.model_conesearch import ModelConesearch
from src.models.model_cross_match import ModelCrossMatch


def parse_conesearch(match, catalog_columns, column_units):

    model = ModelConesearch(match, catalog_columns, column_units)
    return model.return_format()


def parse_crossmatch(
    match, catalog, ra, dec, catalog_columns, column_units, map_ra_dec
):
    model = ModelCrossMatch(
        match, catalog, ra, dec, catalog_columns, column_units, map_ra_dec
    )

    return model.return_format()
