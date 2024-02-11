# Write a program to check if the given number is Armstrong or not.
num = int(input("Enter number = "))
num_str = str(num)
n = len(num_str)
sum = 0

for i in num_str:
    sum += int(i)**n

if(sum == num):
    print("{0} is armstrong.".format(num))

else:
    print("{0} is not armstrong.".format(num))
    
