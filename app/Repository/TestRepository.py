from app.Class.DatabaseClass import DatabaseClass
from app.Config.config import Config


class TestRepository:
    def __init__(
        self,
        conf: Config = None,
        db: DatabaseClass = None
    ):
        self.conf = conf
        self.db = db

    def get_all(
        self
    ):
        query = f"""
            SELECT
                *
            FROM
                test
        """

        return self.db.query_to_array(query)
