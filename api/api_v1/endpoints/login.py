from fastapi.exceptions import HTTPException
from api.deps import UserAuthHandler
from models.usermodel import UserCreate
from fastapi import APIRouter
from models.tokenmodel import Token



router = APIRouter()
authuser_handler=UserAuthHandler()
users = []



@router.post("/", response_model=Token)
async def login_access_token():
    pass


@router.post("/login")
async def login(user_create: UserCreate):
    user = None

    for x in users:
        if x["username"] == user_create.username:
            user = x
            break

    if (user is None) or (not authuser_handler.verify_password(user_create.password, user["password"])):
        raise HTTPException(status_code=401, detail="Invalid username and/or password")
    token = authuser_handler.encode_token(user["username"])
    return {"token": token}

