from typing import Annotated, Literal
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


product_list = [
    {
        "item_name": "Salsa Verde",
        "category": "Salsa",
        "spice_level": 1,
        "size": 270,
        "desc": "Bright and mild green salsa.",
        "image_url": "http://127.0.0.1:8000/media/SalsaVerde.png",
        "price": 250,
    },
    {
        "item_name": "Salsa Roja",
        "category": "Salsa",
        "spice_level": 2,
        "size": 270,
        "desc": "Classic smoky red salsa.",
        "image_url": "http://127.0.0.1:8000/media/SalsaRoja.png",
        "price": 250,
    },
    {
        "item_name": "Salsa Macha",
        "category": "Salsa",
        "spice_level": 4,
        "size": 270,
        "desc": "Crunchy chile oil salsa.",
        "image_url": "http://127.0.0.1:8000/media/SalsaMacha.png",
        "price": 250,
    },
    {
        "item_name": "Salsa Habanero",
        "category": "Salsa",
        "spice_level": 5,
        "size": 270,
        "desc": "Hot and fruity habanero salsa.",
        "image_url": "http://127.0.0.1:8000/media/SalsaHabanero.png",
        "price": 250,
    },
    {
        "item_name": "Tajin",
        "category": "Condiment",
        "spice_level": 2,
        "size": 142,
        "desc": "Tangy chile lime seasoning.",
        "image_url": "http://127.0.0.1:8000/media/SalsaVerde.png",
        "price": 120,
    },
    {
        "item_name": "Taco Seasoning",
        "category": "Condiment",
        "spice_level": 1,
        "size": 50,
        "desc": "Savory taco spice blend.",
        "image_url": "http://127.0.0.1:8000/media/SalsaVerde.png",
        "price": 90,
    },
]


class Product(BaseModel):
    item_name: str
    category: Literal["Salsa", "Condiment"]
    spice_level: Literal[1, 2, 3, 4, 5] | None = None
    size: int
    desc: str | None = None
    image_url: str
    price: float


app = FastAPI()

app.mount("/media", StaticFiles(directory="media"), name="media")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Application": "Salsas Backend"}


@app.get("/products/")
async def get_products(
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
):
    return product_list[skip : skip + limit]


@app.post("/products/")
async def create_product(product: Product):
    product_list.append(product.model_dump())
    return product
