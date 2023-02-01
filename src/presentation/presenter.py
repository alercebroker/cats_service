from fastapi.encoders import jsonable_encoder


def json(final_result):
    return jsonable_encoder(final_result)



    