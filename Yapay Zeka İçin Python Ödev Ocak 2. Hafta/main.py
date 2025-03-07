#•	Kullanıcının girdiği bir sayının tek mi çift mi olduğunu bulan bir Python programı yazın.
sayi=int(input("Sayıyı giriniz:"))
if sayi%2==0:
    print("Girdiğiniz sayı çifttir.")
else:
    print("Girdiğiniz sayı tektir.")

#•	Kullanıcının notunu alarak aşağıdaki not sistemine göre harf notunu hesaplayın:
puan=int(input("Notunuzu giriniz:"))

if(puan>=90 and puan<=100):
    print("Aldığınız notun harf karşılığı: A")
elif(puan>=80 and puan<=89):
    print("Aldığınız notun harf karşılığı: B")
elif(puan>=70 and puan<=79):
    print("Aldığınız notun harf karşılığı: C")
elif(puan>=60 and puan<=69):
    print("Aldığınız notun harf karşılığı: D")
elif(puan>=0 and puan<=59):
    print("Aldığınız notun harf karşılığı: F")
else:
    print("Geçersiz not girdiniz.")

#•	Kullanıcının yaşına göre hangi yaş grubunda olduğunu bulan bir program yazın:
yas=int(input("Yaşınızı giriniz:"))

if(yas>=0 and yas<=12):
    print("0-12 yaş aralığı ÇOCUK yaş grubundadır.")
elif(yas>=13 and yas<=19):
    print("13-19 yaş aralığı GENÇ yaş grubundadır.")
elif(yas>=20 and yas<=59):
    print("20-59 yaş aralığı YETİŞKİN yaş grubundadır.")
elif(yas>=60):
    print("60 yaş ve üzeri YAŞLI yaş grubundadır.")
else:
    print("Geçersiz yaş girdiniz.")