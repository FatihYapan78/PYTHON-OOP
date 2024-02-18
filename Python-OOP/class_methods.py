# 3-) Regular Methods (Normal Methodlar) - Class Methods (Sınıf Methodları) - Static Methods (Static Methodları)

# Regular Methods = İlk parametre olarak self yani nesneyi alır.
# Class Methods = İlk parametre olarak sınıfın kendisini alır.
# Static Methods = Method içinde sınıfa veya nesneye ait bir değişkene ihtiyacımız yok ise kullanılır.

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

    @classmethod
    def zam_orani_belirle(cls, oran):
        cls.zam_orani = oran

    @classmethod
    def from_string(cls, per_str):
        isim, soyisim, maas = per_str.split("-")
        return cls(isim, soyisim, maas)
    
    @staticmethod
    def mesai_gunu(gun):
        if gun.weekday() == 5 or gun.weekday() == 6:
            return "Hafta Sonu"
        else:
            return "Hafta İçi"


# per_1 = Personel(isim="Fatih", soyisim="Yapan",maas=15000)
# per_2 = Personel("Faruk","Yapan",12000)


# Personel.zam_orani_belirle(1.1)

# print(Personel.zam_orani)
# print(per_1.zam_orani)
        
# per_str_1 = "Fatih-Yapan-10000"
# per_str_2 = "Faruk-Yapan-15000"

# new_per_1 = Personel.from_string(per_str_1)

# print(new_per_1.eposta)
        
import datetime

tarih = datetime.date(2024,2,13)
print(tarih.day)
print(Personel.mesai_gunu(tarih))