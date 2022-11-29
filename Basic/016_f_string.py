# PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings 
# (because of the leading f character preceding the string literal). 
# The idea behind f-strings is to make string interpolation simpler. 
# To create an f-string, prefix the string with the letter “ f ”. 
# The string itself can be formatted in much the same way that you would with str.format(). 
# F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.

 
name = 'Rakib'
age = 26
print(f"Hello, My name is {name} and I'm {age} years old.\n\n")



import datetime
 
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")