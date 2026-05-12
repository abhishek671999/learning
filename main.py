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

from -> join -> where -> group by -> having -> select -> limit
# Write your MySQL query statement below
SELECT DISTINCT num ConsecutiveNums from LOGS WHERE (id, num) in (SELECT id+1, num FROM LOGS) AND (id, num) in (SELECT id+2, num FROM LOGS)

with cte as (select player_id, min(event_date) over(partition by player_id) + 1= event_date as is_return from activity)
select round(sum(is_return)/count(distinct player_id), 2)  as fraction from cte


