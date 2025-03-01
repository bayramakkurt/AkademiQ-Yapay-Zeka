#Object-Oriented Programming
print("-----------------Object-Oriented Programming-----------------")
#Class => Sınıf 
class Car():
    #Attributes => Özellikler
    #Constructor => Yapıcı Metod, Classtan bir nesne oluşturulduğunda ilk çalışan metoddur.
    def __init__(self,model,color,year): #Her classın rezerved bir metodu olan __init__ metodu ile classın yapıcı metodunu tanımlarız.Rezerved bir metot olduğu için başına ve sonuna iki tane alt çizgi koyarız.
        self.__model = model   # Metodun çalıştığı sınıfın özelliklerine erişmek için kullanılır.Her metodun ilk parametresi self olmalıdır.
        self.__color = color
        self.__year = year

    #Encapsulation => Kapsülleme
    def setModel(self,model):
        if len(model) >= 3:
            self.__model = model
        else:
            print("Model name must be at least 3 characters.")
    def getModel(self):
        return self.__model
    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color
    def setYear(self,year):
        self.__year = year
    def getYear(self):
        return self.__year
    

    #Methods => Metodlar
    def start(self): #self => Metodun çalıştığı sınıfın özelliklerine erişmek için kullanılır.Her metodun ilk parametresi self olmalıdır.
        print(f"{self.__model} is starting")
    def stop(self): #self => Self classın kendisini temsil eder.
        print(f"{self.__model} is stopping") #self.model => self classın model özelliğine erişmek için kullanılır.Sadece model yazsak hata alırız.

#Instance => Örnek
car1 = Car("Audi","White",2018) #Nesne oluşturulurken yapıcı metot çalışır.
car1.start()
car1.stop()
print(car1.getModel())
print(car1.getColor())
print(car1.getYear())

car2 = Car("Mercedes","Black",2016) #Nesne oluşturulurken yapıcı metot çalışır.
car2.start()
car2.setModel("Toyota") #Nesne özelliklerini değiştirebiliriz.
car2.setColor("Red")
car2.setYear(2020)
car2.start()
car2.stop()
print(car2.getModel())
print(car2.getColor())
print(car2.getYear())

#Inheritance => Kalıtım
print("-----------------Inheritance-----------------")
class Vehicle():
    def __init__(self,model):
        self.model=model
    def start(self):
        print(f"{self.model} Vehicle is starting")

class Car(Vehicle): #Car classı Vehicle classından kalıtım alır.
    def some_car_function(self):
        print("This is some car function")
    def start(self): #Car classının yapıcı metodunu override eder.Method Overriding => Bir metodun üzerine yazma işlemidir.Polymorphism için kullanılır.
        print(f"{self.model} Car is starting")

class Truck(Vehicle):
    def __init__(self, model,capacity): #Truck classının yapıcı metodunu override eder.
        super().__init__(model) #Super classın yapıcı metodunu çağır
        self.capacity = capacity

    def load_weight(self):
        print(f"{self.model} Truck is loading weight")


car = Car("Audi")
car.start()
car.some_car_function()

truck = Truck("Mercedes",1000)
truck.start()
truck.load_weight()
