while True:
    try:
        hrs = input("Enter Hours:")
        h = float(hrs)
        rate = input("Enter Rate:")
        r = float(rate)
        break
    except ValueError:
        print('You should enter a number!')

if h <= 40:
    gpay = h * r
else:
    gpay = (40 * r) + ((h - 40) * (1.5 * r))
print(gpay)