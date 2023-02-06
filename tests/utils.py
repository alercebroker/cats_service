def round_cone_search(_list):
    for element in _list:
        element["values"] = [
            round(value, 2) for value in element["values"] if type(value) == float
        ]
    return _list


def round_cone_search_all(_dict):
    for _list in _dict.values():
        round_cone_search(_list)
    return _dict


def round_cross_match(_list):
    for element in _list:
        if type(element["value"]) == float:
            element["value"] = round(element["value"], 2)
    return _list


def round_cross_match_all(_dict):
    for _list in _dict.values():
        round_cross_match(_list)
    return _dict


def round_controller_conesearch(_list):
    round_cone_search(_list)
    return _list


def round_controller_crossmatch(_list):
    round_cross_match(_list)
    return _list
