from pydantic import BaseModel, Field, EmailStr




class UserModel(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)

    


class UserDatabaseModel(UserModel):
    password: str = Field(...)

    
