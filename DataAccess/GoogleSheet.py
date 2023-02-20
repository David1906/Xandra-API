import logging, gspread, os, sys
from oauth2client.service_account import ServiceAccountCredentials
from Models.Test import Test


class GoogleSheet:
    SHEET_NAME = "FBT Bahubali"
    SCOPE = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
        os.path.abspath(os.path.dirname(sys.argv[0]))
        + "/Static/yield-bahubali-f20f62671db6.json",
        SCOPE,
    )

    def add(self, test: Test):
        try:
            client = gspread.authorize(GoogleSheet.CREDENTIALS)
            sheet = client.open(GoogleSheet.SHEET_NAME).sheet1
            sheet.append_row(
                [
                    "",
                    test.serialNumber,
                    test.project,
                    test.startTime,
                    test.endTime,
                    test.codeVersion,
                    test.fixtureIp,
                    "PASS" if test.status else "FAILED",
                    test.stepLabel,
                    test.operator,
                ]
            )
        except Exception as e:
            logging.error("Error appending google sheet. " + str(e))
