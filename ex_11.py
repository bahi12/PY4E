import re
name = "regex_sum_1807944.txt"

if (name):
    with open(name, 'r') as file:
        content = file.read()
        numbers = re.findall('[0-9]+', content)
        # print(numbers)
        total = sum(int(n) for n in numbers)
        print(total)
