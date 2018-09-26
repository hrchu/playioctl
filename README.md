Various ways to control a magnetic tape drive in Python ✨🍰✨
============================================================

![Screenshot](https://user-images.githubusercontent.com/3183314/46056862-583cf080-c185-11e8-9b98-4d0a7853787d.png)

Demo code for controlling magnetic tape drives under Linux from Python. 
Only two magnetic tape drive operations are implemented currently, i.e., rewind and status.
Operations are implemented in three kinds of ways, includes cpython extenstion, ctypes, and prue fcntl provided by python runtime.
The code is intended to show how to control hardware by Python and is presented in Taipei.py meetup in Sep. 2018.

## Prerequisites

1. Python 3 / Linux
1. root privilege is necessary to operations of magnetic tape drive

## How to run

1. ``$ cd [project_home]/by_cpython_extension/pymt``
2. ``$ pip install .``
3. ``$ python demo.py``

