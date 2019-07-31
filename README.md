# cats_service
catsHTM xmatch service

# to crossmatch one catalog

`curl "catshtm.alerce.online:5000/crossmatch?catalog=GAIADR1&ra=357.733730043103&dec=14.2051386793103&radius=100"`

# to crosmatch all catalogs

`curl "catshtm.alerce.online:5000/crossmatch_all?ra=357.733730043103&dec=14.2051386793103&radius=100"`

`RA` and `Dec` in `degrees`, `radius` in `arcsecs`.

Available catalogs are:
- AAVSO_VSX
- AKARI
- APASS
- CRTS_per_var
- Cosmos
- DECaLS
- FIRST
- GAIADR1
- GAIADR2
- GALEX
- HSCv2
- IPHAS
- IRACgc
- NEDz
- NVSS
- PTFpc
- ROSATfsc
- SAGE
- SDSSDR10
- SDSSoffset
- SWIREz
- SkyMapper
- SpecSDSS
- TMASS
- TMASSxsc
- UCAC4
- UKIDSS
- VISTAviking
- VSTatlas
- VSTkids
- WISE
- XMM
- unWISE
