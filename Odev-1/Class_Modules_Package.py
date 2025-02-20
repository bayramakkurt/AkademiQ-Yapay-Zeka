from Human import Human
#Class => Sınıf
print("-----------------Class-----------------")
#İnstance => Örnek
human1 = Human("Ali")
human1.talk("Merhaba") #Sınıf içindeki metodda self parametresi olmazsa hata verir.
human1.walk()
print(human1) #Oluşturulan nesne değişkenini print edince bu metot çalışır. Ali
    
human2=Human("Veli")
human2.talk("Nasılsın")
human2.walk()
print(human2) #Oluşturulan nesne değişkenini print edince bu metot çalışır. Veli




