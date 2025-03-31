#============================================================#

# Input: Python Practice 8

#============================================================#

### Header ###

print("\n#" + "="*60 + "#\n", 

      " "*15, "Input: Python Practice 8",

      "\n#" + "="*60  + "#"
      )

# print("\n\n#" + "="*60  + "#\n") 
# Printed border

#============================================================#

### Body Start ###

notes = r'''
### Operators and expressions – 2

### Scenario
Your task is to prepare a simple code able to evaluate 
the end time of a period of time, given as a number of minutes 
(it could be arbitrarily large). The start time is given as a 
pair of hours (0..23) and minutes (0..59). The result has to be
printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, 
it will end at 13:16.

Don't worry about any imperfections in your code ‒ it's okay 
if it accepts an invalid time ‒ the most important thing is
that the code produces valid results for valid input data.

Test your code carefully. Hint: using the % operator may be 
the key to success.

### Test Data
- Sample input:
12          
17
59

- Expected output:
13:16

- Sample input:
23
58
642

- Expected output:
10:40

- Sample input:
0
1
2939

- Expected output:
1:0

#============================================================#

### Code:

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hr_min = hour * 60      # hoursto minute conversion
total_min = hr_min + mins + dura    #minutes in total

end_min = total_min % 60
end_hr = int(((total_min - end_min) / 60) % 24)

print("End Time: ", end_hr, ":", end_min, sep = "")


#============================================================#

### Output:
'''

print(notes)

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hr_min = hour * 60      # hoursto minute conversion
total_min = hr_min + mins + dura    #minutes in total

end_min = total_min % 60
end_hr = int(((total_min - end_min) / 60) % 24)

print("End Time: ", end_hr, ":", end_min, sep = "")


### Body End ###

#============================================================#
 
### Footer ###

print("\n#" + "="*60 + "#\n", 

      " "*20, "- - - End - - -",

      "\n#" + "="*60  + "#"
      )

### End of File ###

#============================================================#