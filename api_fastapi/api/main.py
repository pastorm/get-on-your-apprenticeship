from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from dummy import router as dummy_router
from users import router as users_router
from real import router as real_router

from settings import settings

#
# INITIALISATION
#
app = FastAPI()

app.mount("/static", StaticFiles(directory="api/static"), name="static")
templates = Jinja2Templates(directory="api/templates")

#
# CORS
#
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#
# Inclusions
#
app.include_router(dummy_router)
app.include_router(users_router)
app.include_router(real_router)

#
# Index
#

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": settings["TITLE"]}
    )
