from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from app.Model.TestModel import TestResponseModel
from app.Model.TestRedisModel import TestRedisModel
from app.Config.config import Config

from app.Config.view_data import ViewData

router = APIRouter()


@router.get("/", response_model=TestResponseModel)
async def test(
        view_data=Depends(ViewData.create)
):
    test_results = view_data.test_repository.get_all()
    return jsonable_encoder({"data": test_results})


@router.post("/add")
async def add_test_to_redis(
    test: TestRedisModel
):
    test.save(Config.RedisConf.redis_db)
    return 1


@router.get("/get_pks")
async def get_redis_pks():
    return TestRedisModel.all_pks()


@router.get("/get_reddis/{pk}")
async def get_redis_value(
        pk: str
):
    _test = TestRedisModel.get(pk)
    return _test
