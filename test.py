emails = open('mbox.txt')
for line in emails:
    line = line.rstrip()
    if line.startswith('From: '):
        print (line)
