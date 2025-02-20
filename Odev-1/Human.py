#Class => Sınıf
print("-----------------Class-----------------")
#Self => This
class Human:
    #Buil-in Attribute => __init__ => Constructor
    def __init__(self,name): #__init__ =>İnitilaze => Başlatmak. Her örnek oluşturulduğunda çalışır.
        self.name=name
        print("Human created")

    def __str__(self) -> str: #-> str => Dönüş tipi, Fonksiyon ise oluşturulan nesne değişkeni print edilince bu metot çalışır.
        return f"Oluşturulan nesne değişkenini print edince bu metot çalışır. {self.name}"
        
    
    def talk(self,sentence): #self => İlgili sınıfın örneğini alır.Class içindeki değişkenlere erişmek için self.degiskenAdi şeklinde kullanılır.Fonksiyonda parametre olarak aynı değişken isminde bir parametre alınırsa ve class içindeki aynı isimdeki parametreyi kullanmak için bu fark self ile sağlanır.
        print(f"{self.name} is talking...{sentence}")
    def walk(self): #self => İlgili sınıfın örneğini alır.
        print(f"{self.name} is walking...")
