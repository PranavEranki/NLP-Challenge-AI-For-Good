# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:20:08 2019

@author: Hair Albeiro Parra Barrera
"""

### Regular Expressions ### 

# regex are a powerful tool for string manipulation
# They are domain specific langauge (DSL) that is present as a library 
# in most languages. They are useful for : 
# - verifying that strings match a pattern
# - performing substitutions in a string

# DSL are highly specicalized mini programming languages. 

## Regular expressions 

# Can be accessed using the re module, re.function 
# to avoid confusion with strings, we use r"expression" 

import re # regex module

pattern = r"spam" 

if re.match(pattern, "spamspamspam") :
    print("Match")
else:
    print("No match")
    
# Other functionss: 
    # re.match : determines whether the pattern matches at the beginning of the string
    # re.search finds a match of a pattern anywhere in the string
    # re.findall returns a list of all substrings that match a pattern 
    
if re.match(pattern, "eggsspamsausage"): # no match: at the beginning of the string
    print("Match")
else:
    print("No match")
    
if re.search(pattern, "eggspamsausagespam"): # match:  position doesn't matter
    print("Match")
else:
    print("No match")
    
print(re.findall(pattern, "eggspamsausagespam")) # outpus array of all substrings with matches
# note that re.finditer does the same as re.findall, but it returns an iterator
# can add len to find how many ocurrences
num_occ = len(re.findall(pattern, "eggsspamspamsausageeggspam")) # 3
print(num_occ)

import re 

pattern = r"spa" 
if re.match(pattern, "eggsspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern,"eggsspamsausagespam" ): 
    print("Match")
else: 
    print("No match")
    
# Using the re.finditer we can also find where the substring was found 
for x in re.finditer(pattern,"eggsspamsausagespam"):
    print(x)
    print(x.group())
    print(x.start())
    print(x.end())
    print(x.span())
    R ="span="
    y = re.search(R,str(x))
    print(y)
    print(y.group())
    print(y.start())
    print(y.end())
    print(y.span())
    print("----------------")
    
## Regex
    
# The regex search returns an object with several methods that give details 
# group, start, end, span 
    
pattern = r"spam" 

match = re.search(pattern,"eggs spamish sausage spam")
if match: 
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
    
    
## Search and Replace
    
# re.sub(pattern, repl, srting, max=0)
# replaces all occurrences of the pattern in string with repl, 
# substituing all ocurrences, unless max is provided. 
# returns a String
    
import re

str1 = "My name is David. Hi David"
pattern = r"David"
newstr = re.sub(pattern, "Amy", str1)
print(newstr)

### Metacharaters 

# mak regex more powerful than normal stirng methods
# for special characters you can backslash
# t avoid \\\\\, use a raw string, ie r"string"

import re

pattern = r"gr.y" # the "." means any character

if re.match(pattern, "grey"): # match
    print("Match 1")
    
if re.match(pattern, "gray"): # match
    print("Match 2")
    
if re.match(pattern, "blue"): # no match
    print("Match 3")
    
# more matacharacters: 
    # ^ and $: these match the start and the end of the string
    
import re

pattern = r"^gr.y$" # must start with gr, followed by anything, must end with y

if re.match(pattern, "grey"): # match
    print("Match 1")
    
if re.match(pattern, "gray"): # match
    print("Match 2")
    
if re.match(pattern, "stingray"): # no match
    print("Match 3")
    
# note that the ^ can also be used at the beginning of the string

## Character Classes 
    
# provide a way to match only one of a specific set of characters
# inside square brackets

import re

pattern = r"[aeiou]" # anything inside the brackets good

if re.search(pattern, "grey"):
    print("Match 1")
    
if re.search(pattern, "qwertyuiop"):
    print("Match2")
    
if re.search(pattern, "rhythm myths"):
    print("Match 3") # this one will not match 
    
# Character classes can also match ranges of stuff
    
import re 

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"): # only this one will be identified 
    print("Match 1")
    
if re.search(pattern, "E3"):
    print("Match 2")
    
if re.search(pattern, "1ab"):
    print("Match 3")
    
# place a ^ at the start of a character class to invert it 
# this causes it to match any character other than the ones included
    
import re 

pattern = r"[^A-Z]" # anything except between A and Z 

if re.search(pattern, "this is all quiet"): 
    print("Match 1")

if re.search(pattern, "AbCdEfG123"): 
    print("Match 2")
    
if re.search(pattern, "THISISALLSHOUTING"): # this one will obviously no tmatch 
    print("Match 3")
    
## More Metacharacters
    
# some are *,+,? {and}. These specify numbers of repetitions. 
# * means "zero or more repetitions of the previous things" 
# tries to match as many repetitions as possible. 
# previous thing can be a single character, a class, or group of characters (abs)
    
import re

pattern = r"egg(spam)*" # matches egg followd by any # of repetitions of (spam) *

if re.match(pattern, "egg"): 
    print("Match 1")
    
if re.match(pattern, "eggspamspamegg"):
    print("Match 2")
    
if re.match(pattern, "spam"):
    print("Match 3")
    
    
# "+" similar to "*", but it means one or more repetitions
    
import re 

pattern = r"g+" # at least one repetition of g

if re.match(pattern, "g"): 
    print("Match 1")
    
if re.match(pattern, "ggggggggggg"):
    print("Match 2")
    
if re.match(pattern, "abc"): # will not match
    print("Match 3")
    
# note that "(something)+" === "something(something)*" 
    
#"(something)?" means zero or one repetitions 
    
import re 

pattern = r"ice(-)?cream" # the - is optional 

if re.match(pattern, "ice-cream"): # matches
    print("Match 1")
    
if re.match(pattern, "icecream"): # matches
    print("Match 2")
    
if re.match(pattern, "sausages"): # will not match
    print("Match 3")
    
if re.match(pattern, "ice--cream"): # will not match
    print("Match 4")
    
# Curly Braces: {} : user to represent the number of repetitions between 
# two numbers , ie {x,y} 
# Hence, {0,1} == "?" import re 

pattern = r"9{1,3}$" # matches 1 to 3 repetitions of 9, at the end 

if re.match(pattern, "9"): # matches
    print("Match 1")
    
if re.match(pattern, "999"): # matches
    print("Match 2")
    
if re.match(pattern, "9999"): # will not match (4 repetitions!)
    print("Match 3")
    
    
## Groups 
    
# Can be created by parentheses and addes argument ot methacharacters
    
import re

pattern = r"egg(spam)*" # matches egg followd by any number of repetitons of spam


if re.match(pattern, "egg"): # matches
    print("Match 1")
    
if re.match(pattern, "eggspamspamegg"): # matches
    print("Match 2")
    
if re.match(pattern, "spam"): # will not match
    print("Match 3")
    
# the content of groups in a amtch can be accessed using the group function
# group(0) or group() : returns the whole match 
# group(n) returns the nth group from the left 
# groups() returns all groups up from 1

import re

pattern = r"a(bc)(de)(f(g)h)i" 

match = re.match(pattern, "abcdefghijklmnop")
if match: 
    print(match.group()) # full match 
    print(match.group(0)) # full match 
    print(match.group(1)) # first match 
    print(match.group(2)) # second match 
    print(match.groups()) # sequence of matches 
    
pattern  = r"egg(spam)(pearl)(huri)" 

match = re.match(pattern, "eggspampearlhuriTTT" )
if match: 
    print(match.group(0))
    print(match.group())
    
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    
    print(match.groups()) # all groups! 
    
## Special Groups!! 
    
# Named Groups: 
# have the format (?P<name>...) where name is the name of the group,
# and ... is the content. They behave exactly as normal groups, 
# except that they can be accessed by group(name) in addition 
# to its number 

    
# Non-capturing groups: 
# have the format (?:...). They are not accessible by the group method, 
# so they can be added to an existing regular expression without 
# breaking the numbering. 
    
import re

# named group followed by a non-capturing groups
pattern  = r"(?P<first>abc)(?:def)(ghi)" # def will not match

match = re.match(pattern, "abcdefghi")
if match: 
    print(match.group("first")) # match (abc)
    print(match.groups()) # (def) will not appear


# ex: 
import re

pattern = r"(a)(b(?:c)(d)(?:e))" 
pattern1 = r"(a)(b(c)(d)(e))" 
match = re.match(pattern, "abcde") #('a','bcde','d')
match2 = re.match(pattern1,"abcde") #

if match:
    print(match.groups())
    print(len(match.groups()))
    print(match.groups())
    print(len(match.groups()))
    # smae result for voth above 
    
# the "|" character means "or"
    
import re

pattern = r"gr(a|e)y*" # matches either a or e 


if re.match(pattern, "gray"): # matches
    print("Match 1")
    
if re.match(pattern, "grey"): # matches
    print("Match 2")
    
if re.match(pattern, "griy"): # will not match
    print("Match 3")
    
    
## Special Sequences
    
# Various special sequences with backslash 
# This matches the expresion of the group of that number 
    
import re 

# at least one repetition of any character + a repetition of what's found in group 1
pattern = r"(.+) \1"  

match =  re.match(pattern, "word word") # note the space also counts! 
if match:
    print("Match 1")
    
match = re.match(pattern, "?! ?!") # matches
if match: 
    print("Match 2")
    
match  = re.match(pattern, "abccde") # doesn't match
if match:
    print("Match 3")
    
# More useful special sequences are
# \d matches digits == [0-9]
# \s whitespace == [\t\n\r\f\v]
# \w characters == [a-zA-Z0-9_]

# In Unicode mode they match other charcters: 
# for instanc,e \w matches characters with accents 

# uppercase \D, \S , \W mean the opposite!!! 
# ex. \D matches anything that isn't a digit

    
import re 

pattern = r"(\D+\d)" #at least one non-digit and a digit

match =  re.match(pattern, "Hi999") # matches
if match:
    print("Match 1")
    
match = re.match(pattern, "1, 23, 456!") # no match
if match: 
    print("Match 2")
    
match  = re.match(pattern, " !$?") # doesn't match
if match:
    print("Match 3")
    

# \A and \Z match the beginning and ned of string resp. 
# \b matches the empty string between \w and \W characters, 
# or \w characters at the beginning or end of the string
# Informally, boundary between two words
# \B matches the empty string anywhere else 

import re 

pattern = r"\b(cat)\b" # matches "cat" surrounded by word boundaries

match =  re.search(pattern, "The cat sat!") # matches
if match:
    print("Match 1")
    
match = re.search(pattern, "We s>cat<ered?") # no match
if match: 
    print("Match 2")
    
match  = re.search(pattern, " We scattered") # doesn't match
if match:
    print("Match 3")

