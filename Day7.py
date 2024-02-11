# Write a program to check if the given strings are anagram or not.
S1 = input("Enter = ")
S2 = input("Enter = ")

C1 = sorted(S1)
C2 = sorted(S2)

if(C1 == C2):
    print("Is Anagram")

else:
    print("Is not Anagram")
