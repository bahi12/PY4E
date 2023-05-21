try:
    score = input('Enter a sccore (0.0 - 1.0): ')
    fs = float(score)
    if fs < 0.0 or fs > 1.0:
        print('Score out of range')
        exit(1)
    if fs >= 0.9:
        print('A')
    elif fs >= 0.8:
        print('B')
    elif fs >= 0.7:
        print('C')
    elif fs >= 0.6:
        print('D')
    elif fs < 0.6:
        print('F')
except ValueError:
    print('Please enter a valid score!')


