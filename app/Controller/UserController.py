import traceback

from fastapi import APIRouter, Depends
from app.Model.UserModel import UserModel, UserResponseModel
from fastapi.encoders import jsonable_encoder
from app.Config.view_data import ViewData

router = APIRouter()


@router.post("/create", response_model=UserResponseModel)
async def create_user(
    user: UserModel,
    view_data=Depends(ViewData.create)
):
    success = False
    try:
        view_data.user_repository.create_user(user)
        success = True
    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))

    return jsonable_encoder({"data": None, "success": success})

