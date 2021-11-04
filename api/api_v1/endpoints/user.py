from fastapi import APIRouter
from models.usermodel import UserModel



router = APIRouter()

@router.get("/users/{id}", response_description="View user information", response_model=UserModel)
async def get_users(id: str):
    users = await db["users"].find_one({"_id":id})
    return users