#!/usr/bin/env python3

# Python threading is optimized for I/O bound tasks. For example,
# requesting remote resources, connecting a database server, or reading and writing files.

import requests
import threading
from time import sleep, perf_counter

max_threads = 5
max_work = 5

url = 'https://api.covid19api.com'

data = {
    'prop1': 'value1',
    'prop2': 'value2'
}


def do_work(id):
    print(f"thread {id} start")
    for i in range(max_work):
        response = requests.get(url + '/summary')
        print(f"thread {id}:{i} -> {response.status_code}")
        # sleep(0)
    print(f"thread {id} done")


def main():
    threads = []
    for n in range(max_threads):
        # A daemon thread will shut down immediately when the program exits
        t = threading.Thread(target=do_work,args=(n,), daemon=False)
        threads.append(t)
        t.start()

    # wait to all threads to complete
    for t in threads:
        t.join()


if __name__ == '__main__':
    print("app start")
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f"app done in {end_time - start_time: 0.2f} seconds")
