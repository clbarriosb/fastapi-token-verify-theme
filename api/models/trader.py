from pydantic import BaseModel

class TraderCreate(BaseModel):
    name: str
    password: str
    email: str
    role : str = "trader"

class Trader(BaseModel):
    name: str
    password: str
    email: str
    role : str = "trader"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "john_doe@gmail.com",
                "name": "john_doe",
                "password": "securepassword123",
                "role": "trader"
            }
        } 