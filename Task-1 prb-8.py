'''
Problem 5: Program That Takes A String And Returns True If Its a Anagram of another String, False Otherwise

'''
# function to check if two strings are
# anagram or not 
def check(s1, s2):
     
    # the sorted strings are checked 
    if(sorted(s1)== sorted(s2)):
        print("True The strings are anagrams.") 
    else:
        print("False The strings aren't anagrams.")         
         
# driver code  
s1 ="listen"
s2 ="silent"
check(s1, s2)

