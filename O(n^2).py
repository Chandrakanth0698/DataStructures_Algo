
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

"""
Here there is a for loop inside a for loop which gives us
 exponential number of operations performed
 the time complexity becomes O(n^2)
 
 """

print_items(10)