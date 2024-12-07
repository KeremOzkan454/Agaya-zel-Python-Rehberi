# 1. python da varsayılan olarak gelen "random" kütüphanesi ile bir sayı tahmin oyunu yap
# 2. Program 1-100 arası bir sayı belirlesin (1 ve 100 dahil)
# 3. Kullanıcıdan bu sayıyı tahmin etmesini istesin. 
# -- Yanlış bildiğinde daha büyük ya da daha küçük gibi yanıtlar versin. 
# -- Bildiğinde de kullanıcıyı tebrik etsin. Ve program sonlansın.

import random

random_sayi = random.randint(1,100)

while True:
    user_input = int(input("Tahmin ettiğim sayıyı bul bakalım :"))
    if user_input == random_sayi:
        print("Tebrikler tuttuğum sayı ",random_sayi," idi!")
        break
    elif user_input > random_sayi:
        print("Daha küçük bir sayı")
    elif user_input < random_sayi:
        print("Daha büyük bir sayı")
