# Write a program to find a minimum of two numbers.
n1 = int(input("Enter first number = "))
n2 = int(input("Enter second number = "))

if(n1<n2):
    print("{0} is minimum.".format(n1))

elif(n2<n1):
    print("{0} is minimum.".format(n2))
