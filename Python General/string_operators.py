#============================================================#

# String Operators

#============================================================#

### Header ###

print("\n#" + "="*60 + "#\n", 

      " "*20, "String Operators",

      "\n#" + "="*60  + "#"
      )

# print("\n\n#" + "="*60  + "#\n") 
# Printed border

#============================================================#

### Body Start ###

notes1 = r'''
# String Operators in Python

## Concatenation (+)
# The `+` operator joins two strings together.

str1 = "Hello, "
str2 = "World!"
result = str1 + str2
print(result)  

Output:
'''

print(notes1)

str1 = "Hello, "
str2 = "World!"
result = str1 + str2
print(result)  

print("\n\n#" + "="*60  + "#\n") 
# Printed border


#============================================================#

notes2 = r'''
## Repetition (*)
# The `*` operator repeats a string multiple times.

text = "Ha"
print(text * 3)  

Output:
'''

print(notes2)

text = "Ha"
print(text * 3)  

print("\n\n#" + "="*60  + "#\n") 
# Printed border


#============================================================#

notes3 = r'''
## Membership (`in`) - Checking Characters
# The `in` operator checks if a character is present in a string.

text = "Python"
print("y" in text)  # True
print("z" in text)  # False

Output:
'''

print(notes3)

text = "Python"
print("y" in text)  # True
print("z" in text)  # False

print("\n\n#" + "="*60 + "#\n")  
# Printed border


#============================================================#

notes4 = r'''
## Membership (`in`) - Checking Words in a List
# The `in` operator checks if an item exists in a list.

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
print("grape" in fruits)    # False

Output:
'''

print(notes4)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
print("grape" in fruits)    # False

print("\n\n#" + "="*60 + "#\n")  
# Printed border


#============================================================#

notes5 = r'''
## Membership (`not in`) - Excluding Items
# The `not in` operator checks if an item is NOT present.

sentence = "I love programming"
print("code" not in sentence)  # True
print("love" not in sentence)  # False

Output:
'''

print(notes5)

sentence = "I love programming"
print("code" not in sentence)  # True
print("love" not in sentence)  # False

print("\n\n#" + "="*60 + "#\n")  
# Printed border


### Body End ###

#============================================================#
 
 ### Footer ###

print("\n#" + "="*60 + "#\n", 

      " "*20, "- - - End - - -",

      "\n#" + "="*60  + "#"
      )

### End of File ###

#============================================================#