"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    '''
    from math import *
    
    x = 1
    y = 2
    z = 3
    print("x: {0}, y: {1}, z: {2}".format(x, y, z))
    print("pi: ", pi, "e ", e)
    print("pi: ")
    '''
    '''
print()
infile = open("sample.txt", 'r')
print(infile)

wholeFileText = infile.read()
print(wholeFileText)
wholeFileText = infile.read()
print("*", wholeFileText, "*", sep="")
infile.seek(5)
wholeFileText = infile.read()
print("*", wholeFileText, "*", sep="")
    '''
for line in infile:
    print(line, end="")

    line = infile.readdline()
    while line != "":
        print(line.rstrip())
        line = infile.readline()
        


print()


main()    