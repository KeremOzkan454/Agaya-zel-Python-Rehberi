# 1. Kullanıcıdan 5 adet kelime al ve bunları bir listeye ekle.
# 2. Bu listeyi alfabetik olarak kullanıcıya döndür
# Örneğin: kullanıcı "elma","armut","karpuz","şeftali","enver" yazmış olsun
# Senin görevin yukarıda yazan kelimeleri alfabetik olarak kullanıcıya döndürmek olacak. Bol şans :)

ilk_liste_elemani = input("İlk kelimeyi giriniz: ")
ikinci_liste_elemani = input("İkinci kelimeyi giriniz: ")
ucuncu_liste_elemani = input("Üçüncü kelimeyi giriniz: ")
dorduncu_liste_elemani = input("Dördüncü kelimeyi giriniz: ")
besinci_liste_elemani = input("Beşinci kelimeyi giriniz: ")

my_list = []

my_list.append(ilk_liste_elemani)
my_list.append(ikinci_liste_elemani)
my_list.append(ucuncu_liste_elemani)
my_list.append(dorduncu_liste_elemani)
my_list.append(besinci_liste_elemani)

my_list.sort()

print("Girdiğiniz değerlerin alfabetik sıraya göre sıralanmış hali: ")

for eleman in my_list:
    print(eleman)