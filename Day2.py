# Write a program to find the given number is positive or negative.
num = int(input("Enter number here = "))
if(num < 0):
    print("{0} is Negative".format(num))

elif(num == 0):
    print("{0} is a signed numbers".format(num))

elif(num > 0):
    print("{0} is Positive".format(num))

else:
    print("Not a number")
