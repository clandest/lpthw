def cheese_and_crackers(cheese_count, box_of_crackers):
    print 'you have %d of cheese' % cheese_count
    print 'you have %d boxes of crackers' % box_of_crackers
    print 'thats enough for a party!'
    print 'get a blanket! \n'

print 'we can just give the function numbers directly'
cheese_and_crackers(20, 30)

print 'or we can use variables from our script'
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print 'we can even do math inside too!'
cheese_and_crackers(50+10, 5 / 2 + 8)

print 'and we can combine the two variables and math'
cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers - 40)

