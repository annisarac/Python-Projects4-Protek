def isPythagoras(a, b, c):
    if((a*a) == (c*c) - (b*b) or (b*b) == (c*c) - (a*a) or (c*c) == (b*b) + (a*a)):
        print('bilangan pithagoras' , a, ',' , b, 'dan' , c, 'adalah' ,True)
    else:
        print('bilangan pithagoras' , a, ',' , b, 'dan' , c, 'adalah' , False)

a1 = 3
b1 = 4
c1 = 5
a2 = 5
b2 = 9
c2 = 12
a3 = 8
b3 = 6
c3 = 10
a4 = 7
b4 = 8
c4 = 11
isPythagoras(a1, b1, c1)
isPythagoras(a2, b2, c2)
isPythagoras(a3, b3, c3)
isPythagoras(a4, b4, c4)
