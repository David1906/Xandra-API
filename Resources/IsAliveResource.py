from flask_restful import Resource
from DataAccess.TestData import TestData


class IsAliveResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.testData = TestData()

    def get(self):
        return {"message": f"Xandra API is alive"}
