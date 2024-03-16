import time
# Hesapların Dictionary Veri Tipi Kullanılarak Kaydedilmesi.
omerfarukozvardar = {
    "ad":"Ömer Faruk",
    "soyisim":"Özvardar",
    "hesaptipi":"Vadeli",
    "bakiye":24500,
    "ekhesap": 4000,
    "borc": 3000,
    "pin":4325
}

sahapugurozvardar = {
    "ad":"Şahap Uğur",
    "soyisim":"Özvardar",
    "hesaptipi":"Vadeli",
    "bakiye":750000,
    "ekhesap": 60000,
    "borc": 2456,
    "pin":2525
}

# Para çekme, Para yatırma, Borç ödeme Gibi Fonksiyonların Tanımlanması

def paraCek(hesapAdi): # Para Çekme Fonksiyonu
    try: # Olası Bir Durumda Hata Yönetimi
        print(f"Merhabalar {hesapAdi["ad"]} {hesapAdi["soyisim"]} Para Çekme Sekmesine Hoşgeldiniz !")
        time.sleep(2)
        try:
            cekilecekMiktar = int(input("Lütfen Çekmek İstediğiniz Miktarı Giriniz: "))
            time.sleep(2)
        except ValueError as err:
            print("Yanlış Bir Tuşlama Yaptınız !!") #int veri tipli inputa string veya farklı tip bir veri girilme durumunda çalışacak bir hata yönetim kod bloğu.
        if (hesapAdi["bakiye"] > cekilecekMiktar):
            hesapAdi["bakiye"] = hesapAdi["bakiye"] - cekilecekMiktar
            print(f"Para Çekme İşlemi Başarıyla Tamamlanmıştır. Yeni Hesap Bakiyeniz: {hesapAdi["bakiye"]}")
        else:
            print("Hesabınızda Çekmek İstediğiniz Miktar Kadar Bakiye Bulunmamaktadır...")
            
            ekhesapKullanilacak = cekilecekMiktar - hesapAdi["bakiye"] 
            if ekhesapKullanilacak < hesapAdi["ekhesap"]:
                hesapAdi["bakiye"] = 0 
                hesapAdi["ekhesap"] - ekhesapKullanilacak
                time.sleep(2)
                print(f"Ek Hesap Başarıyla Kullanıldı. Yeni Ek Hesap Bakiyeniz: {hesapAdi["ekhesap"]}, Yeni Hesap Bakiyeniz: {hesapAdi["bakiye"]} ")
            else:
                print("Çekilecek Miktarı Karşılayacak Ek Hesap Bakiyeniz Bulunmamaktadır !!")
    finally:
        pass


def paraYatir(hesapadi):  # Para Yatırma Fonksiyonu
    try:
        yatirilacakMiktar = int(input(f"Para Yatırma Sekmesine Hoşgeldiniz Sayın {hesapadi["ad"]} {hesapadi["soyisim"]}...\nLütfen Yatırmak İstediğiniz Miktarı Giriniz:  ")) # Yatırılacak Miktarın Belirlenmesi
    except ValueError as err: # Olası Farklı Veri Tipi Girişi Sonucu Hata Yönetimi
        print("Yanlış ya da Eksik Bir Tuşlama Yaptınız !!")
    time.sleep(2)
    if yatirilacakMiktar > 0 and yatirilacakMiktar!=None: # Yatırılacak Miktarın Negatif ve Boş Değer Olmasına Karşılık Hata Yönetimi
        hesapadi["bakiye"] += yatirilacakMiktar # Bakiyenin Yatırılması
        print(f"Para Yatırma İşleminiz Başarıyla Tamamlanmıştır Yeni Bakiyeniz {hesapadi["bakiye"]}")

def borcOde(hesapadi):
    odenecekBorc = int(input(f"Borç Ödeme Sekmesine Hoşgeldiniz {hesapadi["ad"]} {hesapadi["soyisim"]} Lütfen Yatırmak İstediğiniz Borç Miktarını Giriniz(Borç Miktarınız {hesapadi["borc"]}):  "))

    if odenecekBorc > hesapadi["borc"]:
        print("Mevcut Borcunuzdan Fazla Ödeme Yapamazsınız !!")
        return False
    
    elif odenecekBorc < hesapadi["borc"]:
        onay = input(f"Mevcut Borcunuz {hesapadi["borc"]} , Ödemek İstediğiniz Miktar {odenecekBorc} Onaylıyor Musunuz ? : (e/h)")
        if onay == "e":
            print("Onay Verdiniz... İşleminiz Gerçekleşiyor...")
            time.sleep(2)
            hesapadi["borc"] -= odenecekBorc
            print(f"Borç Ödeme İşleminiz Başarıyla Tamamlandı. Mevcut Borç : {hesapadi["borc"]}")
        elif onay == "h":
            print("İşlemi Onaylamadınız Çıkış Yapılıyor... ")
            return False




while True:
    hesapSec = int(input("OFOBANK'a Hoşgeldiniz Lütfen İşlem Yapmak İstediğiniz Hesabı Seçiniz:\n1-Ömer Faruk Özvardar\n2-Şahap Uğur Özvardar"))
    if hesapSec == 1:
        hesapSifresi = int(input("Lütfen Seçtiğiniz Hesabın 4 Haneli PIN Şifresini Giriniz: "))
        if omerfarukozvardar["pin"] == hesapSifresi:
            anamenuGit = input("Başarıyla Giriş Yapıldı Lütfen Ana Menüye Gitmek için 'Enter' Tuşuna Basınız...")
            if anamenuGit == "":
                islemSec = int(input("Ana Menüye Hoşgeldiniz Lütfen Yapmak İstediğiniz İşlemi Seçiniz:\n1-Para Çek\n2-Borç Öde\n3-Para Yatır"))
                if islemSec == 1:
                    paraCek(omerfarukozvardar)
                elif islemSec == 2:
                    borcOde(omerfarukozvardar)
                elif islemSec == 3:
                    paraYatir(omerfarukozvardar)
    elif hesapSec == 2:
        hesapSifresi = int(input("Lütfen Seçtiğiniz Hesabın 4 Haneli PIN Şifresini Giriniz: "))
        if sahapugurozvardar["pin"] == hesapSifresi:
            anamenuGit = input("Başarıyla Giriş Yapıldı Lütfen Ana Menüye Gitmek için 'Enter' Tuşuna Basınız...")
            if anamenuGit == "":
                islemSec = int(input("Ana Menüye Hoşgeldiniz Lütfen Yapmak İstediğiniz İşlemi Seçiniz:\n1-Para Çek\n2-Borç Öde\n3-Para Yatır"))
                if islemSec == 1:
                    paraCek(sahapugurozvardar)
                elif islemSec==2:
                    borcOde(sahapugurozvardar)
                elif islemSec == 3:
                    paraYatir(sahapugurozvardar)
        else:
            print("Girdiğiniz Hesap Girdiğiniz PIN ile Uyuşmamaktadır !!")
            continue
