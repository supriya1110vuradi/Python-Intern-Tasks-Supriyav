# Create a function getting two integer inputs from user.& print the following:

# Addition of two numbers is +value
# Subtraction of two numbers is +value
# Division of two numbers is +value
# Multiplication of two numbers is +value

m = int(input("enter first value:"))
n = int(input("enter second value:"))


def my_fun(x, y):

    print("Add of 2 values:", x + y)
    print("Sub of 2 values:", x - y)
    print("Div of 2 values:", x / y)
    print("Mul of 2 values:", x * y)


my_fun(m, n)

# Create a function covid( )& it should accept patient name, and body temperature,
# by default the body temperature should be 98 degree


def covid(patient_name, body_temperature): print("details:"+patient_name+","+body_temperature)


covid("Dhoni", "98 degree")

