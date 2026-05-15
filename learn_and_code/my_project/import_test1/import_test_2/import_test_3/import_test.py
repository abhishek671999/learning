import importlib
import os

print(os.getcwd())
abc = importlib.import_module('......codec.test_function.py'.strip('.py'))
print(abc.print_hello())