# Write a program to create a list of n integer values and do the following
# Add an item in to the list (using function)
# Delete (using function)
# Store the largest number from the list to a variable
# Store the Smallest number from the list to a variable

a = [1, 2, 3, 4, 5, 6]
hi = max(a)
lo = min(a)
print(hi)
print(lo)

b = [1, 2, 3, 4, 5]
del b[3]
print(b)

c = list([1, 2, 3, 4])
c.append(8)
print(c)

# Create a tuple and print the reverse of the created tuple
# method1
d = (1, 2, "hey", "hello", 3, 4)
print(d)
e = reversed(d)
print(tuple(e))

# method2
tuples = (1, 2, 3, 4, 5, 67, 8)
reversedTuples = tuples[::-1]
print(reversedTuples)

# Create a tuple and convert tuple into list
f = (1, 2, "hi", "hey", 8, 10)
lis = list(f)
print(lis)
