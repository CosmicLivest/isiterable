/* This is free and unencumbered software released into the public domain under The Unlicense (http://unlicense.org/)
 * main repo: https://github.com/CosmicLivest/isiterable
 * author: CosmicLivest
 * example:
 *     $python
 *     >>> from isiterable import isiterable
 *     >>> class A: pass
 *     >>> class B:
 *     >>>     def __iter__(self):
 *     >>>         for i in range(15):
 *     >>>             yield i
 *     >>> isiterable(A)
 *     False
 *     >>> isiterable(B)
 *     False
 *     >>> x = B()
 *     >>> isiterable(x)
 *     True
 */

#define PY_SSIZE_T_CLEAN
#include <Python.h>

// `isiterable` function
static PyObject *isiterable(PyObject *self, PyObject *obj[], Py_ssize_t length) {
	if (length != (Py_ssize_t)1) {
		PyErr_Format(PyExc_TypeError,
				"isiterable() takes only 1 argument (%i given)", length);
		return NULL;
	}
	PyTypeObject *t = obj[0]->ob_type;
	if (t->tp_iter == NULL) {
		if (PySequence_Check(obj[0])) {
			// The iterator is empty or if it's done, Proceed to call `next()`
			Py_INCREF(Py_True);
			return Py_True;
		}
		Py_INCREF(Py_False);
		return Py_False;
	}
	PyObject *res = (*(t->tp_iter))(obj[0]);
	if (res != NULL && !PyIter_Check(res)) {
		Py_DECREF(res);
		Py_INCREF(Py_False);
		return Py_False;
	}
	Py_DECREF(res);
	Py_INCREF(Py_True);
	return Py_True;

};


static PyMethodDef isiterable_methods[] = {
	// As the function is too simple, We will use 'METH_FASTCALL'
	{"isiterable", isiterable, METH_FASTCALL,
		"If the object is iterable returns True, Otherwise returns False.\n"
		"\n"
		"Args:\n"
		"    param1 (obj): Object to be verified.\n"
		"\n"
		"Returns:\n"
		"    bool: True if the object is iterable, Otherwise False.\n"
		"\n"
		"Example:\n"
		"    >>> isiterable(57890)\n"
		"    False\n"
		"    >>> isiterable(['Hello!', 57890])\n"
		"    True"},
	{NULL, NULL, 0, NULL}
};

static PyModuleDef isiterable_module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "isiterable",
    .m_doc = "This module provides a function to check if an object is iterable quickly and efficiently.\n"
	    "\n"
	    "Example:\n"
	    "    >>> from isiterable import isiterable\n"
	    "    >>> class A: pass\n"
	    "    >>> isiterable(A)\n"
	    "    False\n"
	    "    >>> isiterable([90, 1000, object()])\n"
	    "    True",
    .m_size = -1,
    isiterable_methods
};


PyMODINIT_FUNC PyInit_isiterable(void) {
	PyObject *m;
	m = PyModule_Create(&isiterable_module);
	if (m == NULL) return NULL;
	return m;
}

/* This is free and unencumbered software released into the public domain.
 *
 * Anyone is free to copy, modify, publish, use, compile, sell, or
 * distribute this software, either in source code form or as a compiled
 * binary, for any purpose, commercial or non-commercial, and by any
 * means.
 *
 * In jurisdictions that recognize copyright laws, the author or authors
 * of this software dedicate any and all copyright interest in the
 * software to the public domain. We make this dedication for the benefit
 * of the public at large and to the detriment of our heirs and
 * successors. We intend this dedication to be an overt act of
 * relinquishment in perpetuity of all present and future rights to this
 * software under copyright law.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 * OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 * ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 *
 * For more information, please refer to <http://unlicense.org/>
 */
