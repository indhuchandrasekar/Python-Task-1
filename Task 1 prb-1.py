'''
Problem 1: Python program to count total number of vowels and count each of individual vowels in "Guvi Geeks Network Private Limited"?
'''
def Check_Vow(string, vowels):

    # The term "casefold" has been used to refer to a method of ignoring cases.

    string = string.casefold()

    count = {}.fromkeys(vowels, 0)

    # To count the vowels

    for character in string:

        if character in count:

            count[character] += 1   

    return count

# Driver Code

vowels = 'aeiou'

string = "Guvi Geeks Network Private Limited"

count = sum(string.count(vowel) for vowel in vowels)
print(count)
print (Check_Vow(string, vowels))


