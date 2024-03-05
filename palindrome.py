string  = input("Enter the string : ")
rev = ""
for ind in range(-1,-(len(string)+1), -1):
    rev+= string[ind]
if rev == string:
    print("palindrome")
else:
    print("not a palindrome")
