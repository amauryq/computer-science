# Python threading is optimized for I/O bound tasks. For example,
# requesting remote resources, connecting a database server, or reading and writing files.

import requests
import threading
from time import perf_counter

max_threads = 5
max_work = 5

url = 'https://api.covid19api.com'

data = {
    'prop1': 'value1',
    'prop2': 'value2'
}

class MyThread(threading.Thread):
    id: int

    def __init__(self, id):
        super(MyThread, self).__init__()
        self.id = id

    def run(self):
        print(f"thread {self.id} start")
        for i in range(max_work):
            response = requests.get(url + '/summary')
            print(f"thread {self.id}:{i} -> {response.status_code}")
        print(f"thread {self.id} done")


def main():
    threads = [MyThread(n) for n in range(max_threads)]
    for n in threads:
        n.start()
    # wait to all threads to complete
    for t in threads:
        t.join()


if __name__ == '__main__':
    print("app start")
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f"app done in {end_time - start_time: 0.2f} seconds")
