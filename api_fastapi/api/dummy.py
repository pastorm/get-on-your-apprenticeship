from fastapi import APIRouter
from fastapi.responses import PlainTextResponse, JSONResponse


router = APIRouter(prefix="/dummy", tags=["dummy"])


@router.get("/")
async def dummy():
    return PlainTextResponse("This is a dummy route")


@router.get("/student/")
async def get_student():
    return PlainTextResponse("Harry Potter !")


@router.get("/students/")
async def list():
    return JSONResponse(
        [
            {"name": "Harry Potter", "house": "Gryffindor"},
            {"name": "Hermione Granger", "house": "Gryffindor"},
            {"name": "Ron Weasley", "house": "Gryffindor"},
            {"name": "Neville Longbottom", "house": "Gryffindor"},
            {"name": "Luna Lovegood", "house": "Ravenclaw"},
        ]
    )
