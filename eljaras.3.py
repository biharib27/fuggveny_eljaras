def osszehasonlit_ket_szamot():
    """
    Ez az eljárás bekéri a felhasználótól két számot, összehasonlítja őket,
    és kiírja, hogy melyik a nagyobb, vagy ha a két szám egyenlő.
    """
    szam1 = float(input("Kérem az első számot: "))
    szam2 = float(input("Kérem a második számot: "))
    if szam1 > szam2:
        print("A nagyobb szám:", szam1)
    elif szam1 < szam2:
        print("A nagyobb szám:", szam2)
    else:
        print("A két szám egyenlő.")
osszehasonlit_ket_szamot()
