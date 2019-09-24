len("Hello world!")


# Concatenation of strings
"New" + "found" + "land"

s = "New"
s += "found"
s += "land"

colors = ';'.join(['##45ff23', '#2321fa', '#1298a3', '#a32312'])

''.join(['high', 'way', 'man'])


#Split string
recipes = 'eggsandbaconandspam'
recipes.split('and')

"This is a sentence".split("e") #['This is a s', 'nt', 'nc', '']
"This is a sentence".split("e", maxsplit=0) # ['This is a sentence']
"This is a sentence".split("e", maxsplit=2) # ['This is a s', 'nt', 'nce']
"This is a sentence".split("e", maxsplit=-1) # ['This is a s', 'nt', 'nc', '']

# Right split
"This is a sentence".rsplit("e", maxsplit=1) # ['This is a sentenc', '']
"This is a sentence".rsplit("e", maxsplit=2) # ['This is a sent', 'nc', '']
"This is a sentence".rsplit("e", maxsplit=-1) # ['This is a s', 'nt', 'nc', '']

# The strip() removes characters from both left and right based on the argument
# (a string specifying the set of characters to be removed)
string = " xoxo love xoxo  "
strint.strip() # xoxo love xoxo
strint.strip("xoxoe") # lov
">>> a python prompt".strip() "a python prompt"
str = "0000000this is string example....wow!!!0000000";
print str.strip( '0' ) # this is string example....wow!!!

# The shortest way to test if a string is emptu or just contains whitespace characters is to use strip
my_str = ''
not my_str.strip() # True


# Partition strings
"unforgettable".partition('forget')
departure, separator, arrival = "London:Edinburgh".partition(":")
departure, _, arrival = "London:Edinburgh".partition(":")

# Changing the caitalization of a string
"This is a 'string'".upper() # "THIS IS A 'STRING'"
str.upper("This is a 'string'") # "THIS IS A 'STRING'"

"This IS A 'string'".lower() # "this is a 'string'"

"This IS A 'string'".capitalize() # "This is a 'string'"

"ThIs IS a 'stRIng'".title() # "This Is A 'String'"

"ThIs IS a 'stRIng'".swapcase() # "tHiS is A 'STriNG'"

[str.upper(x) for x in ['These', 'are', 'some', 'strings']] # ['THESE', 'ARE', 'SOME', 'STRINGS']


# Replace all occurrences of one sbstring with another substring
"Make sure to foo your sentence".replace("foo", "spam") # 'Make sure to spam your sentence'
"It can foo multiple examples of foo if you want".replace("foo", "spam", 1)
# 'It can spam multiple examples of foo if you want'


# Counting number o times a substring appears in a string
 s = "Shee sells seashells by seashore"
 s.count("sh") # 2
 s.count ("se") # 3
 # By default start = 0 and end = len(str)
 s.count(se, start)
 start = 13
 s.count ("se", start) # 1


# Starting and ending characters of a string
s = "This is a test string"
s.startswith("T") # True
s.startswith("Thi") # True
s.startswith("thi") # False
s.startswith("is", 2) # True

# Using a tuple to check if it starts with any of a set of strings
s.startswith("This", "That") # True

# Ending
s = "this ends in a full stop."
s.endswith(".") # True
s.endswith("stop.") # True
s.endswith("!") # False

# Testing what a string is composed of
# isalpha() returns True if all characters ina iven string are alphabetic
"Hello World".isalpha() # False contains space
"Hello2World".isalpha() # False contains numbers
"HelloWorld!".isalpha() # False contains punctuation
"HelloWorld".isalpha() # True 
"".isalpha() # False empty string

# is upper()
"HeLLO WORLD".isupper() #False
"HELO WORLD".isupper() # True

# islower()
"Hello World".islower() # False
"hello world".islower() # True

#istitle()
"Hello World".istitle() # True
"Hello world".istitle() # False
"hello world".istitle() # false

# isdecimal() isdigit() isnumeric()

#isalnum() is True if is alphanumeric
"Hello2World".isalnum() # True
"HelloWorld".isalnum() # True
"Hello World".isalnum() # False contains whitespace
"2016".isalnum() #True

#isspace()
"\t\r\n".isspace() #True
" "isspace # True
""isspace # False


# Translating characters in a string
translation_table = str.maketrans("aeiou", "1234")
my_string = "This is a string"
translated = my_string.translate(translation_table) # 'Th3s 3s 1 str3ng'
#You can st the table argument to None if you only need to delete characters
"this syntax is very useful".translate(None, "aeiou")

