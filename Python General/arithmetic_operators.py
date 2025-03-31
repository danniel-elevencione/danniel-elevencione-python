#============================================================#

# Arithmetic Operators

#============================================================#

### Header ###

print("\n#", "="*60, "#\n", 

      " "*20, "Arithmetic Operators",

      "\n#", "="*60, "#\n"
      )

#============================================================#

### Start of Body ###

operators = r'''- Arithmetic Operators -
a + b  # Addition
a - b  # Subtraction
a * b  # Multiplication
a / b  # Division (float)
a // b  # Floor Division (integer result)
a % b  # Modulus (remainder)
a ** b  # Exponentiation (power)   Note: right-sided binding

# Root Operations
a ** 0.5  # Square Root
a ** (1/3)  # Cube Root
a ** (1/n)  # nth Root (general formula)

import math
math.sqrt(a)  # Square Root using math module
math.pow(a, 1/n)  # nth Root using math module


#============================================================#

Remember: 
It's possible to formulate the following rules based 
on this result:

- when both ** arguments are integers, 
the result is an integer, too;
- when at least one ** argument is a float, 
the result is a float, too.
# also applicable for multplication, division, floor and modulo


#============================================================#

- List of priorities -
Priority   #Operator
1          # **            (Highest priority)
2          # +, -
3          # *, /, //, %
4          # +, -          (Lowest priority)


#============================================================#

### Round function

The round() function in Python is used to round a number 
to a specified number of decimal places.

round(number, ndigits)

# number → The number to round.
# ndigits (optional) → The number of decimal places to round to.

### Examples
print(round(3.14159))      # 3 (Rounds to the nearest integer) default
print(round(3.14159, 2))   # 3.14 (Rounded to 2 decimal places)
print(round(3.14159, 4))   # 3.1416 (Rounded to 4 decimal places)
print(round(3.5))          # 4 (Rounds up when exactly .5)
print(round(2.5))          # 2 (Rounds to the nearest even number)
'''

print(operators)


### End of Body ###

#============================================================#
 
 ### Footer ###

print("\n#" + "="*60 + "#\n", 

      " "*20, "- - - End - - -",

      "\n#" + "="*60  + "#"
      )

### End of File ###

#============================================================#