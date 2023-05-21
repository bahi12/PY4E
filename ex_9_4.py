name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
# Create a dictionary to store the word counts
count = {}

# Open the file and loop over each line
with open(name, 'r') as file:
    for line in file:
        # Check if the line starts with "From" and has at least two words
        if line.startswith('From ') and len(line.strip().split()) >= 2:
            # Split the line into words
            words = line.strip().split()

            # Get the second word and add it to the word count dictionary
            second_word = words[1]
            count[second_word] = count.get(second_word, 0) + 1

bigcount = None
bigword = None
for word, count in count.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)
