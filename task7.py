# Create a python module with list and import the module in another .py file and change the value in list
list=[1,2,3,4,5,6]
import mymodule
mymodule.list.append(9)
print(mymodule.list)

# Install pandas package (try to import the package in a python file
import pandas as pand
import numpy as nump
import sys
sys.__stdout__ = sys.stdout
nos = nump.array([1, 2, 3, 4])
series1 = pand.Series(nos)
print(series1)

# Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run
import random
print("Random number is", random.randint(1, 100))

# Import sys package and find the python path
import sys
print(sys.path)
