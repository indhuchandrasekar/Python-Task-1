# Problem 9 : Program That Takes A String And Returns Number of Words In It.
# to count words in string
# using split()
 
# initializing string
test_string = "Welcome To GUVI"
 
 
# printing original string
print("The original string is : " + test_string)
 
# using split()
# to count words in string
res = test_string.count(" ")+1
 
# printing result
print("The number of words in string are : " + str(res))
