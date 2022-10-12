"""
Can you change the  value inside the list contained in the set s
s = {8,7,12,"Rishav,[1,2]}
"""

s = {8,7,12,"Rishav",[1,2]}
s[2]= 3
print(s) # this will show this (TypeError: unhashable type: 'list')