#============================================================#

# Input: Python Practice 6

#============================================================#

### Header ###

print("\n#" + "="*60 + "#\n", 

      " "*25, "Input",

      "\n#" + "="*60  + "#"
      )

# print("\n\n#" + "="*60  + "#\n") 
# Printed border

#============================================================#

### Body Start ###

notes = r'''
### LAB   Simple input and output

# input a float value for variable a here
# input a float value for variable b here

# output the result of addition here
# output the result of subtraction here
# output the result of multiplication here
# output the result of division here

print("\nThat's all, folks!")

'''

print(notes)

# input a float value for variable a here
a = float(input("Enter float value for variable a: "))

# input a float value for variable b here
b = float(input("Enter float value for variable b: "))


# output the result of addition here
addition = a + b
print("\naddition = a + b")
print("addition = ", a, "+", b)
print("addition =", addition)

# output the result of subtraction here
subtraction = a - b
print("\nsubtraction = a - b")
print("subtraction = ", a, "-", b)
print("subtraction =", subtraction)

# output the result of multiplication here
multiplication = a * b
print("\nmultiplication = a * b")
print("multiplication = ", a, "*", b)
print("multiplication =", multiplication)


# output the result of division here
division = a / b
print("\ndivision = a / b")
print("division = ", a, "/", b)
print("division =", division)

print("\nThat's all, folks!")


### Body End ###

#============================================================#
 
 ### Footer ###

print("\n#" + "="*60 + "#\n", 

      " "*20, "- - - End - - -",

      "\n#" + "="*60  + "#"
      )

### End of File ###

#============================================================#