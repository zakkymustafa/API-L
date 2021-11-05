from fastapi import FastAPI
from dotenv import load_dotenv
from api.api_v1.api import api_router

load_dotenv()

app = FastAPI()



app.include_router(api_router, prefix="/v1")
