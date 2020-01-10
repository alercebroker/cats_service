# ALeRCE [Cats Service](http://catshtm.alerce.online)
[![Documentation Status](https://readthedocs.org/projects/alerce/badge/?version=latest)](https://alerceapi.readthedocs.io/en/latest/catshtm.html)

Cats Service provides conesearch and cross-match on different [catalogs](#available-catalogs). It is based on [catsHTM](https://github.com/maayane/catsHTM).

#### Arguments and units in requests

The arguments needed are almost always the name of the `catalog`, `ra` and `dec` in degrees and `radius` in arcsec.

#### Conesearch on a catalog

```
curl "catshtm.alerce.online/conesearch?catalog=GAIADR1&ra=357.73373004&dec=14.20513868&radius=100"
```

#### Conesearch on all catalogs

```
curl "catshtm.alerce.online/conesearch?catalog=GAIADR1&ra=357.73373004&dec=14.20513868&radius=100"
```

#### Crossmatch on a catalog

Since the radius argument is optional, there are two ways to perform cross-match on a catalog.

1. Providing a radius:

```
curl "catshtm.alerce.online/crossmatch?catalog=GAIADR1&ra=357.73373004&dec=14.20513868&radius=100"
```

2. Not providing one:

```
curl "catshtm.alerce.online/crossmatch?catalog=GAIADR1&ra=357.73373004&dec=14.20513868"
```

If a radius is provided, then that value is used. If not, the default value for that catalog is used. See default values in [Available catalogs](#available-catalogs).

#### Crossmatch on all catalogs

For cross-matching on all catalogs, the same rule of providing a radius or not applies. Therefore, there are two ways to send the request.

1. With a value for the radius:

```
curl "catshtm.alerce.online/crossmatch_all?ra=357.733730043103&dec=14.2051386793103&radius=100"
```

2. Without one:

```
curl "catshtm.alerce.online/crossmatch_all?ra=357.733730043103&dec=14.2051386793103"
```

#### Available catalogs:
For catalogs that have a value listed, this value is the radius used for cone search and cross-match. Otherwise, the default radius of 50 arcsec is used.
```
- AAVSO_VSX
- AKARI
- APASS (2 arcsec)
- CRTS_per_var
- Cosmos
- DECaLS (0.1 arcsec)
- FIRST
- GAIADR1 (0.2 arcsec)
- GAIADR2 (0.2 arcsec)
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
```
