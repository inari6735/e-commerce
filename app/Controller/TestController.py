from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from app.Model.TestModel import TestResponseModel

from app.Config.view_data import ViewData

router = APIRouter()


@router.get("/", response_model=TestResponseModel)
async def test(
        view_data=Depends(ViewData.create)
):
    test_results = view_data.test_repository.get_all()
    return jsonable_encoder({"data": test_results})
