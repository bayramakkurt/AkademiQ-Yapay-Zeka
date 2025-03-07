#•	Kullanıcıdan adını, yaşını ve doğum yılını alarak ekrana aşağıdaki gibi yazdıran bir 
isim = input("Adınızı giriniz: ")
yas = int(input("Yaşınızı giriniz: "))
dogum_yili = int(input("Doğum yılınızı giriniz: "))
print(f"Merhaba {isim}! {yas} yaşındasın ve {dogum_yili} yılında doğmuşsun.")

#•	Kullanıcıdan iki sayı alarak bu sayıların toplamını, farkını, çarpımını ve bölümünü ekrana yazdırın.
sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2
print(f"Toplam: {toplam}, Fark: {fark}, Çarpım: {carpim}, Bölüm: {bolum}")