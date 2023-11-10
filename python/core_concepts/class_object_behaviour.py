# class A:
#     class_var = 1
#
#     @classmethod
#     def class_method(cls):
#         cls.class_var = 2
#
#
# objectA_1 = A()
# print(objectA_1.class_var, A.class_var)
# objectA_2 = A()
# print(objectA_2.class_var, A.class_var)
# objectA_1.class_var = 2
# A.class_var = 3
# print('After changing')
# print(objectA_1.class_var, A.class_var)
# print(objectA_2.class_var, A.class_var)
#
#
# class A:
#     def functionA(self):
#         print('This is a function in A')
#
# def functionB(self):
#     print('This is function outside: B')
#
# A.functionB = functionB
#
# a = A()
# a.functionA()
# a.functionB()

class A:
    def method(self):
        print('method A')

class B:
    def method(self):
        print('method B')

class C(A, B):
    def method(self):
        B.method(self)


c = C()
c.method()

import copy
a = [1,2,[3,4]]
b = copy.deepcopy(a)
a[2].append(4)
print(a)
print(b)

# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: [a + [b]], lis))


print(list(map(lambda x: x+1, [1, 2, 3, 4])))