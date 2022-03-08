from app.Config.config import Config
from app.Class.DatabaseClass import DatabaseClass
from app.Repository.TestRepository import TestRepository


class ViewData:
    def __init__(self):
        self.config = Config
        self.my_sql = DatabaseClass(self.config.MySqlConf)

        self.test_repository = TestRepository(self.config, self.my_sql)

    @staticmethod
    def create():
        return ViewData()
