# Check to see if a substring exists between the two strings
# Substring can be a single character
# ---
# Originally implimented using two "x in y" loops, but was too slow

def twoStrings(s1, s2):

    for i in range(len(s1)):
        if s1[i] in s2:
            return "YES"

    return "NO"