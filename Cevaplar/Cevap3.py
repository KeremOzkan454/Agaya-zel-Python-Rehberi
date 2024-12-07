# 1. Kullanıcıdan bir şifre girmesini iste
# 2. Eğer şifre "Python123" ise ekrana "Giriş başarılı!" yazdır
# 3. Eğer şifre yanlış ise ekrana "Hatalı şifre!" yazdır

sifre = input("Şifreyi giriniz: ")

if sifre == "Python123":
    print("Giriş başarılı!")
else:
    print("Hatalı şifre!")