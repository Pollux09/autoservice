from fastapi import APIRouter, Response, HTTPException, status, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from crud.orders import create_order, get_orders
from dependencies import SessionDep
from crud.client import create_client, get_clients


router = APIRouter(prefix="/orders", tags=["orders"])
templates = Jinja2Templates(directory="templates")


@router.post("/create")
async def login(session: SessionDep,
                request: Request,
                car: str = Form(...),
                description: str = Form(...),
                price: int = Form(...),
                ):
    await create_order(car=car, description=description, price=price, session=session)
    orders = await get_orders(session=session)
    return templates.TemplateResponse("orders.html", {
        "request": request,
        "orders": orders,
    })
    

    