# Write a program to find if the given number is prime or not
n = int(input("Enter number = "))

for i in range(0,1,n+1):
    result = i%n
    if(result == 0):
        print("Number is prime")

    else:
        print("Number is not prime")
