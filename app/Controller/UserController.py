import traceback

from fastapi import APIRouter, Depends
from app.Model.UserModel import UserModel, UserResponseModel
from fastapi.encoders import jsonable_encoder
from app.Config.view_data import ViewData
from app.Class.SecurityCaesarCipher import SecurityCaesarCipher

router = APIRouter()


@router.get("/get", response_model=UserResponseModel)
async def get_users(
    view_data=Depends(ViewData.create)
):
    users = None
    success = False

    try:
        users = view_data.user_repository.get_users()
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": users, "success": success})


@router.get("/get/{user_id}", response_model=UserResponseModel)
async def get_user(
    user_id: int,
    view_data=Depends(ViewData.create)
):
    user = None
    success = False

    try:
        user = view_data.user_repository.get_user_by_id(user_id)
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": [user], "success": success})


@router.post("/create", response_model=UserResponseModel)
async def create_user(
    user: UserModel,
    view_data=Depends(ViewData.create)
):
    success = False

    try:
        user.password = SecurityCaesarCipher.encrypt(user.password)
        view_data.user_repository.create_user(user)
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": None, "success": success})


@router.put("/update/{user_id}", response_model=UserResponseModel)
async def update_user(
    user_id: int,
    user_data: UserModel,
    view_data=Depends(ViewData.create)
):
    success = False

    try:
        view_data.user_repository.update_user(user_id, user_data)
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": None, "success": success})


@router.delete("/delete/{user_id}", response_model=UserResponseModel)
async def delete_user(
    user_id: int,
    view_data=Depends(ViewData.create)
):
    success = False

    try:
        view_data.user_repository.delete_user(user_id)
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": None, "success": success})
