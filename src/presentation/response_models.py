from pydantic import BaseModel, create_model
import os


class CrossMatchModel(BaseModel):
    attribute_name: str
    unit: str
    value: float | str | None


class ConeSearchModel(BaseModel):
    attribute_name: str
    unit: str
    values: list[float | str | None]


catalogs = os.environ["CATALOGS"].split(",")

conesearch_catalogs_attributes = {}
crossmatch_catalogs_attributes = {}

for catalog in catalogs:
    conesearch_catalogs_attributes[catalog] = (list[ConeSearchModel], None)
    crossmatch_catalogs_attributes[catalog] = (list[CrossMatchModel], None)

ConeSearchAllModel = create_model(
    "ConeSearchAllModel", **conesearch_catalogs_attributes
)
CrossMatchAllModel = create_model(
    "CrossMatchAllModel", **crossmatch_catalogs_attributes
)
