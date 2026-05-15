import sys


class A:
    def method_B(self):
        print('methodBb')
        getattr(self, 'method_B')()


this = sys.modules[__name__]
this.name ='abhishek'

print(this.name, 'In abc')