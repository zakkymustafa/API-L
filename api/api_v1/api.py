from fastapi import APIRouter
from api.api_v1.endpoints import people, user, login


api_router = APIRouter()

api_router.include_router(user.router, tags=["users"])
api_router.include_router(people.router, tags=["people"])
api_router.include_router(login.router, tags=["login"])

