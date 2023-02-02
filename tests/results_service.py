catalogs = [
    "TMASSxsc",
    "AAVSO_VSX",
    "AKARI",
    "CRTS_per_var",
    "FIRST",
    "NVSS",
    "ROSATfsc",
    "SWIREz",
]

distance_result = [{'distance': 71.86145556680134, 'ra': 0.0177356731, 'dec': -0.000204058073}]


# primer caso del conesearch catalog = "FIRST", ra = 1, dec = 0, radius = 200
cone_search_result1_1 = [
    [
        1.77356731e-02,
        -2.04058073e-04,
        1.40530020e-02,
    ]
]
cone_search_result1_2 = [
    "RA",
    "Dec",
    "SideProb",
]
cone_search_result1_3 = [
    "rad",
    "rad",
    " ",
]
service_cone_search_result1 = [
    {"attribute_name": "RA", "units": "deg", "values": [1.0161792162935126]},
    {"attribute_name": "Dec", "units": "deg", "values": [-0.011691666358208579]},
    {"attribute_name": "SideProb", "units": " ", "values": [0.014053001999855042]},
]

# segundo caso del conesearch catalog = "First", ra = 0, dec = 0, radius = 0 (no encuentra coincidencias)

cone_search_result2_1 = []
cone_search_result2_2 = [
    "RA",
    "Dec",
    "SideProb",
]
cone_search_result2_3 = [
    "rad",
    "rad",
    " ",
]
service_cone_search_result2 = {}


# primer caso del conesearch_all ra = 1, dec = 0, radius = 200
service_cone_search_result1_1 = [
    {"attribute_name": "RA", "units": "deg", "values": []},
    {"attribute_name": "Dec", "units": "deg", "values": []},
    {"attribute_name": "r_K20e", "units": "arcsec", "values": []},
]
service_cone_search_result1_2 = [
    {"attribute_name": "RA", "units": "deg", "values": []},
    {"attribute_name": "Dec", "units": "deg", "values": []},
    {"attribute_name": "VarFlag", "units": " ", "values": []},
]
service_cone_search_result1_3 = [
    {"attribute_name": "RA_rad", "units": "deg", "values": []},
    {"attribute_name": "Dec_rad", "units": "deg", "values": []},
    {"attribute_name": "RA_arcsec", "units": "arcsec", "values": []},
]
service_cone_search_result1_4 = {}
service_cone_search_result1_5 = [
    {"attribute_name": "RA", "units": "deg", "values": [1.0161792162935126]},
    {"attribute_name": "Dec", "units": "deg", "values": [-0.011691666358208579]},
    {"attribute_name": "SideProb", "units": " ", "values": [0.014053001999855042]},
]
service_cone_search_result1_6 = [
    {"attribute_name": "RA", "units": "deg", "values": [1.0159166666666666]},
    {"attribute_name": "Dec", "units": "deg", "values": [-0.011666666666674423]},
    {"attribute_name": "errRA", "units": "deg", "values": [0.000541666655437425]},
]
service_cone_search_result1_7 = [
    {"attribute_name": "RA", "units": "deg", "values": []},
    {"attribute_name": "Dec", "units": "deg", "values": []},
    {"attribute_name": "errPosition", "units": "arcsec", "values": []},
]
service_cone_search_result1_8 = {}

service_cone_search_all_result1 = {
    "TMASSxsc": [
        {"attribute_name": "RA", "units": "deg", "values": []},
        {"attribute_name": "Dec", "units": "deg", "values": []},
        {"attribute_name": "r_K20e", "units": "arcsec", "values": []},
 
    ],
    "AAVSO_VSX": [
        {"attribute_name": "RA", "units": "deg", "values": []},
        {"attribute_name": "Dec", "units": "deg", "values": []},
        {"attribute_name": "VarFlag", "units": " ", "values": []},

    ],
    "AKARI": [
        {"attribute_name": "RA_rad", "units": "deg", "values": []},
        {"attribute_name": "Dec_rad", "units": "deg", "values": []},
        {"attribute_name": "RA_arcsec", "units": "arcsec", "values": []},

    ],
    "FIRST": [
        {"attribute_name": "RA", "units": "deg", "values": [1.0161792162935126]},
        {"attribute_name": "Dec", "units": "deg", "values": [-0.011691666358208579]},
        {"attribute_name": "SideProb", "units": " ", "values": [0.014053001999855042]},
    ],
    "NVSS": [
        {"attribute_name": "RA", "units": "deg", "values": [1.0159166666666666]},
        {"attribute_name": "Dec", "units": "deg", "values": [-0.011666666666674423]},
        {"attribute_name": "errRA", "units": "deg", "values": [0.000541666655437425]},
    ],
    "ROSATfsc": [
        {"attribute_name": "RA", "units": "deg", "values": []},
        {"attribute_name": "Dec", "units": "deg", "values": []},
        {"attribute_name": "errPosition", "units": "arcsec", "values": []},
    ],
}

# segundo caso del conesearch_all ra = 0, dec = 0, radius = 0 (catalogos vacios, este caso engloba numeros negativos o 0)

service_cone_search_result2_1 = {}
service_cone_search_result2_2 = {}
service_cone_search_result2_3 = {}
service_cone_search_result2_4 = {}
service_cone_search_result2_5 = {}
service_cone_search_result2_6 = {}
service_cone_search_result2_7 = {}
service_cone_search_result2_8 = {}

service_cone_search_all_result2 = {}


# primer caso del crossmatch catalog = "FIRST", ra = 1, dec = 0, radius = 200 (entrega resultados)

cross_match_result1_1 = [
    [
        1.77356731e-02,
        -2.04058073e-04,
        1.40530020e-02,
    ]
]
cross_match_result1_2 = [
    "RA",
    "Dec",
    "SideProb",
]
cross_match_result1_3 = [
    "rad",
    "rad",
    " ",
]

service_cross_match_result1 = [
    {"attribute_name": "RA", "value": 1.0161792162935126, "units": "deg"},
    {"attribute_name": "Dec", "value": -0.011691666358208579, "units": "deg"},
    {"attribute_name": "SideProb", "value": 0.014053001999855042, "units": " "},
    {"attribute_name": "distance", "value": 71.86145556680134, "units": "arcsec"},
]

# segundo caso del crossmatch catalog = "FIRST", ra = 1, dec = 0, radius = 0(no entrega resultados)

cross_match_result2_1 = []
cross_match_result2_2 = [
    "RA",
    "Dec",
    "SideProb",
]
cross_match_result2_3 = [
    "rad",
    "rad",
    " ",
]
service_cross_match_result2 = {}


# tercer caso del crossmatch catalog = "FIRST", ra = 1, dec = 0 sin radius

cross_match_result3_1 = []
cross_match_result3_2 = [
    "RA",
    "Dec",
    "SideProb",
]
cross_match_result3_3 = [
    "rad",
    "rad",
    " ",
]
service_cross_match_result3 = {}


# primer caso del crossmatch all  ra = 1, dec = 0 radius = 200

service_cross_match_result1_1 = {}
service_cross_match_result1_2 = {}
service_cross_match_result1_3 = {}
service_cross_match_result1_4 = {}
service_cross_match_result1_5 = [
    {"attribute_name": "RA", "value": 1.0161792162935126, "units": "deg"},
    {"attribute_name": "Dec", "value": -0.011691666358208579, "units": "deg"},
    {"attribute_name": "SideProb", "value": 0.014053001999855042, "units": " "},
    {"attribute_name": "distance", "value": 71.86145556680134, "units": "arcsec"},
]
service_cross_match_result1_6 = [
    {"attribute_name": "RA", "value": 1.0159166666666666, "units": "deg"},
    {"attribute_name": "Dec", "value": -0.011666666666674423, "units": "deg"},
    {"attribute_name": "errRA", "value": 0.000541666655437425, "units": "deg"},
    {"attribute_name": "distance", "value": 71.04428164620468, "units": "arcsec"},
]
service_cross_match_result1_7 = {}
service_cross_match_result1_8 = {}

service_cross_match_all_result1 = {
    "FIRST": [
        {"attribute_name": "RA", "value": 1.0161792162935126, "units": "deg"},
        {"attribute_name": "Dec", "value": -0.011691666358208579, "units": "deg"},
        {"attribute_name": "SideProb", "value": 0.014053001999855042, "units": " "},
        {"attribute_name": "distance", "value": 71.86145556680134, "units": "arcsec"},
    ],
    "NVSS": [
        {"attribute_name": "RA", "value": 1.0159166666666666, "units": "deg"},
        {"attribute_name": "Dec", "value": -0.011666666666674423, "units": "deg"},
        {"attribute_name": "errRA", "value": 0.000541666655437425, "units": "deg"},
        {"attribute_name": "distance", "value": 71.04428164620468, "units": "arcsec"},
    ],
}



service_cross_match_result2_1 = {}
service_cross_match_result2_2 = {}
service_cross_match_result2_3 = {}
service_cross_match_result2_4 = {}
service_cross_match_result2_5 = {}
service_cross_match_result2_6 = {}
service_cross_match_result2_7 = {}
service_cross_match_result2_8 = {}

service_cross_match_all_result2 = {}


service_cross_match_result3_1 = {}
service_cross_match_result3_2 = {}
service_cross_match_result3_3 = {}
service_cross_match_result3_4 = {}
service_cross_match_result3_5 = {}
service_cross_match_result3_6 = {}
service_cross_match_result3_7 = {}
service_cross_match_result3_8 = {}

service_cross_match_all_result3 = {}