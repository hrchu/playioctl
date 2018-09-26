# -*- coding: utf-8 -*-


import mt
import by_fcntl.mt
import by_ctypes.mt

from util import demo

DEVICE = '/dev/nst0'

# by cpython extension
demo(device=DEVICE, implement=mt)

# by prue fcntl
demo(device=DEVICE, implement=by_fcntl.mt)

# by python-ioctl and ctypes
demo(device=DEVICE, implement=by_ctypes.mt)