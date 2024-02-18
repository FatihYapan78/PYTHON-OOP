# 8-) Encapsulation / Kapsülleme


class Personel:

    personel_sayisi = 0
    

    def __init__(self, isim, soyisim, maas):
        self.isim = isim # Public / Global
        self.soyisim = soyisim
        self.maas = maas
        self.eposta = f'{isim}_{soyisim}@firma.com'
        self.__zam_orani = 1.05 # Private

        Personel.personel_sayisi += 1

    def getZamOrani(self):
        return self.__zam_orani
    
    def setZamOrani(self, oran):
        self.__zam_orani = oran
    
    def zam_uygula(self):
        self.maas = self.maas * self.__zam_orani


per_1 = Personel("Fatih", "Yapan", 10000)

print(per_1.getZamOrani())
per_1.setZamOrani(1.1)
print(per_1.getZamOrani())
per_1.zam_uygula()
# print(per_1.zam_orani)
print(per_1.maas)