# 1. Kullanıcının adını, yaşını, boyunu (metre cinsinden) al
# 2. Öncelikle merhaba ile kullanıcıyı selamla
# 3. Kullanıcının 5 yıl sonraki yaşını, ve boyunun 50cm fazlasını ekrana yazdır.

isim = input("İsminizi giriniz: ")
yas = int(input("Yaşınızı giriniz: "))
boy = float(input("Boyunuzu metre cinsinden giriniz: "))

sonraki_yas = yas +5
uzun_boy = boy + 0.5

print("Merhaba ",isim,"!")
print("5 Yıl sonraki yaşınız: ",sonraki_yas)
print("Boyunuzun 50cm fazlası: ",uzun_boy)