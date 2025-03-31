#============================================================#

# Raw and Multiline Strings

#============================================================#

print("\n#" + "="*60 + "#\n", 

      " "*15, "Raw and Multiline Strings",

      "\n#" + "="*60  + "#"
      )

# print("\n\n#" + "="*60  + "#\n") 
# Printed border

#============================================================#

notes = r"""
### Raw Strings (r''' or r^double quotes)

# Raw strings treat backslashes (\) as literal characters, 
# preventing escape sequences.
path = r"C:\Users\NewFolder\file.txt"
print(path)  # Output: C:\Users\NewFolder\file.txt

# Useful in Regular Expressions 
# (avoids double escaping backslashes)
import re
pattern = r"\d{3}-\d{2}-\d{4}"  # Matches formats like 123-45-6789
match = re.findall(pattern, "My SSN is 123-45-6789")
print(match)  # Output: ['123-45-6789']

# Raw strings prevent \n from making a new line
raw_text = r"First Line\nSecond Line"
print(raw_text)  # Output: First Line\nSecond Line


#============================================================#

### Multi-Line Strings (''' or double quotes)

# Multi-line strings span multiple lines, commonly used 
# for documentation (docstrings)
multi_line = '''This is a 
multi-line string.'''
print(multi_line)

# Using triple quotes preserves formatting
formatted_text = '''Line 1
    Indented Line 2
Line 3'''
print(formatted_text)

# Triple quotes can also be used for multi-line comments
'''
This is a multi-line comment.
It won't be executed as code.
'''


#============================================================#

### Raw Multi-Line Strings (Combining Both Features)

# A raw multi-line string keeps both formatting and literal 
# backslashes

raw_multi = r'''C:\NewFolder
Backslash \n won't create a new line here!'''
print(raw_multi)

"""

print(notes)

#============================================================#

print("\n#" + "="*60 + "#\n", 

      " "*20, "- - - End - - -",

      "\n#" + "="*60  + "#"
      )