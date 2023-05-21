# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except IOError:
    print("File not found.")
    quit()

for line in fh:
    line = line.rstrip()
    print(line.upper)