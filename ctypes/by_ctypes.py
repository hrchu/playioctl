import ctypes
import os
import ioctl
import ioctl.linux
#import ioctl_opt

class mtop(ctypes.Structure):
    _fields_ = [("mt_op", ctypes.c_short),
    ("mt_count", ctypes.c_int)]

# alternatives
#MTIOCTOP = ioctl_opt.IOW(ord('m'), 1, mtop)
MTIOCTOP = ioctl.linux.IOW('m', 1, ctypes.sizeof(mtop))

mt_com = mtop(6,1)

fd = open('/dev/nst1', 'r')
ioctl.ioctl(fd.fileno(), MTIOCTOP, ctypes.byref(mt_com))
fd.close()

