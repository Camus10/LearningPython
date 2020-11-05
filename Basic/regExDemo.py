import re

# Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("YES! We have a match!")
else:
    print("No match")


# regular expression function
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	    Replaces one or many matches with a string

# metacharacters
# []	A set of characters     "[a-m]"	
# \	    Signals a special sequence (can also be used to escape special characters)      "\d"	
# .	    Any character (except newline character)	"he..o"	
# ^	    Starts with	    "^hello"	
# $	    Ends with	"world$"	
# *	    Zero or more occurrences	"aix*"	
# +	    One or more occurrences	    "aix+"	
# {}	Exactly the specified number of occurrences	    "al{2}"	
# |	    Either or	"falls|stays"	
# ()	Capture and group

# special sequences
# \A	Returns a match if the specified characters are at the beginning of the string      "\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
#       (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain" or r"ain\b"	
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#       (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" or r"ain\B"
# \d	Returns a match where the string contains digits (numbers from 0-9)	    "\d"	
# \D	Returns a match where the string DOES NOT contain digits	"\D"	
# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	    "\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

# sets
# [arn]	        Returns a match where one of the specified characters (a, r, or n) are present	
# [a-n]	        Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	    Returns a match for any character EXCEPT a, r, and n	
# [0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	        Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	    Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string


txt = "The rain in Spain"
a = re.findall("ai", txt)
print(a)
b = re.findall("Portugal", txt)
print(b)
c = re.search("Portugal", txt)
print(c)
d = re.split(r"\s", txt)
print(d)
e = re.split(r"\s", txt, 1)
print(e)
f = re.sub(r"\s", "9", txt)
print(f)
g = re.search("ai", txt)
print(g)    # this will an object
# .span()   returns a tuple containing the start-, and end positions of the match.
# .string   returns the string passed into the function
# .group()  returns the part of the string where there was a match
h = re.search(r"\bS\w+", txt)
print(h.span())
print(x.string)
print(x.group())