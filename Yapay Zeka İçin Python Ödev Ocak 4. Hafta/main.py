#•	Kullanıcıdan 5 adet sayı alarak bir listeye ekleyin ve bu listenin toplamını, ortalamasını, en büyük ve en küçük elemanını bulun.
liste=[]
sayi1=int(input("1. sayıyı giriniz:"))
liste.append(sayi1)
sayi2=int(input("2. sayıyı giriniz:"))
liste.append(sayi2)
sayi3=int(input("3. sayıyı giriniz:"))
liste.append(sayi3)
sayi4=int(input("4. sayıyı giriniz:"))
liste.append(sayi4)
sayi5=int(input("5. sayıyı giriniz:"))
liste.append(sayi5)
toplam=0
ortalama=0
enbuyuk=0
enkucuk=0

print("Girilen sayılar:",liste)
print("Toplam:",sum(liste))
ortalama=sum(liste)/len(liste)
print("Ortalama:",ortalama)
enbuyuk=max(liste)
print("En büyük sayı:",enbuyuk)
enkucuk=min(liste)
print("En küçük sayı:",enkucuk)

print("-------------")
toplam=0
for i in liste:
    toplam+=i
print("Toplam:",toplam)
ortalama=toplam/len(liste)
print("Ortalama:",ortalama)
enbuyuk=liste[0]
enkucuk=liste[0]
for i in liste:
    if i>enbuyuk:
        enbuyuk=i
    if i<enkucuk:
        enkucuk=i
print("En büyük sayı:",enbuyuk)
print("En küçük sayı:",enkucuk)


#•	Kullanıcıdan aldığı kelimeleri bir listeye ekleyerek ters sıralayan bir program yazın.
liste=[]
while True:
    kelime=input("Kelime giriniz(Kelime eklemeden çıkmak için boş bırakıp Enter basınız!):")
    if kelime=="":
        break
    liste.append(kelime)

liste.sort(reverse=True)
print(liste)

#•	Bir liste içindeki tekrar eden elemanları kaldıran bir program yazın
import random
liste=[]
for i in range(10):
    liste.append(random.randint(1,5))
print("Liste:",liste)
tekrarsiz_liste=[]
for sayi in liste:
    tekrar_varmi = False      
    for eleman in tekrarsiz_liste:
        if sayi == eleman:
            tekrar_varmi = True
            break  
    if not tekrar_varmi:
        tekrarsiz_liste.append(sayi)  
print("Tekrar edenler kaldırılmış liste:",tekrarsiz_liste)
