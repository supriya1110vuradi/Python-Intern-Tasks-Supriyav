# List down all the error types and check all the errors using a py-thon program for all errors
# 1 ZeroDivisionError
a = 10
b = 0
print("Result of Division: " + str(a/b))

# 2  IndentationError
for i in range(10):
print('Hello world')

# 3 Type Error
a = 2
b = 'Hello'
a + b

# 4 OverFlow Error
try:
    import math
    print(math.exp(1000))
except OverflowError:
        print ("OverFlow Exception Raised.")
else:
    print ("Success, no error!")

# 5 Assertion Error
try:
    a = 100
    b = "Hey"
    assert a == b
except AssertionError:
        print ("Assertion Exception Raised.")
else:
    print ("Success, no error!")

# 6 Index error
try:
    a = ['a', 'b', 'c']
    print (a[4])
except LookupError:
    print ("Index Error Exception Raised, list index out of range")
else:
    print ("Success, no error!")

# Design a simple calculator app with try and except for all use cases
print("add:")
def addition(num1,num2):
	try:
		result=num1+num2
		print(result)
	except Exception as e:
		print(e)
addition(6,3)

print("subtract:")
def subtract(num1,num2):
	try:
		result=num1-num2
		print(result)
	except Exception as e:
		print(e)
subtract(8,4)

print("divide:")
def divide(num1,num2):
	try:
		result=num1/num2
		print(result)
	except Exception as e:
		print(e)
divide(12,2)

print("multiply:")
def multiply(num1,num2):
	try:
		result=num1*num2
		print(result)
	except Exception as e:
		print(e)
multiply(8,5)

# print one message if the try block raises a NameError and another for other errors
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something went wrong")

variable
x is not defined
>> > try:
    a = 3
    b = '0'
    print(a + b)
except TypeError:
    print('operation is not supported')
except:
    print("out of try except blocks")

operation is not supported
>> > try:
    a = 3
    b = '0'
    print(a + b)
except TypeError:
    print('operation is not supported')
except ZeroDivisionError:
    print('division by zero is not defined')
except:
    print('out of try except blocks')

operation is not supported

# the try catch block
try:
    a = int(input("enter A:"))
    b = int(input("enter B:"))
    c = a / b
except:
    print("cannot be defined")

enter
A: 7
enter
B: 0
cannot be defined