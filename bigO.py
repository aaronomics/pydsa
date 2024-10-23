def print_items(n):
    for i in range(n):
        print(i)


print_items(10)

"""
O(n) is always linear



"""


def print_items2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print_items2(10)

"""
nested for loops are O(n^2)

you can drop non-dominant elements
- if you have nested for loops and a single loop in the same function
- the nested loop will dominate over time
"""
