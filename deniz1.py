#1. soru
sayi = input('Sayıyı Girin : ')
tekToplam=0
ciftToplam=0
for i in range(1,int(sayi)):
      if(i%2==0):
            ciftToplam+=i
      else:
            tekToplam+=i
print("Tek Sayıların Toplamı : {0}".format(tekToplam))
print("Çift Sayıların Toplamı : {0}".format(ciftToplam))



#3. soru
from functools import reduce

notlar =  [[1,("A", 34), ("O", 5), ("F", 67)], [2,("A", 67), ("F", 88)], [3,("A", 44), ("O", 5), ("F", 78)], [4,("A", 99), ("O", 5), ("F", 65)]]

sonuc = list(map(lambda x: [x[0]] + list(map(lambda y: (y[1]*0.4) if (y[0] == "A") else ( ( y[1] * 1) if ((y[0] == "O")) else ( y[1] * 0.6) ), x[1:]))   ,notlar))
print(sonuc)
sonuc = list(map(lambda a: [a[0]] + ["Gecti" if a[1] >= 50 else "Kaldi"], list(map(lambda x: [x[0]] + [reduce(lambda y,z: y+z , x[1:])] , sonuc))))
print(sonuc)


#4. soru
print("2 Bilinmeyenli Denklem ")

a=int(input("A sayısını giriniz:"))
b=int(input("B sayısını giriniz:"))
c=int(input("C sayısını giriniz:"))
delta=b**2-4*a*c
x1 = (-b - delta ** 0.5)/ (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)
if delta<0:
    print("Reel kök yoktur.")
if delta==0:
    print("Çakışık 2 kök vardır.")
print("Denkleminizin birinci kökü:{}\n Denkleminizin ikinci kökü:{}\n".format(x1,x2))
if delta>0:
    print("Gerçek 2 kök vardır.")
    print("Denkleminizin birinci kökü:{}\n Denkleminizin ikinci kökü:{}\n".format(x1,x2))