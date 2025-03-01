#Modules => Kütüphaneler
#Kütüphaneler => Python'da hazır olarak bulunan ve bizim işimizi kolaylaştıran fonksiyonlar topluluğudur.
print("-----------------Modules-----------------")

import math #math kütüphanesini ekledik.Math kütüphanesindeki bütün fonksiyonları kullanabiliriz.
from math import sqrt #math kütüphanesinden sadece sqrt fonksiyonunu ekledik.Math kütüphanesindeki sadece sqrt fonksiyonunu kullanabiliriz.
from math import sqrt as karekok #math kütüphanesinden sadece sqrt fonksiyonunu ekledik ve karekok adıyla kullanabiliriz.

print(math.sqrt(16))
print(sqrt(16))
print(karekok(16))


from main import Car #main.py dosyasındaki Car classını ekledik.
car3 = Car("Opel")
car3.start()

#Kendi modülümüzü oluşturduk ve bu modülü kullanarak Car classını ekledik.

#Dışarıdan modül ekleme
print("-----------------External Modules-----------------")
import requests #requests kütüphanesini ekledik.
response = requests.get("https://www.google.com")
print(response.status_code)

