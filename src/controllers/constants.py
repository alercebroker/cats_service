# statistically defined radiuses, not advertised ones
radius_dict = {
    "ROSATfsc": 50,
    "XMM": 8,
    "APASS": 2,
    "DECaLS": 0.1,
    "GAIADR1": 0.1,
    "GAIADR2": 0.1,
    "NVSS": 10.8,
    "SDSSoffset": 0.1,
    "SkyMapper": 0.4,
}
# catsHTM catalog name to real name
catalog_map = {
    "TMASS": "2MASS",
    "CRTS_per_var": "CRTS",
    "GAIADR1": "GAIA/DR1",
    "GAIADR2": "GAIA/DR2",
    "SDSSDR10": "SDSS/DR10",
    "TMASSxsc": "2MASSxsc",
}
# map ra, dec to catalog ra, dec name
map_ra_dec = {
    "HSCv2": ("MatchRA", "MatchDec"),
    "XMM": ("RA", "DEC"),
    "SDSSoffset": ("ra", "dec"),
}