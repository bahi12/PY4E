text = "X-DSPAM-Confidence:    0.8475"
a = text.find('0')
b = text.find('5')

parse = float(text[a:b+1])

print(parse)