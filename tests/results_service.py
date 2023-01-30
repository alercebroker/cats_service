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
csr1_1 = [
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
csr1_2 = [
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
csr1_3 = [
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
scsr1 = {
    "RA": {"units": "deg", "values": [1.016179215453705]},
    "Dec": {"units": "deg", "values": [-0.011691666358472456]},
    "SideProb": {"units": " ", "values": [0.014053002]},
    "Fpeak": {"units": "mJy", "values": [10.4300003]},
    "Fint": {"units": "mJy", "values": [10.716876]},
    "rms": {"units": "mJy", "values": [0.108766742]},
    "Major": {"units": "arcsec", "values": [1.63]},
    "Minor": {"units": "arcsec", "values": [0.0]},
    "PosAng": {"units": "deg", "values": [33.9000015]},
    "FitMajor": {"units": "arcsec", "values": [6.53999996]},
    "FitMinor": {"units": "arcsec", "values": [5.42999983]},
    "FitPosAng": {"units": "deg", "values": [6.30000019]},
    "StartMJD": {"units": "MJD", "values": [2450019.71]},
    "StopMJD": {"units": "MJD", "values": [2452482.94]},
}

# segundo caso del conesearch catalog = "First", ra = 0, dec = 0, radius = 0 (no encuentra coincidencias)

csr2_1 = []
csr2_2 = [
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
csr2_3 = [
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
scsr2 = {}


# esto es lo que da el test y por eso da error


# primer caso del conesearch_all ra = 1, dec = 0, radius = 200
scsr1_1 = {
    "RA": {"units": "deg", "values": []},
    "Dec": {"units": "deg", "values": []},
    "r_K20e": {"units": "arcsec", "values": []},
    "J_K20e": {"units": "mag", "values": []},
    "e_J_K20e": {"units": "mag", "values": []},
    "H_K20e": {"units": "mag", "values": []},
    "e_H_K20e": {"units": "mag", "values": []},
    "K_K20e": {"units": "mag", "values": []},
    "e_K_K20e": {"units": "mag", "values": []},
    "Jb_a": {"units": " ", "values": []},
    "Jpa": {"units": "deg", "values": []},
    "Hb_a": {"units": " ", "values": []},
    "Hpa": {"units": "deg", "values": []},
    "Kb_a": {"units": " ", "values": []},
    "Kpa": {"units": "deg", "values": []},
}
scsr1_2 = {
    "RA": {"units": "deg", "values": []},
    "Dec": {"units": "deg", "values": []},
    "VarFlag": {"units": " ", "values": []},
    "MaxMag": {"units": "mag", "values": []},
    "MinMag": {"units": "mag", "values": []},
    "Epoch": {"units": "d", "values": []},
    "period": {"units": "d", "values": []},
}
scsr1_3 = {
    "RA_rad": {"units": "deg", "values": []},
    "Dec_rad": {"units": "deg", "values": []},
    "RA_arcsec": {"units": "arcsec", "values": []},
    "Dec_arcsec": {"units": "arcsec", "values": []},
    "r_K20e": {"units": "deg", "values": []},
    "J_K20e": {"units": "Jy", "values": []},
    "e_J_K20e": {"units": "Jy", "values": []},
    "H_K20e": {"units": "Jy", "values": []},
    "e_H_K20e": {"units": "Jy", "values": []},
}
scsr1_4 = {}
scsr1_5 = {
    "RA": {"units": "deg", "values": [1.0161792162935126]},
    "Dec": {"units": "deg", "values": [-0.011691666358208579]},
    "SideProb": {"units": " ", "values": [0.014053001999855042]},
    "Fpeak": {"units": "mJy", "values": [10.430000305175781]},
    "Fint": {"units": "mJy", "values": [10.716876029968262]},
    "rms": {"units": "mJy", "values": [0.10876674205064774]},
    "Major": {"units": "arcsec", "values": [1.6299999952316284]},
    "Minor": {"units": "arcsec", "values": [0.0]},
    "PosAng": {"units": "deg", "values": [33.900001525878906]},
    "FitMajor": {"units": "arcsec", "values": [6.539999961853027]},
    "FitMinor": {"units": "arcsec", "values": [5.429999828338623]},
    "FitPosAng": {"units": "deg", "values": [6.300000190734863]},
    "StartMJD": {"units": "MJD", "values": [2450019.713368056]},
    "StopMJD": {"units": "MJD", "values": [2452482.9428125005]},
}
scsr1_6 = {
    "RA": {"units": "deg", "values": [1.0159166666666666]},
    "Dec": {"units": "deg", "values": [-0.011666666666674423]},
    "errRA": {"units": "deg", "values": [0.000541666655437425]},
    "errDec": {"units": "deg", "values": [0.0006388888888888888]},
    "Flux": {"units": "mJy", "values": [11.1]},
    "errFlux": {"units": "mJy", "values": [1.0]},
    "MajorAxis": {"units": "arcsec", "values": [35.8]},
    "MinorAxis": {"units": "arcsec", "values": [-28.8]},
    "PA": {"units": "deg", "values": [30.0]},
    "errMajorAxis": {"units": "arcsec", "values": [6.9]},
    "errMinorAxis": {"units": "arcsec", "values": [None]},
    "errPA": {"units": "deg", "values": [30.0]},
}
scsr1_7 = {
    "RA": {"units": "deg", "values": []},
    "Dec": {"units": "deg", "values": []},
    "errPosition": {"units": "arcsec", "values": []},
    "CountRate": {"units": "ct/s", "values": []},
    "errCountRate": {"units": "ct/s", "values": []},
    "BackCountRate": {"units": "ct s^-1 arcmin^-2", "values": []},
    "ExpTime": {"units": "s", "values": []},
    "HardnessRatio1": {"units": " ", "values": []},
    "errHardnessRatio1": {"units": " ", "values": []},
    "HardnessRatio2": {"units": " ", "values": []},
    "errHardnessRatio2": {"units": " ", "values": []},
    "SourceExtentOverPSF": {"units": "arcsec", "values": []},
    "LikelihoodExtent": {"units": " ", "values": []},
    "LikelihoodDetection": {"units": " ", "values": []},
    "ExtractionRadius": {"units": "arcsec", "values": []},
    "PHAbestDetection": {"units": " ", "values": []},
    "Vignetting": {"units": " ", "values": []},
    "NumberCrossID": {"units": " ", "values": []},
    "JD_startObs": {"units": "day", "values": []},
    "JD_endObs": {"units": "day", "values": []},
    "Reliability": {"units": "%", "values": []},
}
scsr1_8 = {}

scsar1 = {
    "TMASSxsc": [
        {
            "RA": {"units": "deg", "values": []},
            "Dec": {"units": "deg", "values": []},
            "r_K20e": {"units": "arcsec", "values": []},
            "J_K20e": {"units": "mag", "values": []},
            "e_J_K20e": {"units": "mag", "values": []},
            "H_K20e": {"units": "mag", "values": []},
            "e_H_K20e": {"units": "mag", "values": []},
            "K_K20e": {"units": "mag", "values": []},
            "e_K_K20e": {"units": "mag", "values": []},
            "Jb_a": {"units": " ", "values": []},
            "Jpa": {"units": "deg", "values": []},
            "Hb_a": {"units": " ", "values": []},
            "Hpa": {"units": "deg", "values": []},
            "Kb_a": {"units": " ", "values": []},
            "Kpa": {"units": "deg", "values": []},
        }
    ],
    "AAVSO_VSX": [
        {
            "RA": {"units": "deg", "values": []},
            "Dec": {"units": "deg", "values": []},
            "VarFlag": {"units": " ", "values": []},
            "MaxMag": {"units": "mag", "values": []},
            "MinMag": {"units": "mag", "values": []},
            "Epoch": {"units": "d", "values": []},
            "period": {"units": "d", "values": []},
        }
    ],
    "AKARI": [
        {
            "RA_rad": {"units": "deg", "values": []},
            "Dec_rad": {"units": "deg", "values": []},
            "RA_arcsec": {"units": "arcsec", "values": []},
            "Dec_arcsec": {"units": "arcsec", "values": []},
            "r_K20e": {"units": "deg", "values": []},
            "J_K20e": {"units": "Jy", "values": []},
            "e_J_K20e": {"units": "Jy", "values": []},
            "H_K20e": {"units": "Jy", "values": []},
            "e_H_K20e": {"units": "Jy", "values": []},
        }
    ],
    "CRTS_per_var": [],
    "FIRST": [
        {
            "RA": {"units": "deg", "values": [1.0161792162935126]},
            "Dec": {"units": "deg", "values": [-0.011691666358208579]},
            "SideProb": {"units": " ", "values": [0.014053001999855042]},
            "Fpeak": {"units": "mJy", "values": [10.430000305175781]},
            "Fint": {"units": "mJy", "values": [10.716876029968262]},
            "rms": {"units": "mJy", "values": [0.10876674205064774]},
            "Major": {"units": "arcsec", "values": [1.6299999952316284]},
            "Minor": {"units": "arcsec", "values": [0.0]},
            "PosAng": {"units": "deg", "values": [33.900001525878906]},
            "FitMajor": {"units": "arcsec", "values": [6.539999961853027]},
            "FitMinor": {"units": "arcsec", "values": [5.429999828338623]},
            "FitPosAng": {"units": "deg", "values": [6.300000190734863]},
            "StartMJD": {"units": "MJD", "values": [2450019.713368056]},
            "StopMJD": {"units": "MJD", "values": [2452482.9428125005]},
        }
    ],
    "NVSS": [
        {
            "RA": {"units": "deg", "values": [1.0159166666666666]},
            "Dec": {"units": "deg", "values": [-0.011666666666674423]},
            "errRA": {"units": "deg", "values": [0.000541666655437425]},
            "errDec": {"units": "deg", "values": [0.0006388888888888888]},
            "Flux": {"units": "mJy", "values": [11.1]},
            "errFlux": {"units": "mJy", "values": [1.0]},
            "MajorAxis": {"units": "arcsec", "values": [35.8]},
            "MinorAxis": {"units": "arcsec", "values": [-28.8]},
            "PA": {"units": "deg", "values": [30.0]},
            "errMajorAxis": {"units": "arcsec", "values": [6.9]},
            "errMinorAxis": {"units": "arcsec", "values": [None]},
            "errPA": {"units": "deg", "values": [30.0]},
        }
    ],
    "ROSATfsc": [
        {
            "RA": {"units": "deg", "values": []},
            "Dec": {"units": "deg", "values": []},
            "errPosition": {"units": "arcsec", "values": []},
            "CountRate": {"units": "ct/s", "values": []},
            "errCountRate": {"units": "ct/s", "values": []},
            "BackCountRate": {"units": "ct s^-1 arcmin^-2", "values": []},
            "ExpTime": {"units": "s", "values": []},
            "HardnessRatio1": {"units": " ", "values": []},
            "errHardnessRatio1": {"units": " ", "values": []},
            "HardnessRatio2": {"units": " ", "values": []},
            "errHardnessRatio2": {"units": " ", "values": []},
            "SourceExtentOverPSF": {"units": "arcsec", "values": []},
            "LikelihoodExtent": {"units": " ", "values": []},
            "LikelihoodDetection": {"units": " ", "values": []},
            "ExtractionRadius": {"units": "arcsec", "values": []},
            "PHAbestDetection": {"units": " ", "values": []},
            "Vignetting": {"units": " ", "values": []},
            "NumberCrossID": {"units": " ", "values": []},
            "JD_startObs": {"units": "day", "values": []},
            "JD_endObs": {"units": "day", "values": []},
            "Reliability": {"units": "%", "values": []},
        }
    ],
    "SWIREz": [],
}

# segundo caso del conesearch_all ra = 0, dec = 0, radius = 0 (catalogos vacios, este caso engloba numeros negativos o 0)

scsr2_1 = {}
scsr2_2 = {}
scsr2_3 = {}
scsr2_4 = {}
scsr2_5 = {}
scsr2_6 = {}
scsr2_7 = {}
scsr2_8 = {}

scsar2 = {
    "TMASSxsc": [],
    "AAVSO_VSX": [],
    "AKARI": [],
    "CRTS_per_var": [],
    "FIRST": [],
    "NVSS": [],
    "ROSATfsc": [],
    "SWIREz": [],
}


# primer caso del crossmatch_all ra = 0, dec = 0, radius = 200, catalog = FIRST (entrega resultados)
