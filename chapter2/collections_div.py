
colors = ['black','white']
sizes = ['S', 'M', 'L']
tshirts = [(color,size) for color in colors for size in sizes]
#print( tshirts)

for color in colors:
    for size in sizes:
        print( color, size)


symbols = '$§¢ø'
tuple(ord(symbol) for symbol in symbols)

import array
test = array.array('I',(ord(symbol) for symbol in symbols))
print( test[0])


#cartesian product in a generator expression
for tshirt in ('%s - %s' % (c,s) for c in colors for s in sizes):
    print( tshirt)




