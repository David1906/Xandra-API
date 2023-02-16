import logging
from watchdog.events import FileSystemEventHandler
from DataAccess.TestData import TestData


class SfcEventHandler(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()
        self.testData = TestData()

    def on_created(self, event):
        try:
            print(f"Created -> {event.src_path}")
            test = self.testData.parse(event.src_path)
            self.testData.add(test)
        except Exception as e:
            logging.error(str(e))

    def on_deleted(self, event):
        print(f"Deleted -> {event.src_path}")
