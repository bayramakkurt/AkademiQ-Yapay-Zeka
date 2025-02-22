#Reference Type vs Value Type  ---İmmutable vs Mutable
#İmmutable: Değiştirilemez
#Mutable: Değiştirilebilir
print("-----------------Reference Type vs Value Type-----------------")
a=1
b=a
b+=10
print("a:",a)
print("b:",b)

#Sayi gibi basit değişkenler Stackte tutulur ve değerleri kopyalanır yani a ve b farklı adreslerde tutulur

list1=["Ahmet","Azra","Emine"]
list2=list1

list2.append("Fatma")

print("list1:",list1)
print("list2:",list2) #Eleman list2 ye eklendiği için list1 de değişti bunun sebebi list1 ve list2 nin aynı referansı göstermesi    

#Liste gibi karmaşık değişkenler Heapte tutulur ve referansları kopyalanır yani list1 ve list2 aynı adresi gösterir
#Bütün programlama dillerinde bu durum geçerlidir ve bu durumdan dolayı hata yapmamak için dikkatli olunmalıdır
#RAM çalışma mantığından dolayı böyle bir durum söz konusudur

#DÖNGÜLER => for, while, do-while   ----İteration
print("-----------------Döngüler-----------------")

#For Döngüsü
for i in range(5): #İndentation yani girinti çok önemli. Bu döngü 0'dan 5'e kadar sayar(5 dahil değil)
    print(i)
    print("Merhaba")
print("Döngü Bitti")

for i in range(1,5): #1'den 5'e kadar sayar(5 dahil değil)
    print(i)

for i in range(1,10,2): #1'den 10'a kadar 2'şer 2'şer sayar (10 dahil değil)
    print(i)

#Break ve Continue
print("-----------------Break ve Continue-----------------")
print("Break")
for i in range(0,100):
    if i==50:
        break #Döngüyü kırar ve döngüyü sonlandırır
    print(i)
print("Continue")
for i in range(0,100):
    if i%2==0:
        continue #Döngüyü kırar ve bir sonraki adıma geçer yani döngüyü sonlandırmaz
    print(i)

#Listelerde Döngü
print("-----------------Listelerde Döngü-----------------")
liste=[1,2,3,4,5]
for i in liste:
    print(i)

#While Döngüsü
print("-----------------While Döngüsü-----------------")
i=0
while i<5: #i 5'ten küçük olduğu sürece döngü devam eder yani şart True olduğu sürece döngü devam eder
    print(i)
    i+=1

#Şartlar => if, elif, else
print("-----------------Şartlar-----------------")
age=17
if age>18: #İf bloğu yanındaki şart True dönerse içerideki kod bloğu çalışır.
    print("Giriş Yapabilirsiniz.")
elif age==18: #İf bloğu yanındaki şart False dönerse elif bloğu bakılır eğerki Elif bloğu True dönerse içerideki kod bloğu çalışır.
    print("Ay Kontrolü Yapılıyor...")
else: #İf ve elif bloğu yanındaki şart False dönerse else bloğu çalışır.
    print("Giriş Yapamazsınız.")


#Fonksiyonlar
print("-----------------Fonksiyonlar-----------------")

price=100
total_price=price+(price*0.2)
print(total_price)

def calculate_tax(price,rate): #Parametreler fonksiyonun içinde tanımlanır ve fonksiyonun içinde kullanılır
    print(price+(price*(rate/100)))

calculate_tax(100,20)
calculate_tax(200,18)

#Default Parametreler
print("-----------------Default Parametreler-----------------")
def calculate_tax2(price,rate=18): #Parametrelerin default değerleri tanımlanabilir eğer rate değeri verilmezse 18 alınır verilirse verilen değer kullanılır.
    print(price+(price*(rate/100)))

calculate_tax2(100,20)
calculate_tax2(200)

#Return
print("-----------------Return-----------------")
def calculate_tax3(price,rate=18): #Fonksiyon sonunda return kullanılırsa fonksiyonun sonucu başka bir değişkene atanabilir
    return price+(price*(rate/100))

price1=calculate_tax3(100,20)
price2=calculate_tax3(200)
print(price1)
print(price2)

#Args ve Kwargs
print("-----------------Args ve Kwargs-----------------")
def sum(*args): #Args fonksiyona birden fazla parametre göndermek için kullanılır
    if len(args)<=0:
        raise ValueError("En az bir parametre girmelisiniz.")
    total=0
    for i in args:
        total+=i
    return total

print(sum(1,2,3,4,5))
print(sum(1,2,3,4,5,6,7,8,9,10))
#print(sum())

#Kwargs
def display(**kwargs): #Kwargs fonksiyona birden fazla keyword parametre göndermek için kullanılır yani key-value şeklinde gönderilir
    for key,value in kwargs.items():
        print(key,value)

display(name="Ahmet",surname="Yılmaz",age=25)

#Lambda Fonksiyonlar
print("-----------------Lambda Fonksiyonlar-----------------")

topla=lambda x,y:x+y #Lambda fonksiyonları genellikle kısa işlemler için kullanılır
print(topla(5,3))

selamla=lambda name:"Merhaba "+name
print(selamla("Ahmet"))