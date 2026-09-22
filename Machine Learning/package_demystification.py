"""
This sample shows how to inspect the publicly accessible
names and objects in an unknown Python library.
"""
import medmnist

available = [name for name in dir(medmnist) if not name.startswith("_")]

for name in available:
    print(name)