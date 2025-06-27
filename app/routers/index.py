from fastapi import APIRouter, Response, HTTPException, status, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from crud.dashboard import get_active_orders_count
from crud.orders import get_orders
from crud.spare_part import get_spare_parts
from dependencies import SessionDep
from schemas.user import LoginAuthData
from crud.client import *


router = APIRouter(tags=["main"])
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def dashboard_page(request: Request, session: SessionDep):    
    active_orders_count = await get_active_orders_count(session=session)
    
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "active_orders_count": active_orders_count,
    })

@router.get('/orders')
async def orders_page(request: Request, session: SessionDep):
    orders = await get_orders(session=session)
    return templates.TemplateResponse("orders.html", {
        "request": request,
        "orders": orders
    })

@router.get('/clients')
async def orders_page(request: Request, session: SessionDep):
    clients = await get_clients(session=session)
    return templates.TemplateResponse("clients.html", {
        "request": request,
        "clients": clients,
    })

@router.get('/warehouse')
async def warehouse_page(request: Request, session: SessionDep):
    spare_parts = await get_spare_parts(session=session)
    return templates.TemplateResponse("warehouse.html", {
        "request": request,
        "spare_parts": spare_parts,
    })
