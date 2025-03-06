#•	Kullanıcının girdiği metni bir .txt dosyasına yazan bir Python programı yazın.

metin=input("Yazdırmak istediğiniz metni giriniz: ")

dosya=open("c:/Users/HBA/Desktop/AkademiQ Yapay Zeka/Odev-3/odev-3.txt","w",encoding="utf-8")
dosya.write(metin)
dosya.close()
print("Metin dosyaya yazıldı.")

#•	Daha sonra yazılan bu dosyayı okuyarak içeriğini ekrana yazdırın.

dosya=open("c:/Users/HBA/Desktop/AkademiQ Yapay Zeka/Odev-3/odev-3.txt","r",encoding="utf-8")
print(dosya.read())
dosya.close()
print("Metin dosyadan okundu.")

#•	Kullanıcıdan alınan 5 farklı satır verisini bir dosyaya kaydedin ve ardından bu dosyadaki verileri satır satır okuyarak ekrana yazdırın.

satir1=input("1. satırı giriniz: ")
satir2=input("2. satırı giriniz: ")
satir3=input("3. satırı giriniz: ")
satir4=input("4. satırı giriniz: ")
satir5=input("5. satırı giriniz: ")

dosya=open("c:/Users/HBA/Desktop/AkademiQ Yapay Zeka/Odev-3/odev-3.txt","w",encoding="utf-8")
dosya.write(satir1+"\n")
dosya.write(satir2+"\n")
dosya.write(satir3+"\n")
dosya.write(satir4+"\n")
dosya.write(satir5)
dosya.close()
print("Satırlar dosyaya yazıldı.")

dosya=open("c:/Users/HBA/Desktop/AkademiQ Yapay Zeka/Odev-3/odev-3.txt","r",encoding="utf-8")
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
dosya.close()
print("Satırlar dosyadan okundu.")
