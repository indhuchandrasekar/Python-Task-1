'''
Problem 5: Program That Takes A String And Returns True If Its a Palindrome, False Otherwise

'''
# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "radar"
result = isPalindrome(s)

if result:
	print("True")
else:
	print("False")

