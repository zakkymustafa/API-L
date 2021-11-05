from pydantic import BaseModel
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, List
from .common import PyObjectId




# CREATE MODEL
class PeopleModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    survived: bool = Field(...)
    passengerClass: int = Field(...) 
    name: str = Field(...)
    sex: str = Field(...)
    age: int = Field(...)
    siblingsOrSpousesAboard: int = Field(...)
    parentsOrChildrenAboard: int = Field(...)
    fare: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
                "example": {
                    "survived": True,
                    "passengerClass": 3,
                    "name": "Mr. Owen Harris Braund",
                    "sex": "male",
                    "age": 25,
                    "siblingsOrSpousesAboard": 1,
                    "parentsOrChildrenAboard": 0,
                    "fare": 7.25,
                }

        }


#UPDATEMODEL
class UpdatePeopleModel(BaseModel):
    survived: Optional[bool]
    passengerClass: Optional[int]
    name: Optional[str]
    sex: Optional[str]
    age: Optional[int]
    siblingsOrSpousesAboard: Optional[int]
    parentsOrChildrenAboard: Optional[int]
    fare: Optional[int]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "survived": True,
                "passengerClass": 3,
                "name": "Mr. Owen Harris Braund",
                "sex": "male",
                "age": 25,
                "siblingsOrSpousesAboard": 1,
                "parentsOrChildrenAboard": 0,
                "fare": 7.25,
            }
        }
