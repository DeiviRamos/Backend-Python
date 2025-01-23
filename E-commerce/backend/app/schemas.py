from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    username: str
    password: str
    
class Token(BaseModel):
    acces_token: str
    token_type: str
    
class LoginRequest(BaseModel):
    username: str
    password: str