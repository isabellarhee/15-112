#strings

#---------------Lecture Notes-------------------------
s = "a\tdef"
print(s)
print(repr(s)) #prints like the full thing w the \t

#multiline comment
'''
this is a multiline comment
actually a multiline string but the program ignores it
'''
for c in s:
    print(c)  #use this to print individual chars

#-----------------------------------------------------------------
#quotes
# Quotes enclose characters to tell Python "this is a string!"
# single-quoted or double-quoted strings are the most common
print('single-quotes')
print("double-quotes")

# triple-quoted strings are less common (though see next section for a typical use)
print('''triple single-quotes''')
print("""triple double-quotes""")

#new lines in strings
# A character preceded by a backslash, like \n, is an 'escape sequence'.
# Even though it looks like two characters, Python treats it as one special character.

# Note that these two print statements do the same thing!
print("abc\ndef")  # \n is a single newline character.
print("""abc
def""")

print("""\
You can use a backslash at the end of a line in a string to exclude
the newline after it. This should almost never be used, but one good
use of it is in this example, at the start of a multi-line string, so
the whole string can be entered with the same indentation (none, that is).
""")

#more escape sequences
print("Double-quote: \"")
print("Backslash: \\")
print("Newline (in brackets): [\n]")
print("Tab (in brackets): [\t]")

print("These items are tab-delimited, 3-per-line:")
print("abc\tdef\tg\nhi\tj\\\tk\n---")
#An escape sequence produces a single character:
s = "a\\b\"c\td"
print("s =", s)
print("len(s) =", len(s)) 

#repr() vs print()
#print() is meant to produce output intended for the user, repr() shows us a representation of the data contained in the string.
#useful for debugging


# STRING CONSTANTS
import string
print(string.ascii_letters)   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print("-----------")
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)          # 0123456789
print("-----------")
print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.printable)       # digits + letters + punctuation + whitespace
print("-----------")
print(string.whitespace)      # space + tab + linefeed + return + ...

#string operators
print("abc" + "def")  # What do you think this should do?
print("abc" * 3)  # How many characters do you think this prints?
#print("abc" + 3)  # ...will this give us an error? (Yes)

#the in operator
# The "in" operator is really really useful!
print("ring" in "strings")
print("wow" in "amazing!")
print("Yes" in "yes!")
print("" in "No way!")

#negative indexes start from back of string 
# ie. s = hello   s[-1] = o
#Slicing:
# Slicing is like indexing, but it lets us get more than 1 character.
# ...how is this like range(a,b)? #
s = "abcdefgh"
print(s) #start inclusive, end exclusive
print(s[0:3])
print(s[1:3])
#Slicing with default parameters
s = "abcdefgh"
print(s)
print(s[3:])
print(s[:3])
print(s[:])
#Slicing with a step parameter
print("This is not as common, but perfectly ok.")
s = "abcdefgh"
print(s)
print(s[1:7:2])

#Reversing a string
s = "abcdefgh"

print("This works, but is confusing:")
print(s[::-1])

print("This also works, but is still confusing:")
print("".join(reversed(s)))

print("Best way: write your own reverseString() function:")
def reverseString(s):
    return s[::-1]

print(reverseString(s)) # crystal clear!

#Looping over Strings
#"for" loop with indexes
s = "abcd"
for i in range(len(s)):
    print(i, s[i])
#or
s = "abcd"
for c in s:
    print(c)

#"for" loop with split
# By itself, names.split(",") produces something called a list.
# Until we learn about lists (soon!), do not store the result of
# split() and do not index into that result.  Just loop over the
# result, as shown here:

names = "fred,wilma,betty,barney"
for name in names.split(","):
    print(name) #prints each name on a sep line

#"for" loop with splitlines
# splitlines() also makes a list, so only loop over its results,
# just like split():

# quotes from brainyquote.com
quotes = """\
Dijkstra: Simplicity is prerequisite for reliability.
Knuth: If you optimize everything, you will always be unhappy.
Dijkstra: Perfecting oneself is as much unlearning as it is learning.
Knuth: Beware of bugs in the above code; I have only proved it correct, not tried it.
Dijkstra: Computer science is no more about computers than astronomy is about telescopes.
"""
for line in quotes.splitlines():
    if (line.startswith("Knuth")):
        print(line)

#--------------------------------EXAMPLE IS PALINDROME-----------------------------
# There are many ways to write isPalindrome(s)
# Here are several.  Which way is best?

def reverseString(s):
    return s[::-1]

def isPalindrome1(s):
    return (s == reverseString(s))

def isPalindrome2(s):
    for i in range(len(s)):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True

def isPalindrome3(s):
    for i in range(len(s)):
        if (s[i] != s[-1-i]):
            return False
    return True

def isPalindrome4(s):
    while (len(s) > 1):
        if (s[0] != s[-1]):
            return False
        s = s[1:-1]
    return True
#----------------------------------------------------------------
#you cant change strings!
# cant do s[2] = "z"
#instead you must create a new string
#ex
s = "abcde"
s = s[:2] + "z" + s[3:]
print(s)
#this means aliases do not change if you change the one it originally was pointing to

#Some String-related Built-In Functions
# str() -> casts to string, len() -> gives length of string
#ord() and chr()
print(ord("A")) # 65
print(chr(65))  # "A"
#eval()
# eval() works but you should not use it!
s = "(3**2 + 4**2)**0.5"
print(eval(s))

# some string methods
# Run this code to see a table of isX() behaviors
def p(test):
    print("True     " if test else "False    ", end="")
def printRow(s):
    print(" " + s + "  ", end="")
    p(s.isalnum())  #alphabetic or numerical
    p(s.isalpha()) #alphabetic
    p(s.isdigit()) #numerical
    p(s.islower()) #lowercase
    p(s.isspace()) #any type of space
    p(s.isupper()) #uppercase
    print()
def printTable():
    print("  s   isalnum  isalpha  isdigit  islower  isspace  isupper")
    for s in "ABCD,ABcd,abcd,ab12,1234,    ,AB?!".split(","):
        printRow(s)
printTable()

#string edits
print("This is nice. Yes!".lower())
print("So is this? Sure!!".upper())
print("   Strip removes leading and trailing whitespace only    ".strip())
print("This is nice.  Really nice.".replace("nice", "sweet"))
print("This is nice.  Really nice.".replace("nice", "sweet", 1)) # count = 1

print("----------------")
s = "This is so so fun!"
t = s.replace("so ", "")
print(t)
print(s) # note that s is unmodified (strings are immutable!)

#Substrings!!
print("This is a history test".count("is")) # 3
print("This IS a history test".count("is")) # 2
print("-------")
print("Dogs and cats!".startswith("Do"))    # True
print("Dogs and cats!".startswith("Don't")) # False
print("-------")
print("Dogs and cats!".endswith("!"))       # True
print("Dogs and cats!".endswith("rats!"))   # False
print("-------")
print("Dogs and cats!".find("and"))         # 5
print("Dogs and cats!".find("or"))          # -1
print("-------")
print("Dogs and cats!".index("and"))        # 5
print("Dogs and cats!".index("or"))         # crash!



#    STRING FORMATTING
#format a string with %s
breed = "beagle"
print("Did you see a %s?" % breed)
#format an integer with %d
dogs = 42
print("There are %d dogs." % dogs)
#format a float with %f
rade = 87.385
print("Your current grade is %f!" % grade)
#format a float with %.[precision]f
#You can control how many fractional digits of a float are included in the string by changing the number to the right of the decimal point.
grade = 87.385
print("Your current grade is %0.1f!" % grade)
print("Your current grade is %0.2f!" % grade)
print("Your current grade is %0.3f!" % grade)
print("Your current grade is %0.4f!" % grade)

#multiple at a time
dogs = 42
cats = 18
exclamation = "Wow"
print("There are %d dogs and %d cats. %s!!!" % (dogs, cats, exclamation))

#format right-aligned with %[minWidth]
dogs = 42
cats = 3
print("%10s %10s" % ("dogs", "cats"))
print("%10d %10d" % (dogs, cats))
#format left-aligned with %-[minWidth]
dogs = 42
cats = 3
print("%-10s %-10s" % ("dogs", "cats"))
print("%-10d %-10d" % (dogs, cats))
#String Formatting with f Strings
x = 42
y = 99
# Place variable names in {squiggly braces} to print their values, like so:
print(f'Did you know that {x} + {y} is {x+y}?')

# BASIC FILE IO-------------------------------------------------------------------------------
# Note: As this requires read-write access to your hard drive,
#       this will not run in the browser in Brython.

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

contentsToWrite = "This is a test!\nIt is only a test!"
writeFile("foo.txt", contentsToWrite)

contentsRead = readFile("foo.txt")
assert(contentsRead == contentsToWrite)

print("Open the file foo.txt and verify its contents.")

#-------------------------Recitation Notes--------------------
#ord: gives ascii val from character
#chr: gives the character from the ascii value

#for 0 -> len(s)

def encode(s):
    result = ""
    for c in s:
        asciiVal = ord(c)
        result += str(asciiVal)
    return int(result)
'''
algorithm ideas for areAnagrams:
-check to see that every character in s1 appears the same number of times in s2

structural ideas for areAnagrams:
-how to convert a string to lower: .lower()
-check lengths are the same
-how to get the number of times a character c appears in string s: s.count(c)
-do the same check backwards
'''
def areAnagrams(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    for c in s1:
        if s1.count(c) != s2.count(c):
            return False
    return True
   

#collapseWhiteSpace
#without using s.replace() replace white space with single space

'''
Brainstorming:
'a\tb' --> 'a b'
'a \tb' --> 'a b'

Algorithm:
Find where the white space is
loop through s and see if the character is whitespace

To check if c is a whitespace: c.isspace()
replace the whitespace with a single space
keep track of previous character

'''
def collapseWhitespace(s):
    prev = ""
    result = ""
    for c in s:
        if (c.isspace() and prev.isspace()):
            result += " "
        elif (not c.isspace()):
            result += c
        prev = c
    return result


