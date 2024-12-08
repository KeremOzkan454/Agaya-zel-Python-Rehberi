# Amacın burada hesap makinesi yapmak AMA!!
# Bu hesap makinesini yaparken fonksiyon kullanmak zorundasın.
# Ayrıca kullanıcı çık komutu verene kadar hesap makinesi işlem yapmayı sürdürecek.


def toplama():
    sayi1 = float(input("İlk sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))

    print(sayi1+sayi2)

def cikarma():
    sayi1 = float(input("İlk sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))

    print(sayi1-sayi2)

def carpma():
    sayi1 = float(input("İlk sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))

    print(sayi1*sayi2)

def bolme():
    sayi1 = float(input("İlk sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))

    print(sayi1/sayi2)


while True:
    print("Toplama içi 1")
    print("Çıkarma için 2")
    print("Çarpma için 3")
    print("Bölme için 4")
    user_input = input("Çıkış yapmak için 5 tuşlayınız: ")

    if user_input == "1":
        toplama()
    elif user_input == "2":
        cikarma()
    elif user_input == "3":
        carpma()
    elif user_input == "4":
        bolme()
    elif user_input == "5":
        break
    else:
        print("Lütfen geçerli bir sayı giriniz!!")