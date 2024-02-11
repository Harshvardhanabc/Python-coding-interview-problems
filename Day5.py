# Write a program to check if the given number is palindrome or not
num = input("Enter number = ")
r_num = str(num)[::-1]
if(num == r_num):
    print("Number is palindrome")
else:
    print("Number is not palindrome")
