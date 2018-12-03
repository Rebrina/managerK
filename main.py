import time
import subprocess
start_time = time.time()

class Timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        print("--- %s seconds ---" % (self.start))

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        print("%s took: %0.3f seconds" % (self.name, self.interval))
        return False

with Timer('Вызов браузера'):
     subprocess.Popen([r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])

print("--- %s seconds ---" % (time.time() - start_time))