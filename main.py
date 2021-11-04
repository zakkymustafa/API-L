
from models.usermodel import UserModel
import os
from fastapi import FastAPI, Body, status, HTTPException
from models.peoplemodel import PeopleModel, UpdatePeopleModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import  List
import motor.motor_asyncio
from dotenv import load_dotenv
from api.api_v1.api import api_router

load_dotenv()

# connect to MONGODB database
app = FastAPI()
#create mongodb client
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
#connect to database
db = client.limadb


    


app.include_router(api_router, prefix="/v1")