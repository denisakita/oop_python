import tracemalloc
from random import random


class Car:
    __slots__ = ['id', 'lat', 'lng']

    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = lat
        self.lng = lng


def rand_lat():
    return random() * 180 - 90


def rand_lng():
    return random() * 360 - 180


def mb(bytes):
    return bytes / 1_000_000


size = 100_000

tracemalloc.start()
cars = [Car(i, rand_lat(), rand_lng()) for i in range(size)]
current, peak = tracemalloc.get_traced_memory()
print('Current', mb(current))

""" Key Concepts
Normal Attribute Storage:

In a typical Python class, attributes are stored in a dictionary. This allows for fast access but uses more memory.

Using __slots__:

__slots__ is a special attribute you can add to a class to specify a fixed set of attributes.
By defining __slots__, Python no longer uses a dictionary to store attributes, which reduces memory usage.


Detailed Explanation
Memory Usage:

When you have many instances of a class, each instance's dictionary can consume a lot of memory.
Using __slots__ can significantly reduce this memory usage.

Example:

Imagine you have a Car class with attributes id, latitude, and longitude.
Normally, each Car instance would store these attributes in a dictionary.
By adding __slots__ = ['id', 'latitude', 'longitude'] to the class, you tell Python to store these attributes in a more memory-efficient way.


Practical Demonstration
Without __slots__:

The instructor creates 100,000 Car instances and measures the memory usage, which is around 18.39 megabytes.

With __slots__:

By adding __slots__, the memory usage drops to 14.47 megabytes, showing significant savings.


Limitations
Fixed Attributes:
Once you define __slots__, you cannot add new attributes to instances of the class. This is a trade-off for the memory efficiency.


Analogy
Toolbox Analogy:
Think of a class as a toolbox. Normally, you have a big toolbox with many compartments (a dictionary) to store different tools (attributes). This makes it easy to find tools quickly but takes up more space.
Using __slots__ is like having a smaller toolbox with fixed slots for specific tools. It takes up less space but can only hold the tools you specified.


Summary
Memory Saving: Using __slots__ can significantly reduce memory usage, especially when you have many instances of a class.
Fixed Attributes: You can only use the attributes you defined in __slots__. You can't add new ones later."""
