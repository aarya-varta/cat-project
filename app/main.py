from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.services import get_cat_fact, get_cat_image

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )

@app.get("/random-cat")
async def random_cat():
    fact = await get_cat_fact()
    print(f"Cat fact -> {fact}")
    image = get_cat_image()

    return JSONResponse({
        "fact": fact,
        "image": image
    })