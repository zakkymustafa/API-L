from models.peoplemodel import PeopleModel, UpdatePeopleModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, status, HTTPException
from typing import List
from db.connect import db


router = APIRouter()


# CREATE
@router.post("/people", response_description = "Add a person to the database", response_model=PeopleModel)
async def create_people(people: PeopleModel = Body(...)):
    people = jsonable_encoder(people)
    # insert user into database
    new_people = await db["people"].insert_one(people)
    created_people = await db["people"].find_one({"_id":new_people.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_people)

# READ
@router.get(
    "/people", response_description="List of all people", response_model=List[PeopleModel]
    )
async def list_people():
    people = await db["people"].find().to_list(1000)
    return people

#READ EACH
@router.get("/people/{id}", response_description="Get information about one person", response_model=PeopleModel)
async def show_one_person(id: str):
    if (people := await db["people"].find_one({"_id":id})) is not None:
        return people
    raise HTTPException(status_code=404, detail=f'People {id} not found')


# DELETE
@router.delete("/people/{id}", response_description="Delete one person", response_model=PeopleModel)
async def delete_person(id: str):
    delete_result = await db["people"].delete_one({"_id":id})

    if delete_result.deleted_count == 1:
        JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    JSONResponse(status_code=status.HTTP_200_OK)

# UPDATE
@router.put("/people/{id}", response_description="Update people", response_model=PeopleModel)
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