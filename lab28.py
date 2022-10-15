def palindrome(s):
    return s==s[::-1]
s=input("enter a string:")
if palindrome(s):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
