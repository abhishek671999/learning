import importlib

abc = importlib.import_module('....codec.test_function.py'.strip('.py'))
print(abc.print_hello())