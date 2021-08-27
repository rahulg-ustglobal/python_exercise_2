"""[[2,4,5],[4,6,8],[3,6,9]]
Considering the above list, we need to have a sum of all the values of all the inner lists.
- Find the sum of only even numbers
- Find the sum of all the numbers from all the inner lists
Don’t use a loop.
"""
numbers = [[2, 4, 5], [4, 6, 8], [3, 6, 9]]

print(numbers)
sum_of_all = map(lambda a: sum(a), numbers)
print("sum of all element is", sum(list(sum_of_all)))

sum_of_even = map(lambda a: sum(filter(lambda b: b % 2 == 0, a)), numbers)
print("sum of even no is", sum(list(sum_of_even)))


