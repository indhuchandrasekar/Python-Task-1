# Problem 7 : Program That Takes A String And Returns Mpst Frequent Character In It.
my_string = "Indhumathi"

print ("The string is : ")
print(my_string)

max_frequency = {}
for i in my_string:
   if i in max_frequency:
      max_frequency[i] += 1
   else:
      max_frequency[i] = 1
my_result = max(max_frequency, key = max_frequency.get)

print ("The maximum of all characters is : ")
print(my_result)