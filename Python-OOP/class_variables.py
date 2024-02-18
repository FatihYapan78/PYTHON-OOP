# 2-) Class Variables (Sınıf Değişkenleri)

class Personel:

    personel_sayisi = 0
    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.eposta = f'{isim}_{soyisim}@firma.com'

        Personel.personel_sayisi += 1
    
    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'
    
    def zam_uygula(self):
        self.maas = self.maas * self.zam_orani

per_1 = Personel(isim="Fatih", soyisim="Yapan",maas=15000)
per_2 = Personel("Faruk","Yapan",12000)



# Personel.zam_orani = 1.5
per_1.zam_orani = 1.5
print(Personel.zam_orani)
print(per_1.zam_orani)

per_1.zam_uygula()
print(per_1.maas)

print(Personel.personel_sayisi)