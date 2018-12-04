import time
import subprocess

class timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        print("Program run start: %0.3f seconds" % (self.start))

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        print("Program run end: %0.3f seconds" % (self.end))
        print("%s took: %0.3f seconds" % (self.name, self.interval))
        return False

with timer('Browser call'):
     subprocess.Popen([r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])