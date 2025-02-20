faiz=1.59
vade="36"
krediAdi="İhtiyaç Kredisi"

print("Faiz Değişken Tipi: ",type(faiz))
print("Vade Değişken Tipi: ",type(vade))
print("Kredi Adı Değişken Tipi: ",type(krediAdi))

print(int(vade)+12) #Vade değişkeni String veri tipinde olduğu için Int veri tipine dönüştürüldü.Aksi halde matematiksel işleme dahil olamazdı.
print(str(faiz))    #Faiz değişkeni Float veri tipinde olduğu için String veri tipine dönüştürüldü.
faiz=str(faiz)
print("Faiz Değişken Tipi: ",type(faiz)) #Faiz değişkeni String veri tipine dönüştürüldü.

#Kullanıcıdan Veri Alma
vade=36 #input("Lütfen istediğiniz Vade sayısını giriniz: ")
print("Kullanıcının girdiği vade sayısı: ",vade)
print("Kullanıcının girdiği vade sayısı veri tipi: ",type(vade)) #Kullanıcıdan alınan veri default String veri türündedir.
vade=int(vade) #Kullanıcıdan alınan veri tipi Int veri tipine dönüştürüldü.Aksi halde matematiksel işleme dahil olamazdı.
print(vade+12)

#STRİNG İNTERPOLATİON
print("--------------STRİNG İNTERPOLATİON--------------") #String ekleme yapmak için kullanılır.
#Format Metodu
print("-----------------Format Metodu-----------------")
print("Seçtiğiniz vade sonucu ortaya çıkan vade: ",str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade)) #Metin içinde {} içine yerleştirilen değişken isimleri .format() sonrası kullanılacak değer değişkeni ile eşleştirilir.
isim="Hacı Bayram" #input("Lütfen isminizi giriniz: ")
metin="Merhaba {name}".format(name=isim)
print(metin)

#F-String
print("--------------F-STRİNG--------------")
metin=f"Merhaba {isim}" #F-String ile değişkenler {} içine yazılarak metin içine eklenebilir.
print(metin)

#Listeler
print("--------------LİSTELER--------------")
dizi=["İhtiyaç Kredisi",1.59,36,True] #Listeler farklı veri tiplerini içerebilir.
print("Dizi Listesi: ",dizi)
krediler=["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print("Krediler Listesi: ",krediler)
print("Krediler Listesi Veri Tipi: ",type(krediler))
print("Krediler Listesi Uzunluğu: ",len(krediler))
#Liste Elemanlarına Erişim
print("Krediler Listesi 1. Elemanı: ",krediler[0])
print("Krediler Listesi 2. Elemanı: ",krediler[1])
print("Krediler Listesi 3. Elemanı: ",krediler[2])
print("Krediler Listesi 1. Elemanı: ",krediler[-3])
print("Krediler Listesi 2. Elemanı: ",krediler[-2])
print("Krediler Listesi 3. Elemanı: ",krediler[-1])

#Listelerde Fonksiyonlar
krediler.append("Eğitim Kredisi") #Listeye eleman eklemek için append() fonksiyonu kullanılır.
print("Krediler Listesi: ",krediler)
krediler.remove("Taşıt Kredisi") #Listeden eleman silmek için kullanılır.Elemanın değeri verilerek silinir.Aynı değere sahip birden fazla eleman varsa ilk bulunan silinir.
print("Krediler Listesi: ",krediler)
krediler.append("Taşıt Kredisi")
print("Krediler Listesi: ",krediler)
krediler.pop() #Listeden son elemanı silmek için kullanılır.Ancak parametre olarak index değeri verilirse o index değerindeki eleman silinir.Elemanın indexi verilerek silinir.
print("Krediler Listesi: ",krediler)
krediler.extend(["Tatil Kredisi","Sağlık Kredisi"]) #Listeye birden fazla eleman eklemek için kullanılır.
print("Krediler Listesi: ",krediler)

#Döngüler
print("--------------DÖNGÜLER--------------")
#For Döngüsü
print("--------------FOR DÖNGÜSÜ--------------")
for i in range(10): #range() fonksiyonu ile belirtilen aralıkta döngü oluşturulur.0'dan başlar ve belirtilen sayıya kadar döngü devam eder.Range içine verilen parametreler INT veri tipinde olmalıdır.
    print(i)
print("*"*10)
for i in range(5,10): #range() fonksiyonu ile belirtilen aralıkta döngü oluşturulur.Başlangıç ve bitiş değerleri belirtilir.
    print(i)
print("*"*10)
for i in range(0,10,2): #range() fonksiyonu ile belirtilen aralıkta döngü oluşturulur.Başlangıç,bitiş ve artış değerleri belirtilir.
    print(i)
print("------------Liste Üzerinde Döngü------------")
for kredi in krediler: #Liste üzerinde döngü oluşturulur.Krediler listesindeki her bir eleman kredi değişkenine atanır ve döngü içinde kullanılır. 
    print(kredi)
print("*"*20)
for i in range(len(krediler)): #Liste uzunluğu kadar döngü oluşturulur.
    print(krediler[i])

#While Döngüsü
print("--------------WHİLE DÖNGÜSÜ--------------")
i=0
while i<10: #Belirtilen koşul sağlandığı sürece döngü devam eder.
    print(i)
    i+=1
print("*"*10)
while True:
    print("X")
    break #Döngüyü sonlandırmak için break kullanılır.
print("*"*10)
i=0
while i<len(krediler):
    if krediler[i]=="Konut Kredisi": #Belirtilen koşul sağlandığında döngü sonlandırılır.
        break
    print(krediler[i])
    i+=1


#Fonksiyonlar
print("--------------FONKSİYONLAR--------------")
fiyat=100
indirim=20

def calculate(): #Fonksiyon tanımlanırken def anahtar kelimesi kullanılır.
    print(100-20) #Fonksiyon içinde yapılacak işlemler girilir.
calculate() #Fonksiyon çağrılır.

def calculateWithParams(a,b): #Fonksiyon parametre alabilir.Parametreler fonksiyon çağrılırken verilir.
    print(a-b)
calculateWithParams(100,20) #Fonksiyon çağrılırken parametreler verilir.

def sayHello(name):
    print(f"Merhaba {name}")
sayHello("Hacı Bayram")
sayHello("Ali")
sayHello("Veli")

def calculateAndReturn(price,discount):
    return price-discount #Fonksiyon sonucu return anahtar kelimesi ile döndürülür.

result=calculateAndReturn(100,20) #Fonksiyon çağrılır ve dönen değer result değişkenine atanır.
print(result)
