# 7-) PROPERTY DECORATORS, GETTERS, SETTERS, DELETERS


class Personel:

    personel_sayisi = 0
    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas

        Personel.personel_sayisi += 1
    
    @property
    def eposta(self):
        return f'{self.isim}_{self.soyisim}@firma.com'
    
    @property
    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'
    
    @tam_isim.setter
    def tam_isim(self, ad):
        isim, soyisim = ad.split(" ")
        self.isim = isim
        self.soyisim = soyisim
    
    @tam_isim.deleter
    def tam_isim(self):
        print("Değişkenlerin İçi Silindi")
        self.isim = None
        self.soyisim = None
    

per_1 = Personel("Fatih", "Yapan", 15000)

# per_1.isim = "Faruk"

# per_1.tam_isim = "Faruk Turan"

# print(per_1.isim)
# print(per_1.eposta)
# print(per_1.tam_isim)


del(per_1.tam_isim)
print(per_1.isim)
print(per_1.soyisim)