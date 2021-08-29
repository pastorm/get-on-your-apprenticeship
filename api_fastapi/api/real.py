import random

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse, JSONResponse

import requests

from settings import settings


router = APIRouter(prefix="/real", tags=["real"])


#
# TOOLS
#
async def get_students() -> list:
    response = requests.get(settings["ENDPOINT_CHARACTERS_LIST"])
    response.raise_for_status()

    return response.json()


#
# ENDPOINTS
#
@router.get("/")
async def real():
    return PlainTextResponse("This is a dummy route")


@router.get("/student")
async def get_student():
    return PlainTextResponse("Harry Potter !")


@router.get("/students")
async def list():
    return JSONResponse(get_student())


@router.get("/random_student")
async def random_student():
    students: list = await get_students()
    choosen_one = random.choice(students)

    return JSONResponse(choosen_one)
