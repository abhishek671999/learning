def zero_division_validation(func):
    def inner(a, b):
        if b == 0:
            raise ZeroDivisionError
        return func(a, b)
    return inner

def add_two(func):
    def inner(a,b):
        return func(a,b) + 2
    return inner
@add_two
@zero_division_validation
def division(a,b):
    return a/b

print(division(4, 2))

a = 1
a += 2
print(a)
print(a -+ 2)

