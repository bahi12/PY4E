def computepay(h, r):
    fh = float(h)
    fr = float(r)
    if fh <= 40:
        return fh * fr
    else:
        return (40 * fr) + ((fh - 40) * (1.5 * fr))
        # return float(h)* float(r)

hrs = input("Enter Hours:")
rt = input("Enter rate:")
p = computepay(hrs, rt)
print("Pay", p)