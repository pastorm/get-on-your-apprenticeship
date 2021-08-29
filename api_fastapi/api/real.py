from fastapi import APIRouter
from fastapi.responses import PlainTextResponse, JSONResponse

import requests

from settings import settings


router = APIRouter(prefix="/real", tags=["real"])


@router.get("/")
async def real():
    return PlainTextResponse("This is a dummy route")


@router.get("/student")
async def get_student():
    return PlainTextResponse("Harry Potter !")


@router.get("/students")
async def list():
    response = requests.get(settings['ENDPOINT_CHARACTERS_LIST'])
    response.raise_for_status()

    return JSONResponse(response.json())
