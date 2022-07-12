from fastapi import APIRouter
from blog import blog

routers = APIRouter()
routers.include_router(blog.router, prefix='/blog')
