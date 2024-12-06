def toplama():
	sayi1 = int(input("Toplanacak İlk sayı >>> "))
	sayi2 = int(input("Toplanacak İkinci sayı >>> "))
	print(sayi1+sayi2)

def cikarma():
	sayi1 = int(input("Çıkarılacak İlk sayı >>> "))
	sayi2 = int(input("Çıkarılacak İkinci sayı >>> "))
	print(sayi1-sayi2)

def bolme():
	sayi1 = int(input("Bölünecek İlk sayı >>> "))
	sayi2 = int(input("Bölünecek İkinci sayı >>> "))
	print(sayi1/sayi2)

def carpma():
	sayi1 = int(input("Çarpılacakİlk sayı >>> "))
	sayi2 = int(input("Çarpılacak İkinci sayı >>> "))
	print(sayi1*sayi2)


print("Toplama için 1\nÇıkarma için 2\nBölme için 3\nÇarpma için 4\nÇıkmak için 5 tuşlayınız.")

while True:
	user_input = input("işlem türünü giriniz: ")
	if user_input == "1":
		toplama()
	elif user_input == "2":
		cikarma()
	elif user_input == "3":
		bolme()
	elif user_input == "4":
		carpma()
	elif user_input == "5":
		break
	else:
		print("Geçersiz sayı girişi!")

