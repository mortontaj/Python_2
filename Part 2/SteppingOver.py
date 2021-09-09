number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

# print(separators)

values = "".join(char if char not in separators else" " for char in number).split()
print(sum([int(val) for val in values]))

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

symbil = ""

for cymbol in quote:
    if cymbol.isalpha() and cymbol.isupper():
        symbil = symbil + cymbol

CapitalLetters = "".join(cymbol if cymbol not in symbil else "" for cymbol in symbil).split()

print(symbil)