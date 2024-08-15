import sqlite3


class Proxy:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, attr):
        value = getattr(self.obj, attr)
        print(f'{attr} -> {value!r}')
        return value


conn = sqlite3.connect(':memory:')
proxy = Proxy(conn)
n = proxy.total_changes
print(n)

proxy.close()

"""
__getattr__ vs. __getattribute__:

__getattr__ is called only when the regular attribute access mechanism fails to find an attribute.
__getattribute__ bypasses the whole attribute access mechanism and is riskier, often leading to infinite recursions if not used carefully.

Example Usage:

The instructor demonstrates creating a proxy class that logs every time an attribute is accessed from an underlying object, using __getattr__.

Practical Application:

This technique can be useful for logging, debugging, or creating dynamic attributes in a class.
"""
