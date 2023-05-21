fname = input("Enter file name: ")
count = []
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        fl = float(line[20:])
        count.append(fl)
total = 0
for value in count:
    total += value

avg = total / len(count)
print("Average spam confidence:", avg)

