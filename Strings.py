s="You are awesome"
print(s)
multiline_string="""This is an
example of multiline
string"""
print(multiline_string)
print(multiline_string[0])
print(s*2)
print(len(s))

#To use double/single quotes with in a sting use escape characters
#  \\ To include a backlash in a string
# \" To include a double quote in a string
# \' To include a single quote in a string
# \n To include new line in  a string
d_quote="This is string with double \" quote"
print(d_quote)
s_quote="This is string with single \' quote"
print(s_quote)
b_string="This is a string with a \\ backlash"
print(b_string)
l_string="This is a string with a \nnew line"
print(l_string)

#Formatted  String
first="This is a"
second="formatted string"
f_string=f"His first name is {first} & his last name is {second}"
print(f_string)

# Slicing of a string
# s[start index: end index ] where end index is not included
# if end index  is not provided it will go till end
# if starting index is not provide it will begin from very beginning
print(s[-1])
print(s[0])
print(s[0:5])
print(s[5:])
print(s[:5])
print(s[:])
print(s[-3:-1])

#Steps in a given string
#s[start index: end index: step size]
#s[start,stop,step]
print(s[0:10:2])

#To reverse a string give step value as -1 then s[stop:start:-1]
print(s[::-1])
print(s[15::-1])

# To remove spaces from beginning and end of string use strip function
# To remove spaces from left side of the string use lstrip function
# To remove spaces from right side of the string use rstrip function
s2="  This is a string for strip function  "
print(s2)
print(s2.strip())
print(s2.lstrip())
print(s2.rstrip())

# To find a substring in a given string use find method it will
# return the beginning index of that substring we can also pass
# starting index and end index as where we want to find the substring by default it will accept
print(s.find("awe"))

#if find method is not able to find given sub string with in given lengths it returns -1
print(s.find("awe",7,10))

# alternate way of find method is in keyword
print("awe" in s)

# count method will count the occurrence of a given substring
print(s.count("a"))
print(s.count("z"))

#Replace method will replace substring with another substring
print(s.replace("awesome", "super"))
print(s)
print(len(s))

#Upper will make all characters upper case
#Lower will make all characters lower case
#Title will make all characters after space upper case
print(s.upper())
print(s.lower())
print(s.title())