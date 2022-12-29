# Python threading is optimized for I/O bound tasks. For example,
# requesting remote resources, connecting a database server, or reading and writing files.

import requests
import concurrent.futures
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
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        # executor.map(do_work, range(max_threads))
        for n in range(max_threads):
            executor.submit(do_work, n)


if __name__ == '__main__':
    print("app start")
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f"app done in {end_time - start_time: 0.2f} seconds")
