# 4-) Inheritance - Subclass (Miras / Kalıtım - Alt Sınıf)

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

class Yazilimci(Personel):
    zam_orani = 1.1

    def __init__(self, isim, soyisim, maas, prog_dili):
        super().__init__(isim, soyisim, maas)
        self.prog_dili = prog_dili

class Mudur(Personel):

    def __init__(self, isim, soyisim, maas, personeller = None):
        super().__init__(isim, soyisim, maas)
        if personeller is not None:
            self.personeller = personeller
        else:
            self.personeller = []

    def personel_ekle(self, per):
        if per not in self.personeller:
            self.personeller.append(per)
    
    def perseonel_cikar(self, per):
        if per in self.personeller:
            self.personeller.remove(per)

    def personelleri_listele(self):
        for per in self.personeller:
            print(per.tam_isim())



yaz_1 = Yazilimci("Fatih", "Yapan", 15000, "python")
yaz_2 = Yazilimci("Faruk", "Yapan", 12000, "java")

mdr_1 = Mudur("Ali", "Yapan", 15000, [yaz_1])
mdr_2 = Mudur("Ahmet", "Yapan", 12000)

# mdr_1.personelleri_listele()
# print("------------")
# mdr_1.personel_ekle(yaz_2)
# mdr_1.personelleri_listele()
# print("------------")
# mdr_1.perseonel_cikar(yaz_1)
# mdr_1.personelleri_listele()
# print("------------")

# yaz_1.zam_uygula()
# print(yaz_1.zam_orani)
# print(yaz_1.maas)
# print(yaz_1.prog_dili)
# print(yaz_2.eposta)

# isinstance() Yaratılan bir nesnenin belirtilen sınıftan yaratılıp yaratılmadığını gösterir.
# print(isinstance(yaz_1, Yazilimci))
# print(isinstance(yaz_1, Personel))
# issubclass() Yaratılan bir sınıfın belirtilen sınıftan yaratılıp yaratılmadığını gösterir.
# print(issubclass(Yazilimci, Personel))
# print(issubclass(Yazilimci, Mudur))