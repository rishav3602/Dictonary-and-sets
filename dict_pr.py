"""
Create an empty dictonary and allow your four friends to enter their favourite language 
as the value and their names as corresponding keywords.
What happen if language of two friends are same ?
What happen if the name of two of the friends are same ?
"""
fav_lang = {}
a = input("Enter your favourite language Ujjwal : ")
b = input("Enter your favourite language Preet : ")
c  = input("Enter your favourite language Mohan : ")
d = input("Enter your favourite language Navya : ")
fav_lang ['Ujjwal']= a
fav_lang ['Preet'] = b 
fav_lang ['Mohan'] = c 
fav_lang ['Navya'] = d
print(fav_lang)

# If the language of two friends are same then their will be no change as in real dictonary 
# two words can have same meaning .


# If the name of two of the friends are same then the dictonary will update itself to the 
# later value we will give in the dictonary .

