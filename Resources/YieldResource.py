from flask_restful import Resource, request
from DataAccess.TestData import TestData
from Utils.ApiDecorators import HandleInternalError, ValidateArgs


class YieldResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.testData = TestData()

    @HandleInternalError
    @ValidateArgs(requiredArgs=["fixtureIp", "yieldCalcQty", "lastTestPassQty"])
    def get(self):
        fixtureIp = request.args["fixtureIp"]
        return {
            "fixtureIp": fixtureIp,
            "yield": self.testData.getYield(
                fixtureIp, int(request.args["yieldCalcQty"])
            ),
            "areLastTestPass": self.testData.areLastTestPass(
                fixtureIp, int(request.args["lastTestPassQty"])
            ),
        }
