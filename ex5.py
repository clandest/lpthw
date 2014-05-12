name = 'Devyn Challman'
age = 35 # not a lie
#height = 74 # inches
height = 74.0 * 2.54 # centimeters
#weight = 180 # pounds
weight = 180.0 * 0.45 # kilos
eyes = 'blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d kilos heavy." % weight
print "Actually thats not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
