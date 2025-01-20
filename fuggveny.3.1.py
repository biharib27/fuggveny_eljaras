def harommal_oszthatok(szamok):
    darab = 0
    for szam in szamok:
        if szam % 3 == 0:  
            darab += 1
    return darab
szam_lista = [3, 7, 9, 12, 14, 18, 22]
harommal_oszthatok_szama = harommal_oszthatok(szam_lista)
print(f"A listában {harommal_oszthatok_szama} darab hárommal osztható szám van.")


