#include "Python.h"


static PyObject *

spam_strlen(PyObject *self, PyObject *args)
{
    char* str;
    size_t len;
    if(!PyArg_ParseTuple(args, "s", &str)) {  // 매개변수 값을 분석하고 지역 변수에 할당
        return NULL;
    }

    len = strlen(str);
    return Py_BuildValue("i", len);

}


static PyObject*

write_log(PyObject *self, PyObject *args) // 인자는 이와같이 고정된다.
{
    char* msg;
    FILE *fp;

    if(!PyArg_ParseTuple(args, "s", &msg))
        return NULL;

    fp = fopen("pylog.txt", "wt+");
    fprintf(fp, msg);

    fclose(fp);

    return Py_BuildValue("i", 0);
}


static PyObject *

simple_add_func(PyObject *self, PyObject *args)
{
    int num;
    int rv=0;
    if(!PyArg_ParseTuple(args, "i", &num)) {
        return NULL;
    }

    while(num>0) {
        rv = rv + num--;
    }

    return Py_BuildValue("i", rv);

}


static PyMethodDef SpamMethods[] = {
    {"strlen", spam_strlen, METH_VARARGS, "count a string length."},
    {"write_log", write_log, METH_VARARGS, "write log into pylog.txt file."},
    {"simple_add", simple_add_func, METH_VARARGS, "simple add function."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "customlib",
    "Test module.",
    -1, SpamMethods
};

PyMODINIT_FUNC
PyInit_customlib(void)
{
    return PyModule_Create(&spammodule);
}