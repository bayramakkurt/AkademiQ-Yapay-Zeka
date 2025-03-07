#•	1’den 100’e kadar olan sayıları ekrana yazdırın.
for i in range(1,101):
    print(f"Sayı: {i}")

#•	1’den 100’e kadar sadece çift sayıları ekrana yazdıran bir program yazın.
for i in range(1,101):
    if i%2==0:
        print(f"Çift Sayı: {i}")

#•	Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir program yazın.
sayi=int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz: "))
sonuc=1
for i in range(sayi,1,-1):
    sonuc*=i
print(f"{sayi}! = {sonuc}")

#•	1’den 100’e kadar olan tüm asal sayıları bulan bir program yazın.
c=False
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            c=True
            break
    if c==False:
        print(f"Asal Sayı: {i}")
        c=False
    else:
        c=False
