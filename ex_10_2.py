name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

# Open the file for reading
with open(name, 'r') as file:
    # Initialize a dictionary to store the counts for each hour
    hour_counts = {}
    # Loop through each line in the file
    for line in file:
        # Check if the line starts with 'From '
        if line.startswith('From '):
            # Split the line into words
            words = line.split()
            # Extract the time string from the line
            time_str = words[5]
            # Split the time string into hour, minute, and second
            hour, minute, second = time_str.split(':')
            # Increment the count for the hour in the dictionary
            hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Print the counts sorted by hour
for hour in sorted(hour_counts):
    print(hour, 'h', hour_counts[hour], 'emails received')
