# write a program using zip() function and list() function ,create a merged list of tuples from the two lists given
lst1 = [1, 6, 5, 4]
lst2 = ['u', 'z', 'x', 'y']
def merge(lst1, lst2):
    merged_list = tuple(zip(lst1, lst2))
    return merged_list
print(merge(lst1, lst2))

# first create a range 1 to 8 the using zip, merge the given list and the range together to create a new list of tuples
lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
list(zip(lst1, lst2))
print(list(zip(lst1, lst2)))
tuple(zip(lst1, lst2))
print(tuple(zip(lst1, lst2)))

# using sorted() function, sort the list in ascending order
lst = [10, 21, 45, 50, 90, 4, 98, 86]
x = sorted(lst)
print("sort in ascending order :", x)

#  write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list 
numbers = [1, 17, 16, 53, 67, 34, 75, 48]
def even_nums(num):
    if(num%2 == 0):
        return True
    else:
        return False
evenNums = filter(even_nums, numbers)
print('Even Numbers are:')
for num in evenNums:
    print(num)
