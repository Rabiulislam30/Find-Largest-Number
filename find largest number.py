#Python program to find out largest number among the three input numbers

#take the values of num1, num2, num3
#for a diffrent result

num1 = 20
num2 = 30
num3 = 40

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if(num1 >= num2) and (num1 >= num3):
    largest = num1

elif (num2 >= num1) and (num2 >= num3):
    larhest = num2

else:
    largest = num3

print("The largest number is", largest)
