# Python program that takes a string that returns a new string with all the vowels removed.
# Function to remove vowels 
  
# import the module for regular expression (re) 
import re 
def rem_vowel(string): 
    return (re.sub("[aeiouAEIOU]","",string))             
  
# Driver program 
string = "Hello World!"
print(rem_vowel(string))
