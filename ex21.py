def add(a, b):
    print 'ADDING %d + %d' % (a, b)
    return a + b

def subtract(a, b):
    print 'SUBTRACTING %d - %d' % (a, b)
    return a - b

def multiply(a, b):
    print 'MULTIPLYING %d * %d' % (a, b)
    return a * b

def division(a, b):
    print 'DIVIDING %d / %d' % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(50, 10)
height = subtract(43, 8)
weight = multiply(50, 21)
iq = division(58, 12)

print "Age: %d, Height: %d, Weight: %d, I.Q: %d" % (age, height, weight, iq)

# a puzzle for the extra credit, type it in anyway.
print "Here is the puzzle."

what = add(age, subtract(height, multiply(weight, division(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
