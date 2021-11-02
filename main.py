
import os
from fastapi import FastAPI, Body, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio


# connect to MONGODB database
app = FastAPI()
#create mongodb client
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
#connect to database
db = client.limadb


# ID convert to String
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


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



# CREATE
@app.post("/people", response_description = "Add a person to the database", response_model=PeopleModel)
async def create_people(people: PeopleModel = Body(...)):
    people = jsonable_encoder(people)
    # insert user into database
    new_people = await db["people"].insert_one(people)
    created_people = await db["people"].find_one({"_id":new_people.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_people)

# READ
@app.get(
    "/people", response_description="List of all people", response_model=List[PeopleModel]
    )
async def list_people():
    people = await db["people"].find().to_list(1000)
    return people

#READ EACH
@app.get("/people/{id}", response_description="Get information about one person", response_model=PeopleModel)
async def show_one_person(id: str):
    if (people := await db["people"].find_one({"_id":id})) is not None:
        return people
    raise HTTPException(status_code=404, detail=f'People {id} not found')

# DELETE
@app.delete("/people/{id}", response_description="Delete one person", response_model=PeopleModel)
async def delete_person(id: str):
    delete_result = await db["people"].delete_one({"_id":id})

    if delete_result.deleted_count == 1:
        JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    JSONResponse(status_code=status.HTTP_200_OK)

# UPDATE
@app.put("/people/{id}", response_description="Update people", response_model=PeopleModel)
async def update_one_person(id: str, people:UpdatePeopleModel = Body(...)):
    #Iterate through the items in the people dictionary 
    people = {p: v for p, v in people.dict().items() if v is not None}

    if len(people) >= 1:
        update_result = await db["people"].update_one({"_id":id}, {"$set": people})

        if update_result.modified_count == 1:
            if (updated_people := await db['people'].find_one({"_id":id}))is not None:
                return updated_people


    if (existing_student := await db["people"].find_one({"_id": id})) is not None:
        return existing_student


    raise HTTPException(status_code=404, detail=f'people {id} not found')