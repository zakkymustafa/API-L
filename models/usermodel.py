from pydantic import BaseModel, Field, EmailStr
from typing import Optional




class UserModel(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)

#for account creation
class UserCreate(UserModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


#for update
class UserUpdate(UserModel):
    password: Optional[str] 

class UserDatabaseModel(UserModel):
    hashed_password: str = Field(...)

    
