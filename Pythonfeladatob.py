from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalasok = []

    def foglal(self, datum):
        self.foglalasok.append(datum)

    def lemond(self, datum):
        if datum in self.foglalasok:
            self.foglalasok.remove(datum)

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, ar=2200)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, ar=5500)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def uj_szoba_hozzaadasa(self, szobaszam, szobatipus):
        if szobatipus == "egyagyas":
            self.szobak.append(EgyagyasSzoba(szobaszam))
        elif szobatipus == "ketagyas":
            self.szobak.append(KetagyasSzoba(szobaszam))
        else:
            print("Érvénytelen szobatípus.")

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if datetime.now() < datum:
                    szoba.foglal(datum)
                    print(f"Sikeres foglalás a(z) {szobaszam} szobában! Foglalás dátuma:", datum.strftime("%Y-%m-%d"))
                    return szoba.ar
                else:
                    print("A foglalás dátuma már elmúlt.")
                    return None
        print("Nincs ilyen szoba.")

    def lemondas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if datum in szoba.foglalasok:
                    szoba.lemond(datum)
                    print("Sikeres lemondás!")
                else:
                    print("Nincs ilyen foglalás.")
                return
        print("Nincs ilyen szoba.")

    def listazas(self):
      for szoba in self.szobak:
        foglalasok_str = [f"Foglalt! Foglalás dátuma: {datum.strftime('%Y-%m-%d')}" for datum in szoba.foglalasok]
        print(f"{szoba.szobaszam}-es Szoba foglalásai: {foglalasok_str}")

    def foglalas_datum_alapjan(self, datum):
        osszeg = 0
        for szoba in self.szobak:
            if datum in szoba.foglalasok:
                osszeg += szoba.ar
        return osszeg


szalloda = Szalloda("Példa Szálloda")

szalloda.uj_szoba_hozzaadasa("10", "egyagyas")
szalloda.uj_szoba_hozzaadasa("12", "egyagyas")
szalloda.uj_szoba_hozzaadasa("14", "ketagyas")
szalloda.uj_szoba_hozzaadasa("16", "ketagyas")
szalloda.uj_szoba_hozzaadasa("18", "ketagyas")

while True:
    print("\nVálasszon műveletet:")
    print("Szoba Számok: 10,12,14,16,18")
    print("1. Szoba Foglalás")
    print("2.Szoba Lemondás")
    print("3. Szoba Foglalások listázása")
    print("4. Szoba Foglalás Ár")
    print("5. Kilépés")

    valasztas = input("Művelet kiválasztása: ")

    if valasztas == "1":
        szobaszam = input("Kérem adja meg a szoba számát: ")
        datum_str = input("Kérem adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")
        szalloda.foglalas(szobaszam, datum)
    elif valasztas == "2":
        szobaszam = input("Kérem adja meg a szoba számát: ")
        datum_str = input("Kérem adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")
        szalloda.lemondas(szobaszam, datum)
    elif valasztas == "3":
        szalloda.listazas()
    elif valasztas == "4":
        datum_str = input("Kérem adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")
        osszeg = szalloda.foglalas_datum_alapjan(datum)
        print(f"A foglalás dátuma alapján összesen fizetendő összeg: {osszeg}")
    elif valasztas == "5":
        break
    else:
        print("Érvénytelen választás. Kérem válasszon újra.")
