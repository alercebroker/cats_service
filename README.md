# cats_service
This is a crossmatch service based on https://github.com/maayane/catsHTM. The service provides conesearch and crossmatch over different [catalogs](#available-catalogs).

#### Arguments and units in requests

The arguments needed are almost always the name of the `catalog`, `ra` and `dec` in degress and `radius` in arcsec.

#### Conesearch in a catalog

`curl "catshtm.alerce.online:5000/conesearch?catalog=GAIADR1&ra=357.733730043103&dec=14.2051386793103&radius=100"`

#### Conesearch over all catalogs

`curl "catshtm.alerce.online:5000/conesearch_all?ra=357.733730043103&dec=14.2051386793103&radius=10"`

#### Crossmatch in a catalog

`curl "catshtm.alerce.online:5000/crossmatch?catalog=SDSSDR10&ra=357.733730043103&dec=14.2051386793103&radius=100"`

#### Crossmatch over all catalogs

`curl "catshtm.alerce.online:5000/crossmatch_all?ra=357.733730043103&dec=14.2051386793103&radius=100"`

#### Available catalogs:
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
