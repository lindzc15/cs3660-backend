from fastapi import APIRouter, HTTPException

from schemas.login_schema import LoginRequest, LoginResponse, VerifyLoginRequest, RegisterResponse, RegisterRequest
from services.login_service import LoginService


router = APIRouter(prefix="/api/login", tags=["Authentication"])

@router.post("/", response_model=LoginResponse)
async def login(login: LoginRequest):
    try:
        token = LoginService.get_login_token(login.username, login.password)
        return LoginResponse(success=True, jwt_token=token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    

@router.post("/verify", response_model=LoginResponse)
async def verify(verify_request: VerifyLoginRequest):
    try:
        _ = LoginService.verify_token(verify_request.jwt_token)
        return LoginResponse(success=True, jwt_token=verify_request.jwt_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.post("/register", response_model=RegisterResponse)
async def register(register_request: RegisterRequest):
    try:
        _ = LoginService.hash_password(register_request.username, register_request.password, register_request.name)
        return RegisterResponse(success=True)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    