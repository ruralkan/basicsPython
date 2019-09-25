f = open("wasteland.txt", mode='wt', encoding='utf-8')

# Writes return the number of codepoints or characters written to the file
f.write('What are the roots that clutch,')
f.write('what brances grow \n')
f.write('Out of this stony rubbish? ')

# Always close the file
f.close()


# Reading files
g = open("wasteland.txt", mode='rt', encoding='utf-8')

#read() method accepts the number of characters to read from the file
g.read(32)

#To read all the remaining data in the file we can call read() without an argument
g.read()

#At the end of the file, further calls to read() return an empty string
g.read()


# seek() method with an argument of zero to move the file pointer back to the start
# of the file. the return value of seek() is the new file pointer position
g.seek(0)


# Readline line by line
g.readline()
g.readline()

# Once we reach the end of the file further calls to readline() 
# return an empty string
g.readline()

g.seek(0)


#Reading multiple lines at once

# We can read all tines from the file into a list with the readlines() method:
g.readlines()

g.close()


# Appending to files
h = open('wasteland.txt', mode='at', encoding='utf-8')

# writelines() methods writes an iterable series of string to the stream. If you want
# line ending on your string you must provide them yourself
h.writelines(
    ['Son of man, \h',
    'You cannot say, or guess, ',
    'for you know only, \n',
    'A heap of broken images, ',
    'where the sun beats\n'])
h.close()


# Files objects as iterators
f = open("filename", mode='rt', encoding='utf'8)
for line in f:
    print(line)
    
f.close()
