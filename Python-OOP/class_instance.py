# 1-) Classes and Instances (Sınıflar ve Nesneler)

class Personel:
    # Yapılandırma Fonksiyonu
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.eposta = f'{isim}_{soyisim}@firma.com'
    
    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'

# self = Sınıfımızdan oluşturacağımız nesneleri temsil ediyor.

per_1 = Personel(isim="Fatih", soyisim="Yapan",maas=15000)
per_2 = Personel("Faruk","Yapan",12000)

# print(per_2.isim)
# print(per_2.soyisim)
# print(per_2.maas)
# print(per_2.eposta)

print(per_1.tam_isim())
print(Personel.tam_isim(per_1))

# print(Personel)


# per_1.isim = "Fatih"
# per_1.soyisim = "Yapan"
# per_1.maas = 10000

# print(per_1.isim)
# print(per_1.soyisim)