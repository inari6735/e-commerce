from app.Config.config import Config
from app.Class.DatabaseClass import DatabaseClass
from app.Repository.UserRepository import UserRepository
from app.Repository.ProductRepository import ProductRepository


class ViewData:
    def __init__(self):
        self.config = Config
        self.my_sql = DatabaseClass(self.config.MySqlConf)

        self.user_repository = UserRepository(self.config, self.my_sql)
        self.product_repository = ProductRepository(self.config, self.my_sql)

    @staticmethod
    def create():
        return ViewData()
