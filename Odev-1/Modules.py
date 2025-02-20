#Moduls =>Moduller
print("-----------------Modules-----------------")
#Alias => Takma İsim
import Matematik as mat
#Built-in Modules => Python ile birlikte gelen modüller
import random
#Modülden sadece istenen fonksiyon alınabilir.
from Matematik import topla as sum
#Modülden classta alınabilir.
from Class_Modules_Package import Human


print(mat.topla(3,4))
print(mat.bol(16,4))

print(random.randint(1,100)) #1 ile 100 arasında rastgele sayı üretir.

human1 = Human("Ali")
human1.talk("Merhaba") #Sınıf içindeki metodda self parametresi olmazsa hata verir.
human1.walk()

#Package => Kütüphaneler
print("-----------------Package-----------------")
from selenium import webdriver
tarayici = webdriver.Chrome() #Tarayıcıyı açar.
tarayici.get("https://www.google.com") #Google sitesine gider.



