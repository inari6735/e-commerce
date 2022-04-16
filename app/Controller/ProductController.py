import traceback

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from app.Model.ProductModel import ProductModel, ProductResponseModel
from app.Config.view_data import ViewData


router = APIRouter()


@router.get("/products", response_model=ProductResponseModel)
async def get_products(
    view_data=Depends(ViewData.create)
):
    products = None
    success = False

    try:
        products = view_data.product_repository.get_products()
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": products, "success": success})


@router.get("/product/{product_id}", response_model=ProductResponseModel)
async def get_products(
    product_id: int,
    view_data=Depends(ViewData.create)
):
    product = None
    success = False

    try:
        product = view_data.product_repository.get_product(product_id)
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": [product], "success": success})


@router.post("/create", response_model=ProductResponseModel)
async def create_product(
    product_data: ProductModel,
    view_data=Depends(ViewData.create)
):
    success = False

    try:
        view_data.product_repository.create_product(product_data)
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": None, "success": success})


@router.put("/update/{product_id}", response_model=ProductResponseModel)
async def update_product(
    product_id: int,
    product_data: ProductModel,
    view_data=Depends(ViewData.create)
):
    success = False

    try:
        view_data.product_repository.update_product(product_id, product_data)
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": None, "success": success})


@router.delete("/delete/{product_id}", response_model=ProductResponseModel)
async def delete_product(
    product_id: int,
    view_data=Depends(ViewData.create)
):
    success = False

    try:
        view_data.product_repository.delete_product(product_id)
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": None, "success": success})
