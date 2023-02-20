import logging, os
from flask import Flask
from flask_restful import Api
from waitress import serve
from Resources.TestResource import TestResource
from Resources.YieldResource import YieldResource
from Utils.FileWatchdog import FileWatchdog
from Utils.SfcEventHandler import SfcEventHandler
from dotenv import dotenv_values

config = dotenv_values(os.path.dirname(os.path.abspath(__file__)) + "/.env")
logging.basicConfig(filename="log.txt", level=logging.ERROR)

app = Flask(__name__)
api = Api(app)
api.add_resource(YieldResource, "/yield")
api.add_resource(TestResource, "/test")

if __name__ == "__main__":
    FileWatchdog(SfcEventHandler()).start(config["FBT_LOGS_PATH"])
    # app.run(debug=True)
    serve(app, host="0.0.0.0", port=5000)
