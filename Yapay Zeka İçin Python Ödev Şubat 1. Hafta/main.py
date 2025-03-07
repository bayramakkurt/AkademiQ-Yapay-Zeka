#•	Girilen iki sayının toplamını, farkını, çarpımını ve bölümünü bulan bir hesap makinesi fonksiyonu yazın.
def hesap_makines(sayi1,sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2
    return f"Toplam: {toplam}, Fark: {fark}, Çarpım: {carpim}, Bölüm: {bolum}"
sayi1=int(input("1. sayıyı giriniz: "))
sayi2=int(input("2. sayıyı giriniz: "))
print(hesap_makines(sayi1,sayi2))

#•	Kullanıcının girdiği bir kelimenin palindrom olup olmadığını kontrol eden bir fonksiyon yazın.
def is_palindrom(kelime):
    kelime = kelime.lower()
    if kelime == kelime[::-1]:
        return "Palindrom"
    else:
        return "Palindrom değil"

kelime = input("Kelime giriniz: ")
print(f"{kelime} kelimesi {is_palindrom(kelime)}")

#•	Kullanıcının yaşını girerek kaç yıl sonra 100 yaşına ulaşacağını hesaplayan bir fonksiyon yazın.
def yas_hesapla(yas):
    kalan_yil = 100 - yas
    return kalan_yil
yas=int(input("Yaşınızı giriniz: "))
print(f"{yas_hesapla(yas)} yıl sonra 100 yaşında olacaksınız.") 