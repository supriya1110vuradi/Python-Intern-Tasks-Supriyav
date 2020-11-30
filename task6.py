# Write a program to loop through a list of numbers and add +2 to every value to elements in list

lst = list([1, 2, 3, 4, 5, 6])
print(lst)
new_lst = [x + 2 for x in lst]
print(new_lst)

# Write a program to get the below pattern
# 54321
# 4321
# 321
# 21
# 1

p = 5
for i in range(p):
    for j in range(p):
        temp = p - j
        print(temp, end="")
    print()
    p -= 1

# Python Program To Print Fibonacci Sequence
a = 0
b = 1
n = 10
sum1 = 0
while sum1 <= n:
    print(sum1)
    a = b
    b = sum1
    sum1 = a + b
    
    
    # Write a code with a function to print armstrong number
Armstrong number is a number that is equivalent to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers. 407 is an Armstrong number.
(4*4*4)+(0*0*0)+(7*7*7)=407

def armstrong(number):
    count = 0
    num = number
    while num != 0:
        num = num % 10
        count += 1
    expo = count
    while num != 0:
        base = num / 10
        tem = 1
        add = 0
        for x in expo:
            tem = tem * base
            add = add + tem

    if add == number:
        print("Armstrong Number")


c = int(input("Enter the no "))
print(armstrong(c))

# Write a program to print the multiplication table of 9

for i in range(11):
    ans = 9 * i
    print(ans)

# Write a program to convert the number of days into ages

ans = int(input("Enter the number of days : "))
a = int(ans / 365)
print("Number of years is :", a)

# Solve Trigonometry problem using math function write a problem to solve using math function

import math

a = math.pi / 6
print("The value of sin pi/6 is :", end="")
print(math.sin(a))

# Create a calculator only on a code level by using if condition

print("This is my first calculator in python")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4. DIVISION")

cal = int(input("Enter the choice you want to enter: 1 to 4 "))

if cal == 1:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    ans = a + b
    print("Addition = ", ans)

elif cal == 2:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    ans = a - b
    print("Subtract = ", ans)

elif cal == 3:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    ans = a * b
    print("Multiply = ", ans)

elif cal == 4:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    ans = a / b
    print("Divide= ", ans)

else:
    print("You have made an invalid choice")
    print("***** BYE *****")
