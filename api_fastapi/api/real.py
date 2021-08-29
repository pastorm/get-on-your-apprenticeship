import random
from typing import Optional

from fastapi import APIRouter, Query
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
async def students_list(house: Optional[str] = Query(None, enum=settings["STUDENT_HOUSE_CHOICES"])):
    students = await get_students()

    if house:
        students = list(filter(lambda student: student['house'] == house, students))

    return JSONResponse(students)


@router.get("/random_student")
async def random_student():
    students: list = await get_students()
    choosen_one = random.choice(students)

    return JSONResponse(choosen_one)
