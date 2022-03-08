from app.Config.config import Config
from app.Class.DatabaseClass import DatabaseClass


class ViewData:
    def __init__(self):
        self.config = Config
        self.my_sql = DatabaseClass(self.config.MySqlConf)

    @staticmethod
    def create():
        return ViewData()
