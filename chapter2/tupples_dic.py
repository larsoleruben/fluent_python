import os
from collections import namedtuple



lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ( 'Tokyo', 2003, 32450, 0.66, 8014 )
traveller_ids = [('USA', '31195855'),('BRA', 'CE42567'), ('ESP', 'XDZ205856')]

for passport in sorted( traveller_ids):
    print('%s/%s' % passport)

for country, _ in traveller_ids:
    print( country)

print( city )

_, filename = os.path.split( '/Users/larschristoffersen/sourcecode/private/fluent_python/chapter2/tupples_dic.py' )
print(filename)


#using * to grab excess items

a, b, *rest = range(5)
print(a,b,rest)
a, b, *rest = range(3)
print(a,b,rest)
a, b, *rest = range(2)
print(a,b,rest)

#* can appear in any position
a, *body, c,d = range(5)
print(a,body,c,d)
*head, b,c,d = range(5)
print(head, b,c,d)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # <2>
    if longitude <= 0:  # <3>
        print(fmt.format(name, latitude, longitude))

# Named tupples
City = namedtuple('City', 'name coluntry population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])