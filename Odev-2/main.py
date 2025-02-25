#ASAL SAYI KONTROLÜ
def asal_mi(sayi):
    asalMi=False
    for i in range(2,sayi):
        if sayi%i==0:
            asalMi=False
            break
        else:
            asalMi=True
    if asalMi:
        print(sayi,"Asal bir sayıdır.")
    else:
        print(sayi,"Asal bir sayı değildir.")

asal_mi(7)
asal_mi(10) 

print("-----------------------------------------------")

#Basit Hesap Makinesi
def hesap_makinesi(sayi1,sayi2,islem_turu):
    if islem_turu=="+":
        print(sayi1,"+",sayi2,"=",sayi1+sayi2)
    elif islem_turu=="-":
        print(sayi1,"-",sayi2,"=",sayi1-sayi2)
    elif islem_turu=="*":
        print(sayi1,"*",sayi2,"=",sayi1*sayi2)
    elif islem_turu=="/":
        if sayi2==0:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
        else:
            print(sayi1,"/",sayi2,"=",sayi1/sayi2)
    else:
        print("Geçersiz işlem türü!")

hesap_makinesi(5, 3, '+')  # Çıktı: 5 + 3 = 8
hesap_makinesi(10, 2, '/')  # Çıktı: 10 / 2 = 5.0
hesap_makinesi(4, 0, '/')   # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
hesap_makinesi(6, 2, '%')   # Çıktı: Geçersiz işlem türü!

