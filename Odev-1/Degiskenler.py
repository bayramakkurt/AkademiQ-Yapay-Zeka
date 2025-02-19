print("KodlamaIO")
baslik="Taşıt Kredisi"
print(baslik)
#String => Metinsel ifade
baslik="İhtiyaç Kredisi"
print(baslik)
#Integer,Int => Tam sayı
vade=36
EkVade=6
vade_2="36"
#Float,Decimal,Double => Ondalıklı sayı
aylik_odeme=200.50
#Boolean,Bool => True,False
yukselisteMi=True

#MATEMATİKSEL OPERATÖRLER
#Toplama => +
print("---------TOPLAMA---------")
print(5+5)
print(vade+12)
print(vade+EkVade)
print(36+6)
#Çıkarma => -
print("---------ÇIKARMA---------")
print(5-5)
print(vade-12)
print(vade-EkVade)
print(36-6)
#Çarpma => *
print("---------ÇARPMA---------")
print(5*5)
print(vade*2)
print(vade*EkVade)
print(10*10)
#Bölme => Float Tipinde Değer Döner 
print("---------BÖLME---------")
print(5/5)
print(vade/2)
print(vade/EkVade)
print(10/2)
print("---------DEĞİŞKENLERİN DEĞERLERİNİN DEĞİŞTİRİLMESİ---------")
yeniVade=vade/2
fiyat=100
indirimliFiyat=fiyat-20
print(indirimliFiyat)
print(yeniVade)
#Mod => %
print("---------MOD---------")
print(10%2)
print(vade%5)
print(vade%EkVade)


#MANTIKSAL OPERATÖRLER
#Eşit mi? => ==
print("---------EŞİT Mİ?---------")
print(5==5)
print(1 ==2)

#Eşit Değil mi? => !=
print("---------EŞİT DEĞİL Mİ?---------")
print(5!=5)
print(1 !=2)

#Büyük mü? => >
print("---------BÜYÜK MÜ?---------")
print(5>5)
print(5>4)
print(5>6)
print(5>=5)

#Küçük mü? => <
print("---------KÜÇÜK MÜ?---------")
print(5<5)
print(5<4)
print(5<6)
print(5<=5)

#OR => Veya => True ise True
print("---------OR---------")
print(1>2 or 2>1)

#AND => Ve => True ise True
print("---------AND---------")
print(1>2 and 2>1)
print(1<2 and 2>1)

print(1>2 or 5>2 and 3>2)
print(1>2 and 5>2 and 3>2)
print(2>1 or 1>2 and 3>2)

#NOT => Değil => True ise False, False ise True
print("---------NOT---------")
print(not 1>2)
print(not 2>1)

#KARAR YAPILARI
#IF => Eğer , Else => Değilse , Elif => Değilse Eğer
#IF
print("---------IF,ELSE,ELIF---------")
sayi1=15
sayi2=15
#Sayi1 Sayi2'den büyükse ekrana Sayi1 Sayi2'den büyüktür yazdır.
if sayi1>sayi2: #Condition => Koşul , İndentation => Girinti , Scope => Kapsam 
    print("Sayi1 Sayi2'den büyüktür") 
    print("Bu alan if bloğu içindedir ve şart sağlanırsa çalışır.")
elif sayi1==sayi2:
    print("Sayi1 Sayi2'ye eşittir")
else:
    print("Sayi1 Sayi2'den büyük değildir")
print("Bu alan if bloğu dışındadır ve şart sağlanmasa da çalışır.")
