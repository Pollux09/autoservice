from fastapi import APIRouter, Response, HTTPException, status, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from dependencies import SessionDep
from schemas.user import LoginAuthData


router = APIRouter(prefix="/auth", tags=["auth"])
templates = Jinja2Templates(directory="templates")


@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def login(session: SessionDep,
                response: Response,
                email: str = Form(...),
                password: str = Form(...),
                ):
    if email == "admin@admin.com":
        response.set_cookie("access_token", "admin_token", httponly=True, samesite="lax")
        return RedirectResponse(url="/dashboard", status_code=303)
    return "Неверный логин или пароль"
