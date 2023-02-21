from flask import jsonify, request
from flask_restful import Resource
from DataAccess.TestData import TestData
from Utils.ApiDecorators import HandleInternalError, ValidateArgs


class TestsResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.testData = TestData()

    @HandleInternalError
    @ValidateArgs(requiredArgs=["fixtureIp", "qty"])
    def get(self):
        data = self.testData.find(request.args["fixtureIp"], request.args["qty"])
        return jsonify({"data": data})
