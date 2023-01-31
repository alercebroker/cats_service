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


# primer caso del conesearch catalog = "FIRST", ra = 1, dec = 0, radius = 200
cone_search_result1_1 = [
    [
        1.77356731e-02,
        -2.04058073e-04,
        1.40530020e-02,
        1.04300003e01,
        1.07168760e01,
        1.08766742e-01,
        1.63000000e00,
        0.00000000e00,
        3.39000015e01,
        6.53999996e00,
        5.42999983e00,
        6.30000019e00,
        2.45001971e06,
        2.45248294e06,
    ]
]
cone_search_result1_2 = [
    "RA",
    "Dec",
    "SideProb",
    "Fpeak",
    "Fint",
    "rms",
    "Major",
    "Minor",
    "PosAng",
    "FitMajor",
    "FitMinor",
    "FitPosAng",
    "StartMJD",
    "StopMJD",
]
cone_search_result1_3 = [
    "rad",
    "rad",
    " ",
    "mJy",
    "mJy",
    "mJy",
    "arcsec",
    "arcsec",
    "deg",
    "arcsec",
    "arcsec",
    "deg",
    "MJD",
    "MJD",
]
service_cone_search_result1 = [
    {"attribute_name": "RA", "units": "deg", "values": [1.0161792162935126]},
    {"attribute_name": "Dec", "units": "deg", "values": [-0.011691666358208579]},
    {"attribute_name": "SideProb", "units": " ", "values": [0.014053001999855042]},
    {"attribute_name": "Fpeak", "units": "mJy", "values": [10.430000305175781]},
    {"attribute_name": "Fint", "units": "mJy", "values": [10.716876029968262]},
    {"attribute_name": "rms", "units": "mJy", "values": [0.10876674205064774]},
    {"attribute_name": "Major", "units": "arcsec", "values": [1.6299999952316284]},
    {"attribute_name": "Minor", "units": "arcsec", "values": [0.0]},
    {"attribute_name": "PosAng", "units": "deg", "values": [33.900001525878906]},
    {"attribute_name": "FitMajor", "units": "arcsec", "values": [6.539999961853027]},
    {"attribute_name": "FitMinor", "units": "arcsec", "values": [5.429999828338623]},
    {"attribute_name": "FitPosAng", "units": "deg", "values": [6.300000190734863]},
    {"attribute_name": "StartMJD", "units": "MJD", "values": [2450019.713368056]},
    {"attribute_name": "StopMJD", "units": "MJD", "values": [2452482.9428125005]},
]

# segundo caso del conesearch catalog = "First", ra = 0, dec = 0, radius = 0 (no encuentra coincidencias)

cone_search_result2_1 = []
cone_search_result2_2 = [
    "RA",
    "Dec",
    "SideProb",
    "Fpeak",
    "Fint",
    "rms",
    "Major",
    "Minor",
    "PosAng",
    "FitMajor",
    "FitMinor",
    "FitPosAng",
    "StartMJD",
    "StopMJD",
]
cone_search_result2_3 = [
    "rad",
    "rad",
    " ",
    "mJy",
    "mJy",
    "mJy",
    "arcsec",
    "arcsec",
    "deg",
    "arcsec",
    "arcsec",
    "deg",
    "MJD",
    "MJD",
]
service_cone_search_result2 = {}


# primer caso del conesearch_all ra = 1, dec = 0, radius = 200
service_cone_search_result1_1 = [
    {"attribute_name": "RA", "units": "deg", "values": []},
    {"attribute_name": "Dec", "units": "deg", "values": []},
    {"attribute_name": "r_K20e", "units": "arcsec", "values": []},
    {"attribute_name": "J_K20e", "units": "mag", "values": []},
    {"attribute_name": "e_J_K20e", "units": "mag", "values": []},
    {"attribute_name": "H_K20e", "units": "mag", "values": []},
    {"attribute_name": "e_H_K20e", "units": "mag", "values": []},
    {"attribute_name": "K_K20e", "units": "mag", "values": []},
    {"attribute_name": "e_K_K20e", "units": "mag", "values": []},
    {"attribute_name": "Jb_a", "units": " ", "values": []},
    {"attribute_name": "Jpa", "units": "deg", "values": []},
    {"attribute_name": "Hb_a", "units": " ", "values": []},
    {"attribute_name": "Hpa", "units": "deg", "values": []},
    {"attribute_name": "Kb_a", "units": " ", "values": []},
    {"attribute_name": "Kpa", "units": "deg", "values": []},
]
service_cone_search_result1_2 = [
    {"attribute_name": "RA", "units": "deg", "values": []},
    {"attribute_name": "Dec", "units": "deg", "values": []},
    {"attribute_name": "VarFlag", "units": " ", "values": []},
    {"attribute_name": "MaxMag", "units": "mag", "values": []},
    {"attribute_name": "MinMag", "units": "mag", "values": []},
    {"attribute_name": "Epoch", "units": "d", "values": []},
    {"attribute_name": "period", "units": "d", "values": []},
]
service_cone_search_result1_3 = [
    {"attribute_name": "RA_rad", "units": "deg", "values": []},
    {"attribute_name": "Dec_rad", "units": "deg", "values": []},
    {"attribute_name": "RA_arcsec", "units": "arcsec", "values": []},
    {"attribute_name": "Dec_arcsec", "units": "arcsec", "values": []},
    {"attribute_name": "r_K20e", "units": "deg", "values": []},
    {"attribute_name": "J_K20e", "units": "Jy", "values": []},
    {"attribute_name": "e_J_K20e", "units": "Jy", "values": []},
    {"attribute_name": "H_K20e", "units": "Jy", "values": []},
    {"attribute_name": "e_H_K20e", "units": "Jy", "values": []},
]
service_cone_search_result1_4 = {}
service_cone_search_result1_5 = [
    {"attribute_name": "RA", "units": "deg", "values": [1.0161792162935126]},
    {"attribute_name": "Dec", "units": "deg", "values": [-0.011691666358208579]},
    {"attribute_name": "SideProb", "units": " ", "values": [0.014053001999855042]},
    {"attribute_name": "Fpeak", "units": "mJy", "values": [10.430000305175781]},
    {"attribute_name": "Fint", "units": "mJy", "values": [10.716876029968262]},
    {"attribute_name": "rms", "units": "mJy", "values": [0.10876674205064774]},
    {"attribute_name": "Major", "units": "arcsec", "values": [1.6299999952316284]},
    {"attribute_name": "Minor", "units": "arcsec", "values": [0.0]},
    {"attribute_name": "PosAng", "units": "deg", "values": [33.900001525878906]},
    {"attribute_name": "FitMajor", "units": "arcsec", "values": [6.539999961853027]},
    {"attribute_name": "FitMinor", "units": "arcsec", "values": [5.429999828338623]},
    {"attribute_name": "FitPosAng", "units": "deg", "values": [6.300000190734863]},
    {"attribute_name": "StartMJD", "units": "MJD", "values": [2450019.713368056]},
    {"attribute_name": "StopMJD", "units": "MJD", "values": [2452482.9428125005]},
]
service_cone_search_result1_6 = [
    {"attribute_name": "RA", "units": "deg", "values": [1.0159166666666666]},
    {"attribute_name": "Dec", "units": "deg", "values": [-0.011666666666674423]},
    {"attribute_name": "errRA", "units": "deg", "values": [0.000541666655437425]},
    {"attribute_name": "errDec", "units": "deg", "values": [0.0006388888888888888]},
    {"attribute_name": "Flux", "units": "mJy", "values": [11.1]},
    {"attribute_name": "errFlux", "units": "mJy", "values": [1.0]},
    {"attribute_name": "MajorAxis", "units": "arcsec", "values": [35.8]},
    {"attribute_name": "MinorAxis", "units": "arcsec", "values": [-28.8]},
    {"attribute_name": "PA", "units": "deg", "values": [30.0]},
    {"attribute_name": "errMajorAxis", "units": "arcsec", "values": [6.9]},
    {"attribute_name": "errMinorAxis", "units": "arcsec", "values": [None]},
    {"attribute_name": "errPA", "units": "deg", "values": [30.0]},
]
service_cone_search_result1_7 = [
    {"attribute_name": "RA", "units": "deg", "values": []},
    {"attribute_name": "Dec", "units": "deg", "values": []},
    {"attribute_name": "errPosition", "units": "arcsec", "values": []},
    {"attribute_name": "CountRate", "units": "ct/s", "values": []},
    {"attribute_name": "errCountRate", "units": "ct/s", "values": []},
    {"attribute_name": "BackCountRate", "units": "ct s^-1 arcmin^-2", "values": []},
    {"attribute_name": "ExpTime", "units": "s", "values": []},
    {"attribute_name": "HardnessRatio1", "units": " ", "values": []},
    {"attribute_name": "errHardnessRatio1", "units": " ", "values": []},
    {"attribute_name": "HardnessRatio2", "units": " ", "values": []},
    {"attribute_name": "errHardnessRatio2", "units": " ", "values": []},
    {"attribute_name": "SourceExtentOverPSF", "units": "arcsec", "values": []},
    {"attribute_name": "LikelihoodExtent", "units": " ", "values": []},
    {"attribute_name": "LikelihoodDetection", "units": " ", "values": []},
    {"attribute_name": "ExtractionRadius", "units": "arcsec", "values": []},
    {"attribute_name": "PHAbestDetection", "units": " ", "values": []},
    {"attribute_name": "Vignetting", "units": " ", "values": []},
    {"attribute_name": "NumberCrossID", "units": " ", "values": []},
    {"attribute_name": "JD_startObs", "units": "day", "values": []},
    {"attribute_name": "JD_endObs", "units": "day", "values": []},
    {"attribute_name": "Reliability", "units": "%", "values": []},
]
service_cone_search_result1_8 = {}

service_cone_search_all_result1 = {
    "TMASSxsc": [
        {"attribute_name": "RA", "units": "deg", "values": []},
        {"attribute_name": "Dec", "units": "deg", "values": []},
        {"attribute_name": "r_K20e", "units": "arcsec", "values": []},
        {"attribute_name": "J_K20e", "units": "mag", "values": []},
        {"attribute_name": "e_J_K20e", "units": "mag", "values": []},
        {"attribute_name": "H_K20e", "units": "mag", "values": []},
        {"attribute_name": "e_H_K20e", "units": "mag", "values": []},
        {"attribute_name": "K_K20e", "units": "mag", "values": []},
        {"attribute_name": "e_K_K20e", "units": "mag", "values": []},
        {"attribute_name": "Jb_a", "units": " ", "values": []},
        {"attribute_name": "Jpa", "units": "deg", "values": []},
        {"attribute_name": "Hb_a", "units": " ", "values": []},
        {"attribute_name": "Hpa", "units": "deg", "values": []},
        {"attribute_name": "Kb_a", "units": " ", "values": []},
        {"attribute_name": "Kpa", "units": "deg", "values": []},
    ],
    "AAVSO_VSX": [
        {"attribute_name": "RA", "units": "deg", "values": []},
        {"attribute_name": "Dec", "units": "deg", "values": []},
        {"attribute_name": "VarFlag", "units": " ", "values": []},
        {"attribute_name": "MaxMag", "units": "mag", "values": []},
        {"attribute_name": "MinMag", "units": "mag", "values": []},
        {"attribute_name": "Epoch", "units": "d", "values": []},
        {"attribute_name": "period", "units": "d", "values": []},
    ],
    "AKARI": [
        {"attribute_name": "RA_rad", "units": "deg", "values": []},
        {"attribute_name": "Dec_rad", "units": "deg", "values": []},
        {"attribute_name": "RA_arcsec", "units": "arcsec", "values": []},
        {"attribute_name": "Dec_arcsec", "units": "arcsec", "values": []},
        {"attribute_name": "r_K20e", "units": "deg", "values": []},
        {"attribute_name": "J_K20e", "units": "Jy", "values": []},
        {"attribute_name": "e_J_K20e", "units": "Jy", "values": []},
        {"attribute_name": "H_K20e", "units": "Jy", "values": []},
        {"attribute_name": "e_H_K20e", "units": "Jy", "values": []},
    ],
    "FIRST": [
        {"attribute_name": "RA", "units": "deg", "values": [1.0161792162935126]},
        {"attribute_name": "Dec", "units": "deg", "values": [-0.011691666358208579]},
        {"attribute_name": "SideProb", "units": " ", "values": [0.014053001999855042]},
        {"attribute_name": "Fpeak", "units": "mJy", "values": [10.430000305175781]},
        {"attribute_name": "Fint", "units": "mJy", "values": [10.716876029968262]},
        {"attribute_name": "rms", "units": "mJy", "values": [0.10876674205064774]},
        {"attribute_name": "Major", "units": "arcsec", "values": [1.6299999952316284]},
        {"attribute_name": "Minor", "units": "arcsec", "values": [0.0]},
        {"attribute_name": "PosAng", "units": "deg", "values": [33.900001525878906]},
        {
            "attribute_name": "FitMajor",
            "units": "arcsec",
            "values": [6.539999961853027],
        },
        {
            "attribute_name": "FitMinor",
            "units": "arcsec",
            "values": [5.429999828338623],
        },
        {"attribute_name": "FitPosAng", "units": "deg", "values": [6.300000190734863]},
        {"attribute_name": "StartMJD", "units": "MJD", "values": [2450019.713368056]},
        {"attribute_name": "StopMJD", "units": "MJD", "values": [2452482.9428125005]},
    ],
    "NVSS": [
        {"attribute_name": "RA", "units": "deg", "values": [1.0159166666666666]},
        {"attribute_name": "Dec", "units": "deg", "values": [-0.011666666666674423]},
        {"attribute_name": "errRA", "units": "deg", "values": [0.000541666655437425]},
        {"attribute_name": "errDec", "units": "deg", "values": [0.0006388888888888888]},
        {"attribute_name": "Flux", "units": "mJy", "values": [11.1]},
        {"attribute_name": "errFlux", "units": "mJy", "values": [1.0]},
        {"attribute_name": "MajorAxis", "units": "arcsec", "values": [35.8]},
        {"attribute_name": "MinorAxis", "units": "arcsec", "values": [-28.8]},
        {"attribute_name": "PA", "units": "deg", "values": [30.0]},
        {"attribute_name": "errMajorAxis", "units": "arcsec", "values": [6.9]},
        {"attribute_name": "errMinorAxis", "units": "arcsec", "values": [None]},
        {"attribute_name": "errPA", "units": "deg", "values": [30.0]},
    ],
    "ROSATfsc": [
        {"attribute_name": "RA", "units": "deg", "values": []},
        {"attribute_name": "Dec", "units": "deg", "values": []},
        {"attribute_name": "errPosition", "units": "arcsec", "values": []},
        {"attribute_name": "CountRate", "units": "ct/s", "values": []},
        {"attribute_name": "errCountRate", "units": "ct/s", "values": []},
        {"attribute_name": "BackCountRate", "units": "ct s^-1 arcmin^-2", "values": []},
        {"attribute_name": "ExpTime", "units": "s", "values": []},
        {"attribute_name": "HardnessRatio1", "units": " ", "values": []},
        {"attribute_name": "errHardnessRatio1", "units": " ", "values": []},
        {"attribute_name": "HardnessRatio2", "units": " ", "values": []},
        {"attribute_name": "errHardnessRatio2", "units": " ", "values": []},
        {"attribute_name": "SourceExtentOverPSF", "units": "arcsec", "values": []},
        {"attribute_name": "LikelihoodExtent", "units": " ", "values": []},
        {"attribute_name": "LikelihoodDetection", "units": " ", "values": []},
        {"attribute_name": "ExtractionRadius", "units": "arcsec", "values": []},
        {"attribute_name": "PHAbestDetection", "units": " ", "values": []},
        {"attribute_name": "Vignetting", "units": " ", "values": []},
        {"attribute_name": "NumberCrossID", "units": " ", "values": []},
        {"attribute_name": "JD_startObs", "units": "day", "values": []},
        {"attribute_name": "JD_endObs", "units": "day", "values": []},
        {"attribute_name": "Reliability", "units": "%", "values": []},
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
        1.04300003e01,
        1.07168760e01,
        1.08766742e-01,
        1.63000000e00,
        0.00000000e00,
        3.39000015e01,
        6.53999996e00,
        5.42999983e00,
        6.30000019e00,
        2.45001971e06,
        2.45248294e06,
    ]
]
cross_match_result1_2 = [
    "RA",
    "Dec",
    "SideProb",
    "Fpeak",
    "Fint",
    "rms",
    "Major",
    "Minor",
    "PosAng",
    "FitMajor",
    "FitMinor",
    "FitPosAng",
    "StartMJD",
    "StopMJD",
]
cross_match_result1_3 = [
    "rad",
    "rad",
    " ",
    "mJy",
    "mJy",
    "mJy",
    "arcsec",
    "arcsec",
    "deg",
    "arcsec",
    "arcsec",
    "deg",
    "MJD",
    "MJD",
]

service_cross_match_result1 = [
    {"attribute_name": "RA", "value": 1.0161792162935126, "units": "deg"},
    {"attribute_name": "Dec", "value": -0.011691666358208579, "units": "deg"},
    {"attribute_name": "SideProb", "value": 0.014053001999855042, "units": " "},
    {"attribute_name": "Fpeak", "value": 10.430000305175781, "units": "mJy"},
    {"attribute_name": "Fint", "value": 10.716876029968262, "units": "mJy"},
    {"attribute_name": "rms", "value": 0.10876674205064774, "units": "mJy"},
    {"attribute_name": "Major", "value": 1.6299999952316284, "units": "arcsec"},
    {"attribute_name": "Minor", "value": 0.0, "units": "arcsec"},
    {"attribute_name": "PosAng", "value": 33.900001525878906, "units": "deg"},
    {"attribute_name": "FitMajor", "value": 6.539999961853027, "units": "arcsec"},
    {"attribute_name": "FitMinor", "value": 5.429999828338623, "units": "arcsec"},
    {"attribute_name": "FitPosAng", "value": 6.300000190734863, "units": "deg"},
    {"attribute_name": "StartMJD", "value": 2450019.713368056, "units": "MJD"},
    {"attribute_name": "StopMJD", "value": 2452482.9428125005, "units": "MJD"},
    {"attribute_name": "distance", "value": 71.86145556680134, "units": "arcsec"},
]

# segundo caso del crossmatch catalog = "FIRST", ra = 1, dec = 0, radius = 0(no entrega resultados)

cross_match_result2_1 = []
cross_match_result2_2 = [
    "RA",
    "Dec",
    "SideProb",
    "Fpeak",
    "Fint",
    "rms",
    "Major",
    "Minor",
    "PosAng",
    "FitMajor",
    "FitMinor",
    "FitPosAng",
    "StartMJD",
    "StopMJD",
]
cross_match_result2_3 = [
    "rad",
    "rad",
    " ",
    "mJy",
    "mJy",
    "mJy",
    "arcsec",
    "arcsec",
    "deg",
    "arcsec",
    "arcsec",
    "deg",
    "MJD",
    "MJD",
]
service_cross_match_result2 = {}


# tercer caso del crossmatch catalog = "FIRST", ra = 1, dec = 0 sin radius

cross_match_result3_1 = []
cross_match_result3_2 = [
    "RA",
    "Dec",
    "SideProb",
    "Fpeak",
    "Fint",
    "rms",
    "Major",
    "Minor",
    "PosAng",
    "FitMajor",
    "FitMinor",
    "FitPosAng",
    "StartMJD",
    "StopMJD",
]
cross_match_result3_3 = [
    "rad",
    "rad",
    " ",
    "mJy",
    "mJy",
    "mJy",
    "arcsec",
    "arcsec",
    "deg",
    "arcsec",
    "arcsec",
    "deg",
    "MJD",
    "MJD",
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
    {"attribute_name": "Fpeak", "value": 10.430000305175781, "units": "mJy"},
    {"attribute_name": "Fint", "value": 10.716876029968262, "units": "mJy"},
    {"attribute_name": "rms", "value": 0.10876674205064774, "units": "mJy"},
    {"attribute_name": "Major", "value": 1.6299999952316284, "units": "arcsec"},
    {"attribute_name": "Minor", "value": 0.0, "units": "arcsec"},
    {"attribute_name": "PosAng", "value": 33.900001525878906, "units": "deg"},
    {"attribute_name": "FitMajor", "value": 6.539999961853027, "units": "arcsec"},
    {"attribute_name": "FitMinor", "value": 5.429999828338623, "units": "arcsec"},
    {"attribute_name": "FitPosAng", "value": 6.300000190734863, "units": "deg"},
    {"attribute_name": "StartMJD", "value": 2450019.713368056, "units": "MJD"},
    {"attribute_name": "StopMJD", "value": 2452482.9428125005, "units": "MJD"},
    {"attribute_name": "distance", "value": 71.86145556680134, "units": "arcsec"},
]
service_cross_match_result1_6 = [
    {"attribute_name": "RA", "value": 1.0159166666666666, "units": "deg"},
    {"attribute_name": "Dec", "value": -0.011666666666674423, "units": "deg"},
    {"attribute_name": "errRA", "value": 0.000541666655437425, "units": "deg"},
    {"attribute_name": "errDec", "value": 0.0006388888888888888, "units": "deg"},
    {"attribute_name": "Flux", "value": 11.1, "units": "mJy"},
    {"attribute_name": "errFlux", "value": 1.0, "units": "mJy"},
    {"attribute_name": "MajorAxis", "value": 35.8, "units": "arcsec"},
    {"attribute_name": "MinorAxis", "value": -28.8, "units": "arcsec"},
    {"attribute_name": "PA", "value": 30.0, "units": "deg"},
    {"attribute_name": "errMajorAxis", "value": 6.9, "units": "arcsec"},
    {"attribute_name": "errMinorAxis", "value": None, "units": "arcsec"},
    {"attribute_name": "errPA", "value": 30.0, "units": "deg"},
    {"attribute_name": "distance", "value": 71.04428164620468, "units": "arcsec"},
]
service_cross_match_result1_7 = {}
service_cross_match_result1_8 = {}

service_cross_match_all_result1 = {
    "FIRST": [
        {"attribute_name": "RA", "value": 1.0161792162935126, "units": "deg"},
        {"attribute_name": "Dec", "value": -0.011691666358208579, "units": "deg"},
        {"attribute_name": "SideProb", "value": 0.014053001999855042, "units": " "},
        {"attribute_name": "Fpeak", "value": 10.430000305175781, "units": "mJy"},
        {"attribute_name": "Fint", "value": 10.716876029968262, "units": "mJy"},
        {"attribute_name": "rms", "value": 0.10876674205064774, "units": "mJy"},
        {"attribute_name": "Major", "value": 1.6299999952316284, "units": "arcsec"},
        {"attribute_name": "Minor", "value": 0.0, "units": "arcsec"},
        {"attribute_name": "PosAng", "value": 33.900001525878906, "units": "deg"},
        {"attribute_name": "FitMajor", "value": 6.539999961853027, "units": "arcsec"},
        {"attribute_name": "FitMinor", "value": 5.429999828338623, "units": "arcsec"},
        {"attribute_name": "FitPosAng", "value": 6.300000190734863, "units": "deg"},
        {"attribute_name": "StartMJD", "value": 2450019.713368056, "units": "MJD"},
        {"attribute_name": "StopMJD", "value": 2452482.9428125005, "units": "MJD"},
        {"attribute_name": "distance", "value": 71.86145556680134, "units": "arcsec"},
    ],
    "NVSS": [
        {"attribute_name": "RA", "value": 1.0159166666666666, "units": "deg"},
        {"attribute_name": "Dec", "value": -0.011666666666674423, "units": "deg"},
        {"attribute_name": "errRA", "value": 0.000541666655437425, "units": "deg"},
        {"attribute_name": "errDec", "value": 0.0006388888888888888, "units": "deg"},
        {"attribute_name": "Flux", "value": 11.1, "units": "mJy"},
        {"attribute_name": "errFlux", "value": 1.0, "units": "mJy"},
        {"attribute_name": "MajorAxis", "value": 35.8, "units": "arcsec"},
        {"attribute_name": "MinorAxis", "value": -28.8, "units": "arcsec"},
        {"attribute_name": "PA", "value": 30.0, "units": "deg"},
        {"attribute_name": "errMajorAxis", "value": 6.9, "units": "arcsec"},
        {"attribute_name": "errMinorAxis", "value": None, "units": "arcsec"},
        {"attribute_name": "errPA", "value": 30.0, "units": "deg"},
        {"attribute_name": "distance", "value": 71.04428164620468, "units": "arcsec"},
    ],
}
