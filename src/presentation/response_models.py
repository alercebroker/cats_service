from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel, validator, ValidationError
from pydantic.generics import GenericModel

DataT = TypeVar('DataT')

class CrossMatchDataModel(BaseModel):
    value: int
    units: str

class CrossMatchContainerModel(BaseModel):
    attribute_name: CrossMatchDataModel

class CrossMatchModel(BaseModel):
    catalog_name: List[CrossMatchContainerModel]

class CrossMatchAllModel(BaseModel):
    catalogs: List[CrossMatchModel]

class ConeSearchDataModel(BaseModel):
    units: str
    values: List[int]

class ConeSearchContainerModel(GenericModel, Generic[DataT]):
    attribute_name: ConeSearchDataModel
    
class ConeSearchModel(BaseModel):
    catalog_name: ConeSearchContainerModel

class ConeSearchAllModel(BaseModel):
    catalogs: List[ConeSearchModel]