#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: Pointer to a Python object (assumed to be bytes)
 */
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints information about Python lists
 * @p: Pointer to a Python object (assumed to be a list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *element;

	printf("[*] Python list info\n");

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
		{
			element = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
			if (PyBytes_Check(element))
				print_python_bytes(element);
		}
	}
	else
	{
		printf("[ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: Pointer to a Python object (assumed to be bytes)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *str;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		str = PyBytes_AsString(p);

		printf("size: %ld\n", size);
		printf("trying string: %s\n", str);
		printf("first %ld bytes: ", size < 10 ? size : 10);

		for (i = 0; i < size && i < 10; i++)
		{
			printf("%02x", str[i] & 0xff);
			if (i < size - 1 && i < 9)
				printf(" ");
		}
		printf("\n");
	}
	else
	{
		printf("[ERROR] Invalid Bytes Object\n");
	}
}

