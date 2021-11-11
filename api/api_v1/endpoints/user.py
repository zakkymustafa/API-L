from fastapi import APIRouter, Body, status
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from models.usermodel import UserModel, UserCreate
from db.connect import db
from api.deps import UserAuthHandler


router = APIRouter()
userauth_handler = UserAuthHandler()
users = []

@router.get("/users/{id}", response_description="View user information", response_model=UserModel)
async def get_users(id: str):
    users = await db["users"].find_one({"_id":id})
    return users

@router.post("/users", response_description="create user", response_model=UserCreate)
async def create_users(user_create: UserCreate = Body(...)):
    if any(x["username"] == user_create.username for x in users):
        raise HTTPException(status_code=400, detail="Username is taken")
    hashed_password = userauth_handler.get_password_hash(user_create.password)
    users.append({
        "username": user_create.username,
        "email": user_create.email,
        "password": hashed_password
    })
    return JSONResponse(status_code=201)



