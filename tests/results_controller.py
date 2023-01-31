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

controller_conesearch_result1 = {
    "cat_name": "FIRST",
    "cat_fields": [
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
}
controller_conesearch_result2 = {"cat_name": "FIRST", "cat_fields": {}}


controller_crossmatch_result1 = {'cat_name': 'FIRST', 'cat_fields': [{'attribute_name': 'RA', 'value': 1.0161792162935126, 'units': 'deg'}, {'attribute_name': 'Dec', 'value': -0.011691666358208579, 'units': 'deg'}, {'attribute_name': 'SideProb', 'value': 0.014053001999855042, 'units': ' '}, {'attribute_name': 'Fpeak', 'value': 10.430000305175781, 'units': 'mJy'}, {'attribute_name': 'Fint', 'value': 10.716876029968262, 'units': 'mJy'}, {'attribute_name': 'rms', 'value': 0.10876674205064774, 'units': 'mJy'}, {'attribute_name': 'Major', 'value': 1.6299999952316284, 'units': 'arcsec'}, {'attribute_name': 'Minor', 'value': 0.0, 'units': 'arcsec'}, {'attribute_name': 'PosAng', 'value': 33.900001525878906, 'units': 'deg'}, {'attribute_name': 'FitMajor', 'value': 6.539999961853027, 'units': 'arcsec'}, {'attribute_name': 'FitMinor', 'value': 5.429999828338623, 'units': 'arcsec'}, {'attribute_name': 'FitPosAng', 'value': 6.300000190734863, 'units': 'deg'}, {'attribute_name': 'StartMJD', 'value': 2450019.713368056, 'units': 'MJD'}, {'attribute_name': 'StopMJD', 'value': 2452482.9428125005, 'units': 'MJD'}, {'attribute_name': 'distance', 'value': 71.86145556680134, 'units': 'arcsec'}]}
controller_crossmatch_result2 = {"cat_name": "FIRST", "cat_fields": {}}
controller_crossmatch_result3 = {"cat_name": "FIRST", "cat_fields": {}}


controller_conesearch_all_result1 = {
    "catalogs": [
        {
            "cat_name": "2MASSxsc",
            "cat_fields": [
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
        },
        {
            "cat_name": "AAVSO_VSX",
            "cat_fields": [
                {"attribute_name": "RA", "units": "deg", "values": []},
                {"attribute_name": "Dec", "units": "deg", "values": []},
                {"attribute_name": "VarFlag", "units": " ", "values": []},
                {"attribute_name": "MaxMag", "units": "mag", "values": []},
                {"attribute_name": "MinMag", "units": "mag", "values": []},
                {"attribute_name": "Epoch", "units": "d", "values": []},
                {"attribute_name": "period", "units": "d", "values": []},
            ],
        },
        {
            "cat_name": "AKARI",
            "cat_fields": [
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
        },
        {
            "cat_name": "FIRST",
            "cat_fields": [
                {
                    "attribute_name": "RA",
                    "units": "deg",
                    "values": [1.0161792162935126],
                },
                {
                    "attribute_name": "Dec",
                    "units": "deg",
                    "values": [-0.011691666358208579],
                },
                {
                    "attribute_name": "SideProb",
                    "units": " ",
                    "values": [0.014053001999855042],
                },
                {
                    "attribute_name": "Fpeak",
                    "units": "mJy",
                    "values": [10.430000305175781],
                },
                {
                    "attribute_name": "Fint",
                    "units": "mJy",
                    "values": [10.716876029968262],
                },
                {
                    "attribute_name": "rms",
                    "units": "mJy",
                    "values": [0.10876674205064774],
                },
                {
                    "attribute_name": "Major",
                    "units": "arcsec",
                    "values": [1.6299999952316284],
                },
                {"attribute_name": "Minor", "units": "arcsec", "values": [0.0]},
                {
                    "attribute_name": "PosAng",
                    "units": "deg",
                    "values": [33.900001525878906],
                },
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
                {
                    "attribute_name": "FitPosAng",
                    "units": "deg",
                    "values": [6.300000190734863],
                },
                {
                    "attribute_name": "StartMJD",
                    "units": "MJD",
                    "values": [2450019.713368056],
                },
                {
                    "attribute_name": "StopMJD",
                    "units": "MJD",
                    "values": [2452482.9428125005],
                },
            ],
        },
        {
            "cat_name": "NVSS",
            "cat_fields": [
                {
                    "attribute_name": "RA",
                    "units": "deg",
                    "values": [1.0159166666666666],
                },
                {
                    "attribute_name": "Dec",
                    "units": "deg",
                    "values": [-0.011666666666674423],
                },
                {
                    "attribute_name": "errRA",
                    "units": "deg",
                    "values": [0.000541666655437425],
                },
                {
                    "attribute_name": "errDec",
                    "units": "deg",
                    "values": [0.0006388888888888888],
                },
                {"attribute_name": "Flux", "units": "mJy", "values": [11.1]},
                {"attribute_name": "errFlux", "units": "mJy", "values": [1.0]},
                {"attribute_name": "MajorAxis", "units": "arcsec", "values": [35.8]},
                {"attribute_name": "MinorAxis", "units": "arcsec", "values": [-28.8]},
                {"attribute_name": "PA", "units": "deg", "values": [30.0]},
                {"attribute_name": "errMajorAxis", "units": "arcsec", "values": [6.9]},
                {"attribute_name": "errMinorAxis", "units": "arcsec", "values": [None]},
                {"attribute_name": "errPA", "units": "deg", "values": [30.0]},
            ],
        },
        {
            "cat_name": "ROSATfsc",
            "cat_fields": [
                {"attribute_name": "RA", "units": "deg", "values": []},
                {"attribute_name": "Dec", "units": "deg", "values": []},
                {"attribute_name": "errPosition", "units": "arcsec", "values": []},
                {"attribute_name": "CountRate", "units": "ct/s", "values": []},
                {"attribute_name": "errCountRate", "units": "ct/s", "values": []},
                {
                    "attribute_name": "BackCountRate",
                    "units": "ct s^-1 arcmin^-2",
                    "values": [],
                },
                {"attribute_name": "ExpTime", "units": "s", "values": []},
                {"attribute_name": "HardnessRatio1", "units": " ", "values": []},
                {"attribute_name": "errHardnessRatio1", "units": " ", "values": []},
                {"attribute_name": "HardnessRatio2", "units": " ", "values": []},
                {"attribute_name": "errHardnessRatio2", "units": " ", "values": []},
                {
                    "attribute_name": "SourceExtentOverPSF",
                    "units": "arcsec",
                    "values": [],
                },
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
        },
    ]
}
controller_conesearch_all_result2 = {"catalogs": []}


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
