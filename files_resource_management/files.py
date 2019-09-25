import sys

def main(filename):
    f = open("filename", mode='rt', encoding='utf'8)
    for line in f:
        print(line)
    
    f.close()

if if __name__ == "__main__":
    main(sys.argv[1])

""" From Terminal
python3 files.py wasteland.txt

You notice that there are empty lines between each line of the poem, this occurs because
each line in the file is terminated by a new line, and then print() adds its own.
To fix that, we could use the strip() method or use the write() method of stdout stram
"""
def main(filename):
    f = open("filename", mode='rt', encoding='utf'8)
    for line in f:
        sys.stdout.write(line)
    
    f.close()

if if __name__ == "__main__":
    main(sys.argv[1])