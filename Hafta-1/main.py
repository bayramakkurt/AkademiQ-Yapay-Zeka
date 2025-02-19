print("Hello World")

print("-----------------")
#DEĞİŞKENLER
name="Hacı Bayram" #String türünde değişken
print("İSİM: "+name)
age=22             #Integer türünde değişken
print("YAŞ: ",age)
print("age değişkeninin değişken tipi: ",type(age)) #Değişkenin türünü öğrenmek için kullanılır.
age=22.5           #Float türünde değişken
print("YAŞ: ",age)
print("age değişkeninin değiştikten sonraki değişken tipi: ",type(age)) #Değişkenin türünü öğrenmek için kullanılır.
#Python programlama dili TYPE-SAFE değildir. Yani bir değişkenin türünü belirtmek zorunda değilsiniz.

print("-----------------")
#ARİTMETİK OPERATÖRLER
a=10
b=5
print("a+b Sonucu: ",a+b)
print("a-b Sonucu: ",a-b)
print("a*b Sonucu: ",a*b)
print("a/b Sonucu: ",a/b)
print("a//b Sonucu: ",a//b) #Bölme işleminden sonra tam kısmı alır.
print("a**b Sonucu: ",a**b) #Üs alma işlemi yapar.
print("a%b Sonucu: ",a%b)   #Mod alma işlemi yapar.

print("-----------------")
#KARŞILAŞTIRMA OPERATÖRLERİ
a=10
b=5
print("a>b Sonucu: ",a>b)
print("a<b Sonucu: ",a<b)
print("a>=b Sonucu: ",a>=b)
print("a<=b Sonucu: ",a<=b)
print("a==b Sonucu: ",a==b)
print("a!=b Sonucu: ",a!=b)

print("-----------------")
#ATAMA OPERATÖRLERİ
a=10
b=5
a+=b #a=a+b
print("a+=b Sonucu: ",a)
a-=b #a=a-b
print("a-=b Sonucu: ",a)
a*=b #a=a*b
print("a*=b Sonucu: ",a)
a/=b #a=a/b
print("a/=b Sonucu: ",a)
a//=b #a=a//b
print("a//=b Sonucu: ",a)
a**=b #a=a**b
print("a**=b Sonucu: ",a)
a%=b #a=a%b
print("a%=b Sonucu: ",a)

print("-----------------")

#MANTIKSAL OPERATÖRLER
a=True
b=False
print("a and b Sonucu: ",a and b)
print("a or b Sonucu: ",a or b)
print("not a Sonucu: ",not a)

print("-----------------")

students=["Hacı Bayram","Ali","Veli","Ayşe","Fatma"]
print(students)
print(type(students))
print(students[0])
students.append("Mehmet")
print(students)
students.remove("Ali")
print(students)
students.pop(1)
print(students)
students.insert(1,"Ali")

