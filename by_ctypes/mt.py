import ctypes

# https://github.com/olavmrk/python-ioctl
from by_ctypes import ioctl
from by_ctypes.ioctl import linux

# import ioctl_opt

class mtop(ctypes.Structure):
    _fields_ = [
        ("mt_op", ctypes.c_short),
        ("mt_count", ctypes.c_int)
    ]


class mtget(ctypes.Structure):
    _fields_ = [
        ("mt_type", ctypes.c_long),
        ("mt_resid", ctypes.c_long),
        ("mt_dsreg", ctypes.c_long),
        ("mt_gstat", ctypes.c_long),
        ("mt_erreg", ctypes.c_long),
        ("mt_fileno", ctypes.c_int),
        ("mt_blkno", ctypes.c_int),
    ]


def rewind(device):
    # MTIOCTOP = ioctl_opt.IOW(ord('m'), 1, mtop) # alternatives
    MTIOCTOP = ioctl.linux.IOW('m', 1, ctypes.sizeof(mtop))
    MTREW = 6
    mt_com = mtop(MTREW, 1)

    with open(device, 'r') as fd:
        ioctl.ioctl(fd.fileno(), MTIOCTOP, ctypes.byref(mt_com))


def status(device):
    status = mtget()
    MTIOCGET = ioctl.linux.IOR('m', 2, ctypes.sizeof(mtget))

    with open(device, 'r') as fd:
        ioctl.ioctl(fd.fileno(), MTIOCGET, ctypes.byref(status))
        return {
            "file number": status.mt_fileno,
            "block number": status.mt_blkno,
            "partition": status.mt_resid & 0xff
        }
