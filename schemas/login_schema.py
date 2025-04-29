from pydantic import BaseModel

# Define request model
class LoginRequest(BaseModel):
    username: str
    password: str

class VerifyLoginRequest(BaseModel):
    jwt_token: str

class LoginResponse(BaseModel):
    success: bool
    jwt_token: str|None = None

class RegisterResponse(BaseModel):
    success: bool

class RegisterRequest(BaseModel):
    username: str
    password: str
    name: str

class UpdateRequest(BaseModel):
    username: str
    name: str
    old_username: str