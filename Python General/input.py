

#============================================================#

# Input

#============================================================#

print("\n#" + "="*60 + "#\n", 

      " "*25, "Input",

      "\n#" + "="*60  + "#"
      )

# print("\n\n#" + "="*60  + "#\n") 
# Printed border

#============================================================#

notes = r'''
General Format for Input in Python
# variable = input("Prompt message: ")
'''

#============================================================#

notes1 = r'''
# Basic Input Example
name = input("Enter your name: ") 
print("Hello,", name)
'''
print(notes1)
name = input("Enter your name: ") 
print("Hello,", name)

expl = r'''
- Explanation -
input("Enter your name: ") → Asks the user for input.
The entered value is stored in the variable name.
print("Hello,", name) → Prints the value entered by the user.''' 

print(expl)

print("\n\n#" + "="*60  + "#\n") 


#============================================================#

notes2 = r'''
# Integer Input
age = int(input("Enter your age: "))
print("Your age is:", age)
'''
print(notes2)
age = int(input("Enter your age: "))
print("Your age is:", age)

print("\n\n#" + "="*60  + "#\n") 


#============================================================#

notes3 = r'''
# Float Input
decimal = float(input("Enter a decimal number: "))
print("Decimal:, decimal")
'''
print(notes3)
decimal = float(input("Enter a decimal number: "))
print("Decimal:, decimal")

print("\n\n#" + "="*60  + "#\n") 


#============================================================#

notes4 = r'''
# Basic Boolean Input
user_input = input("Enter True or False: ")  
bool_value = user_input == "True"  
print(bool_value)  
'''
print(notes4)
user_input = input("Enter True or False: ")  
bool_value = user_input == "True"  
print(bool_value)  


#============================================================#

print("\n#" + "="*60 + "#\n", 

      " "*20, "- - - End - - -",

      "\n#" + "="*60  + "#"
      )