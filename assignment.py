def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer:
# The followint is printed: 
#     3
#     4
# 
# First, we take each of the values in the array [1, 2, 3] and temprarly store them as number. 
# For each of them, we compare if the number is bigger than 1 (only happens for 2 and 3).
# In those cases, the number is passed as the argument to the add_one function and 
# the function returns the next integer to the number that we passed.  
#     1 --> Nothing
#     2 --> 3
#     3 --> 4

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer:
# add_one(2) returns the number 3. 
# The difference is that return inside the function is passing a value to whoever
# called that function, while the print in the loop is taking the value that the function
# add_one() returns and then printing it.