from fastapi import APIRouter

from apis.version1 import (
    route_general_pages,
    route_users,
    route_jobs
)


api_router = APIRouter()
api_router.include_router(route_general_pages.genera_pages_router, prefix='', tags=['general_pages'])
api_router.include_router(route_users.router,prefix='/users', tags=['users'])
api_router.include_router(route_jobs.router, prefix='/jobs', tags=['jobs'])
