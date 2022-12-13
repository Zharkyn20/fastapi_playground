from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
genera_pages_router = APIRouter()


@genera_pages_router.get('/')
async def home(request: Request):
    return templates.TemplateResponse('general_pages/homepage.html',{'request': request})
