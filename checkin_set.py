"""
Can we have a set having 18 as integer and "18" as string and 18.0 as bool.
check its length.
"""

from re import S


a = {18,"18",18.0}
print(a) # We will get {18,"18"} and 18.0 will be removed as it is equivalent to 18.
print(len(a))