# cats_service
catsHTM xmatch service

#one catalog
curl "localhost:5000/crossmatch?catalog=GAIADR1&ra=5.049097899679436119e-02&dec=2.443460952792061147e-06&radius=3600"


#all catalogs
curl "localhost:5000/crossmatch_all?ra=5.049097899679436119e-02&dec=2.443460952792061147e-06&radius=300"
