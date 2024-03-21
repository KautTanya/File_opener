"""Декоратор з context-lib"""
from contextlib import contextmanager


@contextmanager
def file_opener(filename, mode):
    """Open and close file"""
    file = None
    try:
        file = open(filename, mode)
        yield file
    finally:
        if file is not None:
            file.close()


with file_opener("file.txt", "r") as f:
    # print(f.read())
    f.read()

# print(f.closed)
