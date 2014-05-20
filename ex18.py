# This one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok that *args is acutally pointless, we can do it this way
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes none
def print_none():
    print "I got nothing."

print_two('devyn', 'ashlin')
print_two_again('devyn', 'ashlin')
print_one('ashlin')
print_none()
