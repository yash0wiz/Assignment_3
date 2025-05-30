#Task 1: Calculate Factorial Using a Function 
#Problem Statement: Write a Python program that:
#1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
#2.   Returns the calculated factorial.
#3.   Calls the function with a sample number and prints the output.
 

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

num=int(input("Enter a number: "))
result = fact(num)
print("Factorial of  ",num," is : ", result)


