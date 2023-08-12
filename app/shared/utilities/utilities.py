import os
import shutil
from multiprocessing.pool import ThreadPool
from threading import Thread

import requests
from fastapi import HTTPException
from requests.adapters import HTTPAdapter
from starlette import status
from urllib3 import Retry


def check_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def parallelize(threads_number, function, args, chunksize=1):
    pool = ThreadPool(threads_number)
    results = pool.starmap(function, args, chunksize=chunksize)
    pool.close()
    pool.join()
    return results


def threading(threads_number, function, args):
    threads = []
    for n in range(1, threads_number):
        t = Thread(target=function, args=args[n])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def get_requests_session():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def remove_dir_content(directory_path: str) -> None:
    for files in os.listdir(directory_path):
        path = os.path.join(directory_path, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


def bad_request(detail: str = 'Wrong params') -> HTTPException:
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
