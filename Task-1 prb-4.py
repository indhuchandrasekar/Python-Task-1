# Python program that take a string returns number of unique character in it.
 
# Function to count the number of distinct
# characters present in the string str
 
 
def countDis(str):
 
    # Stores all distinct characters
    s = set(str)
 
    # Return the size of the set
    return len(s)
 
 
# Driver Code
if __name__ == "__main__":
 
    # Given string S
    S = "geeksforgeeks"
 
    print(countDis(S))
    
