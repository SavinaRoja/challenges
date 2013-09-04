#include <python2.7/Python.h>
#include <gmp.h>

/* A library of modular utility methods which can be employed in multiple
 * problems for Project Euler. These are implemented in C and compiled for use
 * through simple python module loading.
 * Author: Paul Barton
 */

static PyObject *PE_Error;

static PyObject *
c_fibo_iter(PyObject *self, PyObject *args)
{
    mpz_t a;
    mpz_t b;
    mpz_t c;
    mpz_init_set_ui(a, 0);
    mpz_init_set_ui(b, 1);
    mpz_init(c);
    
    
    char *max;
    mpz_t gmp_max;
    
    if (!PyArg_ParseTuple(args, "s", &max)) {
        return NULL;
    }
    mpz_init_set_str(gmp_max, max, 10);
    free(max);
    
    gmp_printf("%Zd\n", a);
    while (mpz_cmp(b, gmp_max) <= 0) {
        gmp_printf("%Zd\n", b);
        mpz_add(c, a, b);
        mpz_set(a, b);
        mpz_set(b, c);
    }
    Py_RETURN_NONE;
    
}

static PyObject *
c_maths_test(PyObject *self, PyObject *args)
{
    printf("This is a test of the c maths import system");
    Py_RETURN_NONE;
};

static PyMethodDef ProjectEulerMethods[] = {
    {"test", c_maths_test, METH_VARARGS,
     "This is the documentation of the c_maths.test() function.\n"},
    {"c_fibo_iter", c_fibo_iter, METH_VARARGS,
     "Prints the fibonacci sequence up the passed integer.\n"},
    {NULL, NULL, 0, NULL}// Sentinel
};

PyMODINIT_FUNC
initc_maths(void)
{
    PyObject *m;

    m = Py_InitModule("c_maths", ProjectEulerMethods);
    if (m == NULL)
        return;

    PE_Error = PyErr_NewException("projecteuler.error", NULL, NULL);
    Py_INCREF(PE_Error);
    PyModule_AddObject(m, "error", PE_Error);
}
