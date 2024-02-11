# Write a program to find a minimum of three numbers.
n1 = int(input("Enter first number = "))
n2 = int(input("Enter second number = "))
n3 = int(input("Enter third number = "))

if(n1<n2 and n1<n3):
    print("{0} is minimum.".format(n1))
elif(n2<n1 and n2<n3):
    print("{0} is minimum.".format(n2))
elif(n3<n2 and n3<n1):
    print("{0} is minimum.".format(n3))
