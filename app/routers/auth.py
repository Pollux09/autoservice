from fastapi import APIRouter, Response, Cookie

# from deps import SessionDep, CurrentUser, RefreshTokenDep, AuthServiceDep
# from models.schemas.auth import LoginAuthData, SignupAuthData

router = APIRouter(prefix="/auth", tags=["auth"])