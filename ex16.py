from sys import argv

script, filename = argv

print 'we are going to erase %s.' % filename
print 'if you don\'t want that, hit CTRL-C (^C).'
print 'if you do want that, hit RETURN.'

raw_input('?')

print 'opening file....'
target = open(filename, 'w')

print 'Truncating the file. Goodbye!'
target.truncate()

print 'now i\'m going to ask you for three lines.'

line1 = raw_input('line: 1')
line2 = raw_input('line: 2')
line3 = raw_input('line: 3')

print 'I\'m going to write theses to the file.'

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print 'and finally, we close it.'
target.close()
