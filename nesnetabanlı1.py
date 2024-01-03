class Araba:
    def __init__(self, vites_tipi, marka, renk, plaka, km):
        self.vites_tipi = vites_tipi
        self.marka = marka
        self.renk = renk
        self.plaka = plaka
        self.km = km
        print("__init__ çalıştı.")

    def hizArttir(self):
        self.km += 10
        print("Metod çalıştı.")
        return self.km

    def stop(self):
        print("Araba durduruldu.")