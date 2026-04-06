'''s = "python programming"
print(s.capitalize())
print(s.title())
s = s.title()
print(s) 

print(s.replace("on","ON"))
print(s)
'''
#Reverse a string without using Built-in functions & slice
#input : "abc" ==> output : "cba" 

def Reverse_string(s):
    stop = -1 * (len(s) + 1)
    res = ""
    for i in range(-1, stop, -1):
        res += s[i]
    return res 

print(Reverse_string("abc"))


def is_palindrome(s):
    return Reverse_string(s) == s 
print(is_palindrome("abc"))
print(is_palindrome("madam"))

#Anagram
s1 ="paces"
s2 = "space" 
def Anagram(s1,s2):
    pass 
print(Anagram("paces","space")) #True
print(Anagram("abc","aabbcc")) #False 

import collections
print(collections.Counter("aabbcc")) 

def Anagram(s1,s2):
    return collections.Counter(s1) == collections.Counter(s2) 

print(Anagram("paces","space")) #True
print(Anagram("abc","aabbcc")) #False