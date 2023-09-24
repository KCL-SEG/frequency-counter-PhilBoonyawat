"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if frequencies.get(str(item)) != None:
            frequencies[str(item)] = frequencies[str(item)] + 1 
        else:
            frequencies[str(item)] = 1

    return frequencies

print(frequencies([1,1,1,1,4,2,3]))