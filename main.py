
from models.usermodel import UserModel
import os
from fastapi import FastAPI, Body, status, HTTPException
from models.peoplemodel import PeopleModel, UpdatePeopleModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import  List
from dotenv import load_dotenv
from api.api_v1.api import api_router

load_dotenv()

app = FastAPI()

app.include_router(api_router, prefix="/v1")
