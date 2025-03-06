#Dosya İşlemleri
print("------------------Dosya İşlemleri------------------")
#1. Adım: Dosya Açma
#Dosya açma işlemi open() fonksiyonu ile yapılır.
#open() fonksiyonu dosya adı ve dosya açma modu parametreleri alır.
#Dosya açma modları:
# r: Dosyayı okuma modunda açar. Dosya yoksa hata verir.
# w: Dosyayı yazma modunda açar. Dosya yoksa oluşturur.
# a: Dosyayı ekleme modunda açar. Dosya yoksa oluşturur.
# x: Dosyayı oluşturma modunda açar. Dosya varsa hata verir.
# Dosya açma modlarına ek olarak dosya türü belirtilir.
# t: Metin dosyası
# b: Binary dosya
# Dosya açma modu ve dosya türü birlikte kullanılır.
# Örnek: Dosya okuma modunda açma işlemi
dosya = open("c:/Users/HBA/Desktop/AkademiQ Yapay Zeka/Odev-3/calisma.txt", "rt")


#2. Adım: Dosya Okuma
#Dosya okuma işlemi read() fonksiyonu ile yapılır.
#read() fonksiyonu dosyanın tamamını okur.
#Örnek: Dosya okuma işlemi
icerik = dosya.read()
print(icerik)
#Dosya kapatma işlemi close() fonksiyonu ile yapılır.
dosya.close()

#3. Adım: Dosya Yazma
#Dosya yazma işlemi write() fonksiyonu ile yapılır.
#Örnek: Dosya yazma işlemi
dosya = open("c:/Users/HBA/Desktop/AkademiQ Yapay Zeka/Odev-3/calisma.txt", "wt")
dosya.write("Merhaba Python\n")
dosya.write("Merhaba Dünya\n")
#Dosya kapatma işlemi close() fonksiyonu ile yapılır.
dosya.close()

#4. Adım: Dosya Ekleme
#Dosya ekleme işlemi append() fonksiyonu ile yapılır.
#Örnek: Dosya ekleme işlemi
dosya = open("c:/Users/HBA/Desktop/AkademiQ Yapay Zeka/Odev-3/calisma.txt", "at")
dosya.write("Merhaba Python\n")
dosya.write("Merhaba Dünya\n")
#Dosya kapatma işlemi close() fonksiyonu ile yapılır.
dosya.close()


