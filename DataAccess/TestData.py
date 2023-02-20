import logging, re
from datetime import datetime
from DataAccess.GoogleSheet import GoogleSheet
from DataAccess.MySqlConnector import MySqlConnector
from Models.Test import Test


class TestData:
    REGEX_RESULT = "^result\s*:(pass|failed)+\s*"

    def __init__(self) -> None:
        self.mySqlConnector = MySqlConnector()

    def parse(self, fullPath: str) -> Test:
        try:
            with open(fullPath, "r") as fp:
                test = Test()
                for l_no, line in enumerate(fp):
                    if test.serialNumber == None and self.search("Board\s*SN", line):
                        test.serialNumber = self.extractValue(line)
                        continue

                    if test.project == None and self.search("Project\s*Name", line):
                        test.project = self.extractValue(line)
                        continue

                    if test.startTime == None and self.search("Start\s*Time", line):
                        test.startTime = self.extractDateTime(line)
                        continue

                    if test.endTime == None and self.search("End\s*Time", line):
                        test.endTime = self.extractDateTime(line)
                        continue

                    if test.codeVersion == None and self.search(
                        "test\s*code\s*ver", line
                    ):
                        test.codeVersion = self.extractValue(line)
                        continue

                    if test.fixtureIp == None and self.search("FixtureIP", line):
                        value = self.extractValue(line)
                        if value != "":
                            test.fixtureIp = value
                        continue

                    if test.status == None and self.search("result", line):
                        test.status = self.search("pass", line)
                        test.stepLabel = re.sub(
                            TestData.REGEX_RESULT, "", line, flags=re.I
                        ).strip()
                        continue

                    if test.operator == None and self.search("Operator\s*ID", line):
                        test.operator = self.extractValue(line)
                        continue

                    if test.isComplete():
                        break
                return test
        except Exception as e:
            logging.error(str(e))
            return Test()

    def search(self, pattern: str, string: str) -> bool:
        return re.search(pattern, string, re.IGNORECASE) != None

    def extractDateTime(self, line: str) -> datetime:
        value = self.extractValue(line)
        dt = datetime.strptime(value, "%Y%m%d_%H%M%S")
        return dt.isoformat()

    def extractValue(self, line: str) -> str:
        return line.split(":")[1].strip()

    def add(self, test: Test):
        if test.fixtureIp == None:
            return
        db = self.mySqlConnector.getConnector()
        sql = f"""
        INSERT INTO `tests` (`testId`, `serialNumber`, `project`, `startTime`, `endTime`, `codeVersion`, `fixtureIp`, `status`, `stepLabel`, `operator`) 
        VALUES (
            NULL, 
            '{test.serialNumber}',
            '{test.project}',
            '{test.startTime}',
            '{test.endTime}',
            '{test.codeVersion}',
            '{test.fixtureIp}',
             {test.status},
            '{test.stepLabel}',
            '{test.operator}'
        )"""
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        GoogleSheet().add(test)

    def getYield(self, fixtureIp: str, qty: int = 10) -> float:
        tests = self.find(fixtureIp, qty)
        if len(tests) == 0:
            return 100
        passTests = 0
        for test in tests:
            if test["status"]:
                passTests += 1
        return round((passTests / len(tests)) * 100, 2)

    def areLastTestPass(self, fixtureIp: str, qty: int = 3) -> bool:
        tests = self.find(fixtureIp, qty)
        if len(tests) >= qty:
            for test in tests:
                if not test["status"]:
                    return False
        return True

    def find(self, fixtureIp: str, qty: int = 10) -> "list[Test]":
        db = self.mySqlConnector.getConnector()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            f"SELECT * FROM `tests` WHERE fixtureIp='{fixtureIp}' ORDER BY endTime DESC LIMIT {qty};"
        )
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
