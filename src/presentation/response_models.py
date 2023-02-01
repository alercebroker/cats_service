from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel, validator, ValidationError
from pydantic.generics import GenericModel

DataT = TypeVar('DataT')

class CrossMatchFieldsModel(GenericModel, Generic[DataT]):
    attribute_name: str
    value: int
    units: str

class CrossMatchModel(BaseModel):
    catalog_name: str
    catalog_fields: List[CrossMatchFieldsModel]

class ConeSearchFieldsModel(GenericModel, Generic[DataT]):
    attribute_name: str
    units: str
    values: List[float]
    
class ConeSearchModel(BaseModel):
    catalog_name: str
    catalog_fields: List[ConeSearchFieldsModel]