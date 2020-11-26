# Write a Python script to merge two Python dictionaries
Won1 = {"Win": "1", "Victory": "2", "Champion": "3"}
Won2 = {"success": "1", "First": "2", "achieve": "3"}
Won1.update(Won2)
print(str(Won1))

# Write a Python program to map two lists into a dictionary
roll = ["1", "2", "3"]
name = ["sup", "shru", "san"]
student = dict(zip(roll, name))
print(student)

# Write a Python program to remove a key from a dictionary
Capitals = {"Maharashtra": "Mumbai", "Goa": "panaji", "Bihar": "Patna"}
print(str(Capitals))
del Capitals['Maharashtra']
print(str(Capitals))

# a Python program to find the length of a set
sup = {"100", "200", "300", "800", "850", "1000"}
print(len(sup))

# Write a Python program to remove the intersection of a 2nd set from the 1st set
set1 = {"100", "200", "300", "400", "600"}
set2 = {"700", "850", "200", "100", "900"}
print(set1)
print(set2)
set1.difference_update(set2)
print(set1)
