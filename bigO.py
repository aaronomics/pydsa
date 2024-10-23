def print_items(n):
    for i in range(n):
        print(i)


print_items(10)


# O(n) is always linear



def print_items2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print_items2(10)


# nested for loops are O(n^2)

# you can drop non-dominant elements
# - if you have nested for loops and a single loop in the same function
# - the nested loop will dominate over time

# O(log_n) - binary search, works on sorted data


# if a function has 2 different parameters...

def print_items3(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

# this would be O(a + b), not O(n), but technically it is still O(n)

# and this....
def print_items4(a,b):
    for i in range(a):
        for j in range(b):
            print(i, j)

# would be O(a*b)

