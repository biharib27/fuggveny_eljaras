def kerulet(a, *oldalak):
    if len(oldalak) == 0:
        return 4 * a  
    if len(oldalak) == 1:
        return 2 * (a + oldalak[0]) 
    if len(oldalak) == 2:
        return a + oldalak[0] + oldalak[1]  
    if len(oldalak) > 2:
        return a + sum(oldalak) 
print('Négyzet kerülete: ', kerulet(8)) 
print('Téglalap kerülete: ', kerulet(7, 4))
print('Háromszög kerülete: ', kerulet(10, 5, 6))
print('Sokszög kerülete: ', kerulet(3, 7, 4, 8, 2))

