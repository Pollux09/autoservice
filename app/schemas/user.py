from pydantic import BaseModel, EmailStr


class LoginAuthData(BaseModel):
    email: EmailStr
    password: str