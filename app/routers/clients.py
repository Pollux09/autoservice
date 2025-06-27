from fastapi import APIRouter, Response, HTTPException, status, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from dependencies import SessionDep
from schemas.user import LoginAuthData
from crud.client import create_client, get_clients


router = APIRouter(prefix="/clients", tags=["clients"])
templates = Jinja2Templates(directory="templates")


@router.post("/create")
async def login(session: SessionDep,
                request: Request,
                email: str = Form(...),
                fullname: str = Form(...),
                phone: str = Form(...),
                car: str = Form(...)
                ):
    await create_client(email=email, fullname=fullname, phone=phone, car=car, session=session)
    clients = await get_clients(session=session)
    return templates.TemplateResponse("clients.html", {
        "request": request,
        "clients": clients,
    })
    

    