# class A:
#     def method(self):
#         print('This is class A')
#
# class B:
#     def method(self):
#         print('This is class B')
#
# class C(A, B):
#     def method(self):
#         super(C, self).method()
#
#
# c = C()
# c.method()

# list1 = [1,[2],3]
# list2 = list1.copy()
# print(list1, id(list1), list2, id(list2))
# list2[1].append(5)
# print(list1, id(list1), list2, id(list2))

a = 1
def function(lst):
    lst.append(4)
    print(lst)



list1 = [1 , 2, 3]
print(list(map(lambda x: x+1, list1)))
function(list1.copy())
print(list1)


dictionary = {'name': 'abhishek'}
if 'name' in dictionary:
    print('yes')