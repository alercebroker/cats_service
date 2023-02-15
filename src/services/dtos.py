class ConesearchDto:
    def __init__(self, catalog, ra, dec, radius, path):
        self.catalog = catalog
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.path = path


class ConesearchAllDto:
    def __init__(self, catalogs, ra, dec, radius, path):
        self.catalogs = catalogs
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.path = path


class CrossmatchDto:
    def __init__(self, catalog, ra, dec, radius, path, map_ra_dec, radius_dict):
        self.catalog = catalog
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.path = path
        self.map_ra_dec = map_ra_dec
        self.radius_dict = radius_dict


class CrossmatchAllDto:
    def __init__(self, catalogs, ra, dec, radius, path, map_ra_dec, radius_dict):
        self.catalogs = catalogs
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.path = path
        self.map_ra_dec = map_ra_dec
        self.radius_dict = radius_dict
