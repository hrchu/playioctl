#include <Python.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/mtio.h>


static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    int fd = open("/dev/nst1", O_RDONLY);

    struct mtop mt_com;

    mt_com.mt_op = 6;
    mt_com.mt_count = 1;

    ioctl(fd, MTIOCTOP, &mt_com);

    close(fd);

    return PyLong_FromLong(0);
/*
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    if (sts < 0) {
        return NULL;
    }
    return PyLong_FromLong(sts);
*/
}

static PyMethodDef SpamMethods[] = {
    {"system",  spam_system, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void) {
    PyObject* m = PyModule_Create(&spammodule);
    if (m == NULL) {
        return NULL;
    }
    return m;
}

