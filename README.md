# cats_service
This is a crossmatch service based on https://github.com/maayane/catsHTM. The service provides conesearch and crossmatch over different [catalogs](#available-catalogs).

#### Arguments and units in requests

The arguments needed are almost always the name of the `catalog`, `ra` and `dec` in degrees and `radius` in arcsec.

#### Conesearch in a catalog

`curl "catshtm.alerce.online/conesearch?catalog=GAIADR1&ra=357.733730043103&dec=14.2051386793103&radius=100"`

#### Conesearch over all catalogs

`curl "catshtm.alerce.online/conesearch_all?ra=357.733730043103&dec=14.2051386793103&radius=10"`

#### Crossmatch in a catalog

There are two ways to perform crossmatch in a catalog.

Providing a radius:

`curl "catshtm.alerce.online/crossmatch?catalog=SDSSDR10&ra=357.733730043103&dec=14.2051386793103&radius=100"`

Not providing one:

`curl "catshtm.alerce.online/crossmatch?catalog=SDSSDR10&ra=357.733730043103&dec=14.2051386793103"`

If a radius is provided, then that value is used. If not, then the default value for that catalog is used. See default values in [Available catalogs](#available-catalogs)

#### Crossmatch over all catalogs

For crossmatching over all catalogs, the same rule of providing or not providing a radius applies. Therefore, there are two ways to send the request:

With radius:

`curl "catshtm.alerce.online/crossmatch_all?ra=357.733730043103&dec=14.2051386793103&radius=100"`

Without radius:

`curl "catshtm.alerce.online/crossmatch_all?ra=357.733730043103&dec=14.2051386793103"`

#### Available catalogs:

For the catalogs that do not have a value listed, the default radius is 50 arcsec.

- AAVSO_VSX
- AKARI
- APASS (2 arcsec)
- CRTS_per_var
- Cosmos
- DECaLS (0.1 arcsec)
- FIRST
- GAIADR1 (0.1 arcsec)
- GAIADR2 (0.1 arcsec)
- GALEX
- HSCv2
- IPHAS
- IRACgc
- NEDz
- NVSS (10.8 arcsec)
- PTFpc
- ROSATfsc
- SAGE
- SDSSDR10
- SDSSoffset (0.1 arcsec)
- SWIREz
- SkyMapper (0.4 arcsec)
- SpecSDSS
- TMASS
- TMASSxsc
- UCAC4
- UKIDSS
- VISTAviking
- VSTatlas
- VSTkids
- WISE
- XMM (8 arcsec)
- unWISE
