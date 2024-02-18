# 5-) Special Methods (Özel Methodlar)

class Personel:

    """
        Bu sınıf yeni personeller yaratmak için yazılmıştır.
    """

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

    def __repr__(self): # Diğer geliştiricilere bilgi vermek için kullanılır.
        return f"Personel('{self.isim}', '{self.soyisim}', {self.maas})"
    
    def __str__(self): # Son kullanıcıya bilgi vermek için kullanılır.
        return f"{self.tam_isim()} - {self.eposta}"
    
    def __add__(self, other):
        return self.maas + other.maas
    
    def __len__(self):
        return len(self.tam_isim())

per_1 = Personel("Fatih", "Yapan", 15000)
per_2 = Personel("Faruk", "Yapan", 12000)

# print(per_1)
# print(str(per_1))
# print(repr(per_1))
# print(per_1.__str__())
# print(per_1.__repr__())

# print(per_1 + per_2)
# print(per_1.__add__(per_2))
# print(Personel.__add__(per_1,per_2))

# print(len(per_1))

print(help(per_1))