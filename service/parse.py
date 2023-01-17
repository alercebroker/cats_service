import model_conesearch
import model_cross_match
def parse_conesearch(match, catalog_columns, column_units):

    model = model_conesearch(match, catalog_columns,column_units)

    return model.return_format()


    return


def parse_crossmatch(match, catalog, ra, dec, catalog_columns, column_units,map_ra_dec):
    model = model_cross_match(match, catalog, ra, dec, catalog_columns, column_units, map_ra_dec)

    return model.return_format()
