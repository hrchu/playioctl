import fcntl
import struct

# https://github.com/vpelletier/python-ioctl-opt

_IOC_NRBITS = 8
_IOC_TYPEBITS = 8
_IOC_SIZEBITS = 14
_IOC_DIRBITS = 2

_IOC_NRMASK = (1 << _IOC_NRBITS) - 1
_IOC_TYPEMASK = (1 << _IOC_TYPEBITS) - 1
_IOC_SIZEMASK = (1 << _IOC_SIZEBITS) - 1
_IOC_DIRMASK = (1 << _IOC_DIRBITS) - 1

_IOC_NRSHIFT = 0
_IOC_TYPESHIFT = _IOC_NRSHIFT + _IOC_NRBITS
_IOC_SIZESHIFT = _IOC_TYPESHIFT + _IOC_TYPEBITS
_IOC_DIRSHIFT = _IOC_SIZESHIFT + _IOC_SIZEBITS

IOC_NONE = 0
IOC_WRITE = 1
IOC_READ = 2


def IOC(dir, type, nr, size):
    """
    dir
        One of IOC_NONE, IOC_WRITE, IOC_READ, or IOC_READ|IOC_WRITE.
        Direction is from the application's point of view, not kernel's.
    size (14-bits unsigned integer)
        Size of the buffer passed to ioctl's "arg" argument.
    """
    assert dir <= _IOC_DIRMASK, dir
    assert type <= _IOC_TYPEMASK, type
    assert nr <= _IOC_NRMASK, nr
    assert size <= _IOC_SIZEMASK, size
    return (dir << _IOC_DIRSHIFT) | (type << _IOC_TYPESHIFT) | (nr << _IOC_NRSHIFT) | (size << _IOC_SIZESHIFT)


def IOC_SIZECHECK(t):
    """
    Returns the size of given type, and check its suitability for use in an
    ioctl command number.
    """
    result = t
    assert result <= _IOC_SIZEMASK, result
    return result


def IOW(type, nr, size):
    """
    An ioctl with write parameters.
    size
    """
    return IOC(IOC_WRITE, type, nr, IOC_SIZECHECK(size))


def IOR(type, nr, size):
    """
    An ioctl with read parameters.
    size (ctype type or instance)
        Type/structure of the argument passed to ioctl's "arg" argument.
    """
    return IOC(IOC_READ, type, nr, IOC_SIZECHECK(size))


def rewind(device):
    MTREW = 6
    mt_com = struct.pack('hi', MTREW, 1)
    MTIOCTOP = IOW(ord('m'), 1, len(mt_com))

    with open(device, 'r') as fd:
        fcntl.ioctl(fd, MTIOCTOP, mt_com)


def status(device):
    long_size = 8
    int_size = 4
    status = bytearray(long_size * 5 + int_size * 2)
    MTIOCGET = IOR(ord('m'), 2, len(status))

    with open(device, 'r') as fd:
        fcntl.ioctl(fd, MTIOCGET, status)
        status = struct.unpack('lllllii', status)
        return {
            "file number": status[-2],
            "block number": status[-1],
            "partition": status[1] & 0xff
        }
