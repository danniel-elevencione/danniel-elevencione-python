#============================================================#

# Variables

#============================================================#

print("\n#" + "="*60 + "#\n", 

      " "*25, "Variables",

      "\n#" + "="*60  + "#"
      )


notes = r'''
### Variables – Data Containers ###
Python allows storing values (numbers, text) in 
variables—named containers for data.

Each variable has:

- A name (chosen by the programmer)

- A value (the stored data)



#============================================================#

Variable names must:

- Use letters (A-Z, a-z), digits (0-9), and underscores (_)

- Start with a letter (underscore is considered a letter)

- Be case-sensitive (alice ≠ ALICE)

- Avoid Python keywords (reserved words)



#============================================================#

Sample usage:
var = 11
account_balance = 1E10
client_name = 'Danniel'
print(var, account_balance, client_name)
print(var)

'''

print(notes)

print("Code Output:")

var = 11
account_balance = 1E6
client_name = 'Danniel'
print(var, account_balance, client_name)
print(var, "\n")


notes2 = r'''
#============================================================#

- How to assign a new value to an 
already existing variable

You can assign a new value to an existing variable using 
the = operator.

The = operator assigns the right-hand value to the left-hand 
variable, which can be an expression involving literals, 
operators, or other variables.

var = 1
print(var)
var = var + 1
print(var)

'''

print(notes2)

#============================================================#

print("\n#" + "="*60  + "#\n", 
      "\nSolving simple mathematical problems")

notes3 = r'''
a = 3.0
b = 4.0 
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

'''

print(notes3)

a = 3.0
b = 4.0 
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
      
print("\n\n#" + "="*60  + "#\n")

#============================================================#

notes4 = r'''
### Scenario
#John has 3 apples, Mary has 5, and Adam has 6.  

### Your Task:

1. Create variables `john`, `mary`, and `adam`, assigning their 
apple counts.  
2. Print all three variables on one line, separated by commas.  
3. Create `total_apples` as the sum of their apples.  
4. Print `total_apples`.  
5. Experiment by creating new variables, performing arithmetic 
operations, and printing strings with numbers.

#============================================================#

Code:

john = 3
mary = 5 
adam = 6

print("John =", john, "Mary =", mary, "Adam =", adam)

total_apples = john + mary + adam

print("Total apples =", total_apples)


#============================================================#
'''

print(notes4)

john = 3
mary = 5 
adam = 6

print("Output:\n", "John =", john, "Mary =", mary, 
      "Adam =", adam)

total_apples = john + mary + adam

print("Total apples =", total_apples, "\n")



notes5 = r'''
#============================================================#

### Shortcut operators

Expression              |  Shortcut operator
i = i + 2 * j           |  i += 2 * j
var = var/2             |  var /= 2
rem = rem % 10          |  rem %= 10
j = j - (i + var + rem) |  j -= (i + var + rem)
x = x ** 2              |  x **= 2


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

print(notes5)

#============================================================#

print("\n#" + "="*60 + "#\n", 

      " "*20, "- - - End - - -",

      "\n#" + "="*60  + "#"
      )