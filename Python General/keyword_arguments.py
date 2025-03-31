# Basic Keyword Arguments

print("Basic Keyword Arguments")

print("\nMy name is", "Danniel.")
print("Danniel 11\n")
# print in newline

print("My name is", "Danniel.", end=" ")
print("Danniel 11\n")
# put space instead of newline

print("My name is", "Danniel.", end="")
print("Danniel 11\n")
# no space no newline

print("My", "name", "is", "Danniel.", sep="-")
# put dash between arguments


# Practice
# Expected output: Programming***Essentials***in...Python

print("Programming", "Essentials", "in", sep="***", end="...")
print("Python\n")


# ============================================================ #


# Formatting the output
try_task = r'''

Try to:

Reduce print() calls by using \n in strings.

Double the arrow size while maintaining proportions.

Duplicate the arrow side by side by using "string" * 2.

Remove quotes and observe Python's response to locate errors.

Experiment with parentheses and check if errors arise there.

Change print to variations like Print and observe the result.

Replace quotes with apostrophes and see what happens.

'''

print (try_task)


'''
Code:

print("    *")      #1
print("   * *")     #2
print("  *   *")    #3
print(" *     *")   #4
print("***   ***")  #5
print("  *   *")    #6
print("  *   *")    #7
print("  *****\n")  #8

'''

# ============================================================ #

print("\nFirst Version\n")

print(" "*3,   "*\n",              #1
      " ",     "*",       "*\n",   #2
      "",      "*", " "  , "*\n",  #3
               "*", " "*3, "*",    #4
      "\n***", " ", "***\n",       #5
      "", "*", " ", "*\n",         #6
      "", "*", " ", "*\n",         #7
      "",      "*"*5, "\n"         #8
      ) 

# ============================================================ #

print("\n\nSecond Version\n")

print("", "*", "", sep=" "*4)
print("", "* *", "", sep=" "*3)
print("", "*   *", "", sep=" "*2)
print("", "*     *", "", sep=" "*1)
print("***", "***", sep=" "*3)
print("", "*   *", "", sep=" "*2)
print("", "*   *", "", sep=" "*2)
print("", "*****", "", sep=" "*2)

# ============================================================ #

print("\n\nSide by Side Version\n")

print("", "*", "", sep=" "*4, end="")
print("", "*", "", sep=" "*4)
print("", "* *", "", sep=" "*3, end="")
print("", "* *", "", sep=" "*3)
print("", "*   *", "", sep=" "*2, end="")
print("", "*   *", "", sep=" "*2)
print("", "*     *", "", sep=" "*1, end="")
print("", "*     *", "", sep=" "*1)
print("***", "***", sep=" "*3, end="")
print("***", "***", sep=" "*3)
print("", "*   *", "", sep=" "*2, end="")
print("", "*   *", "", sep=" "*2)
print("", "*   *", "", sep=" "*2, end="")
print("", "*   *", "", sep=" "*2)
print("", "*****", "", sep=" "*2, end="")
print("", "*****", "", sep=" "*2)

# ============================================================ #

print("\n\nEnlarge Version\n")

print("\n", "*", "", sep=" "*8)
print("\n", "*   *", "", sep=" "*6)
print("\n", "*       *", "", sep=" "*4)
print("\n", "*           *", "", sep=" "*2)
print("\n* * *", "* * *", sep=" "*7)
print("\n", "*       *", "", sep=" "*4)
print("\n", "*       *", "", sep=" "*4)
print("\n", "* * * * *", "", sep=" "*4)

