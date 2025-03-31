#============================================================#

# Input

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
# Pythagorean Theorem

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

Output:
'''

print(notes)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)


### Body End ###

#============================================================#
 
 ### Footer ###

print("\n#" + "="*60 + "#\n", 

      " "*20, "- - - End - - -",

      "\n#" + "="*60  + "#"
      )

### End of File ###

#============================================================#