# Python Temel Bilgiler Notları
# Bu dosya, Python'un temel özelliklerini ve kullanımını açıklamak için hazırlanmıştır.

# ======================================
# 1. Print Fonksiyonu
# ======================================
# Print, ekrana bir şeyler yazdırmak için kullanılır.
print("Merhaba Dünya!")  # Ekrana 'Merhaba Dünya!' yazdırır.

# ======================================
# 2. Değişkenler
# ======================================
# Değişkenler, verileri saklamak için kullanılır. Python'da tür belirtmeye gerek yoktur.
isim = "Osman"  # Metin (string) türünde bir değişken
yas = 14  # Sayı (integer) türünde bir değişken
boy = 1.70  # Ondalıklı sayı (float) türünde bir değişken

# Değişkenleri yazdırabiliriz:
print("Ad:", isim)
print("Yaş:", yas)
print("Boy:", boy)

# ======================================
# 3. Kullanıcıdan Veri Alma
# ======================================
# Kullanıcıdan veri almak için input() kullanılır.
# input() ile alınan veri her zaman string türündedir.
ad = input("Adınızı girin: ")  # Kullanıcıdan adını alır
print("Merhaba, " + ad + "!")  # Kullanıcının adını yazdırır

# ======================================
# 4. Koşullu İfadeler (if - else)
# ======================================
# Bir durumu kontrol etmek için if-else kullanılır.
sayi = int(input("Bir sayı girin: "))  # Kullanıcıdan bir sayı alıp int'e çevirir 
# int() içine girilen değeri eğer mümkün ise tamsayıya çevirir. Örnek: "1" = 1 gibi
if sayi > 0:
    print("Pozitif bir sayı girdiniz.")
elif sayi < 0:
    print("Negatif bir sayı girdiniz.")
else:
    print("Sayı sıfırdır.")

# ======================================
# 5. Döngüler
# ======================================
# For ve while döngüleriyle işlemler tekrar edilebilir.

# 5.1 For Döngüsü
for i in range(5):  # 0'dan 4'e kadar (5 dahil değil) sayıları yazdırır
    print("For döngüsü:", i)

# 5.2 While Döngüsü
# Bir şart sağlandığı sürece döner. SONSUZA KADAARRR!!!
x = 0
while x < 5:
    print("While döngüsü:", x)
    x += 1  # x'i bir artırır

# ======================================
# 6. Listeler
# ======================================
# Listeler birden fazla veriyi bir arada tutar.
meyveler = ["Elma", "Armut", "Muz", "Çilek"]  # Bir liste oluşturduk
print("Meyveler:", meyveler)

# Listeye eleman ekleyebiliriz:
meyveler.append("Kiraz")  # Listeye "Kiraz" ekler
print("Güncellenmiş liste:", meyveler)

# Liste elemanlarına erişim:
print("İlk meyve:", meyveler[0])  # İlk eleman (indeks 0)
print("Son meyve:", meyveler[-1])  # Son eleman

# ======================================
# 7. Fonksiyonlar
# ======================================
# Fonksiyonlar, kodu tekrar kullanmayı sağlar.
def selamla(isim):
    """Bu fonksiyon verilen ismi selamlar."""
    print("Merhaba, " + isim + "!")

# Fonksiyonu çağır:
selamla("Enver Printer")
selamla("Derya (yüce ve büyük adam)")

# ======================================
# 8. Dosya İşlemleri
# ======================================
# Bir dosyaya yazabilir ve okuyabiliriz.

# Yazma işlemi:
with open("anime_kizlari.txt", "w") as dosya:
    dosya.write("Bu bir dosyadır.\nMerhaba Dünya!")

# Okuma işlemi:
with open("anime_kizlari.txt", "r") as dosya:
    icerik = dosya.read()
    print("Dosya içeriği:\n", icerik)

# ======================================
# 9. Hata Yönetimi (try - except)
# ======================================
# Hataları yakalamak için kullanılır.
try:
    bolunen = int(input("Bölünen sayıyı girin: "))
    bolen = int(input("Bölen sayıyı girin: "))
    sonuc = bolunen / bolen
    print("Sonuç:", sonuc)
except ZeroDivisionError: # Python da belirli hata tipleri var. Hata yapa yapa ezberleyeceksin inan bana XD
    print("Bir sayı sıfıra bölünemez!")
except ValueError:
    print("Lütfen sadece sayı girin!")

# ======================================
# 10. Modüller
# ======================================
# Modüller, Python'un ekstra yetenekler kazanmasını sağlar.
import math  # Matematik modülünü ekler Eğer istersen sen de kendi modülünü yazıp buraya ekleyebilirsin
print("Pi sayısı:", math.pi)
print("5'in karesi:", math.pow(5, 2))

# ======================================
# Python'un Temelleri Bu Kadar!
# Umarım bu notlar öğrenmene yardımcı olur. :)
