# cats_service
catsHTM xmatch service

RA and Dec in degrees, radius in arcsecs. Available catalogs are: 'FIRST', 'TMASS', 'TMASSxsc', 'DECaLS', 'GAIADR1', 'GAIADR2', 'GALEX', 'HSCv2', 'IPHAS', 'NEDz', 'SDSSDR10', 'SDSSoffset', 'SpecSDSS', 'SAGE', 'IRACgc', 'UKIDSS', 'VISTAviking', 'VSTatlas', 'VSTkids', 'AKARI', 'APASS', 'NVSS', 'Cosmos', 'PTFpc', 'ROSATfsc', 'SkyMapper', 'UCAC4', 'WISE', 'XMM', 'AAVSO_VSX', 'unWISE', 'SWIREz', 'Simbad_PM200' and 'CRTS_per_var'.

#one catalog
curl "catshtm.alerce.online:5000/crossmatch?catalog=GAIADR1&ra=357.733730043103&dec=14.2051386793103&radius=100"

#all catalogs
curl "catshtm.alerce.online:5000/crossmatch_all?ra=357.733730043103&dec=14.2051386793103&radius=100"
