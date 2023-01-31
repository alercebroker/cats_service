def truncar (dic1):
    for key in dic1:
        dic1[key]["value"] = round(dic1[key]["value"],2)

    return dic1

def truncar_cone (dic1):
    for key in dic1:
        dic1[key]["values"] = round(dic1[key]["values"],2)

    return dic1

def truncar_all (dic1):
    for key in dic1:
        for key2 in dic1[key]:
            dic1[key][key2]["value"] = round(dic1[key][key2]["value"],2)