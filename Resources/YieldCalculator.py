import logging
from flask_restful import Resource, request
from DataAccess.TestData import TestData


class YieldCalculator(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.testData = TestData()

    def get(self):
        try:
            for argument in ["fixtureIp", "lastTestPassQty"]:
                if not argument in request.args:
                    return {"message": f"Argument required: {argument}"}, 400

            fixtureIp = request.args["fixtureIp"]
            return {
                "fixtureIp": fixtureIp,
                "yield": round(self.testData.getYield(fixtureIp), 2),
                "areLastTestPass": self.testData.areLastTestPass(
                    fixtureIp, int(request.args["lastTestPassQty"])
                ),
            }
        except Exception as e:
            logging.error(str(e))
            return {"message": f"Internal error: {str(e)}"}, 500
