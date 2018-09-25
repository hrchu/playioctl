#include <Python.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/mtio.h>


static PyObject * do_rewind(PyObject *self, PyObject *args) {
    // parse input
    const char *device;
    if (!PyArg_ParseTuple(args, "s", &device))
        return NULL;

    // open device file
    int fd;
    if ((fd = open(device, O_RDONLY)) < 0) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    // execute ioctl command
    struct mtop mt_com;
    mt_com.mt_op = MTREW; // #define MTREW	6 @mtio.h
    mt_com.mt_count = 1;

    if(ioctl(fd, MTIOCTOP, &mt_com) < 0) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    close(fd);

    // return nothing
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject * do_status(PyObject *self, PyObject *args) {
    // parse input
    const char *device;
    if (!PyArg_ParseTuple(args, "s", &device))
        return NULL;

    // open device file
    int fd;
    if ((fd = open(device, O_RDONLY)) < 0) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    // execute ioctl command
    struct mtget status;
    if (ioctl(fd, MTIOCGET, (char *)&status) < 0) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    if (status.mt_type != MT_ISSCSI2) {
        PyErr_SetString(PyExc_NotImplementedError, "Unsupported tape type");
        return NULL;
    }

    close(fd);

    // return status info in dict
    return Py_BuildValue("{s:i,s:i,s:i}",
              "file number", status.mt_fileno, "block number", status.mt_blkno, "partition", (status.mt_resid & 0xff));
}

static PyMethodDef MtMethods[] = {
    {"rewind",  do_rewind, METH_VARARGS,
     "Rewind the tape."},
    {"status",  do_status, METH_VARARGS,
     "Print status information about the tape unit."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef mtmodule = {
    PyModuleDef_HEAD_INIT,
    "mt",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    MtMethods
};

PyMODINIT_FUNC PyInit_mt(void) {
    PyObject* m = PyModule_Create(&mtmodule);
    if (m == NULL) {
        return NULL;
    }
    return m;
}

