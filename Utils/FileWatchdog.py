import time
from watchdog.observers.polling import PollingObserver


class FileWatchdog:
    def __init__(self, eventHandler):
        self.observer = PollingObserver()
        self.eventHandler = eventHandler

    def run(self, path):
        print(f"Watching {path}...")
        self.start(path)
        try:
            while True:
                time.sleep(5)
        except:
            self.stop()
        self.observer.join()

    def start(self, path):
        self.observer.schedule(self.eventHandler, path, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
