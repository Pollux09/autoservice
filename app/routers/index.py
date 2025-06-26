from fastapi import APIRouter, Response, HTTPException, status, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from dependencies import SessionDep
from schemas.user import LoginAuthData


router = APIRouter(prefix="/dashboard",tags=["main"])
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
