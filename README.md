How to do hardware control via ioctl from Python feat. magnetic tape drive
===============================================================================

![Screenshot](https://user-images.githubusercontent.com/3183314/46056862-583cf080-c185-11e8-9b98-4d0a7853787d.png)

Two operations, i.e., rewind and status, are presented. Both of the operations are implemented in three kinds of ways, including **cpython extenstion**, **ctypes** and **fcntl**.
The code is intended to show how to do hardware control in Taipei.py (Sep. 2018) and europython 2020.

## Prerequisites

1. Python 3 / Linux
2. You will need either a real tape drive or use **mhvtl** as a simulate tape drive.
3. root privilege is necessary to operations of magnetic tape drive

## How to run

1. install the cpython extension
 - ``$ cd [project_home]/by_cpython_extension/pymt``
 - ``$ pip install .``
2. Run the demo code ``$ python demo.py``

## Courtesy
* [olavmrk/python-ioctl](https://github.com/olavmrk/python-ioctl)
* [vpelletier/python-ioctl-opt](https://github.com/vpelletier/python-ioctl-opt)
