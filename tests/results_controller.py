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

controller_conesearch_result1 = [
    {"attribute_name": "RA", "unit": "deg", "values": [1.0161792162935126]},
    {"attribute_name": "Dec", "unit": "deg", "values": [-0.011691666358208579]},
    {"attribute_name": "SideProb", "unit": " ", "values": [0.014053001999855042]},
]

controller_conesearch_result2 = []


controller_crossmatch_result1 = {
    "cat_name": "FIRST",
    "cat_fields": [
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
}
controller_crossmatch_result2 = {"cat_name": "FIRST", "cat_fields": {}}
controller_crossmatch_result3 = {"cat_name": "FIRST", "cat_fields": {}}


controller_conesearch_all_result1 = {
    "TMASSxsc": [],
    "AAVSO_VSX": [],
    "AKARI": [],
    "CRTS_per_var": [],
    "FIRST": [
        {"attribute_name": "RA", "unit": "deg", "values": [1.0161792162935126]},
        {"attribute_name": "Dec", "unit": "deg", "values": [-0.011691666358208579]},
        {"attribute_name": "SideProb", "unit": " ", "values": [0.014053001999855042]},
    ],
    "NVSS": [
        {"attribute_name": "RA", "unit": "deg", "values": [1.0159166666666666]},
        {"attribute_name": "Dec", "unit": "deg", "values": [-0.011666666666674423]},
        {"attribute_name": "errRA", "unit": "deg", "values": [0.000541666655437425]},
    ],
    "ROSATfsc": [],
    "SWIREz": [],
}


controller_conesearch_all_result2 = {
    "TMASSxsc": [],
    "AAVSO_VSX": [],
    "AKARI": [],
    "CRTS_per_var": [],
    "FIRST": [],
    "NVSS": [],
    "ROSATfsc": [],
    "SWIREz": [],
}


controller_crossmatch_all_result1 = {
    "catalogs": [
        {
            "cat_name": "FIRST",
            "cat_fields": [
                {
                    "attribute_name": "distance",
                    "value": 71.86145556680134,
                    "units": "arcsec",
                }
            ],
        },
        {
            "cat_name": "NVSS",
            "cat_fields": [
                {
                    "attribute_name": "distance",
                    "value": 71.04428164620468,
                    "units": "arcsec",
                }
            ],
        },
    ]
}
controller_crossmatch_all_result2 = {"catalogs": []}
controller_crossmatch_all_result3 = {"catalogs": []}
