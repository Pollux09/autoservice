from fastapi import APIRouter, Response, HTTPException, status, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from dependencies import SessionDep
from schemas.user import LoginAuthData
from crud.spare_part import *


router = APIRouter(prefix="/warehouse", tags=["warehouse"])
templates = Jinja2Templates(directory="templates")





@router.post("/create")
async def add_spare_part(session: SessionDep,
                request: Request,
                title: str = Form(...),
                category: str = Form(...),
                price: str = Form(...),
                count: int = Form(...)
                ):
    
    await create_spare_part(title=title, category=category, price=price, count=count, session=session)
    spare_parts = await get_spare_parts(session=session)
    return templates.TemplateResponse("warehouse.html", {
        "request": request,
        "spare_parts": spare_parts,
    })
    

    