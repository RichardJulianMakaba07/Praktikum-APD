# cuaca = "Cerah"

# if cuaca == "Cerah":
#     print("Kamu pergi keluar rumah")

# cuaca = input("Masukan cuaca hari ini: ")
# if cuaca == "cerah":
#     print("Kamu keluar rumah")
    
# cuaca = input("Masukan cuaca hari ini: ")
# if cuaca == "cerah":
#     print("Kamu keluar rumah")
# else:
#     print("kamu tetap di rumah")
    
# cuaca = input("Masukan cuaca hari ini: ")
# if cuaca == "cerah":
#     print("Kamu keluar rumah")
# elif cuaca == "mendung":
#     print("baca komik")
# else:
#     print("kamu tidur")
    
# opsi = input("""Pilih menu:
# 1. kondisi 1
# 2. kondisi 2
# 3. kondisi 3
# Masukkan pilihan menu: """)

# if opsi == "1":
#     print("kondisi 1")
# elif opsi == "2":
#     print("kondisi 2")
# elif opsi == "3":
#     print("kondisi 3")
# else:
#     print("input tidak valid")

# umur = int(input("masukkan umur: "))
# if umur <0:
#     print("input tidak valid")
# elif (umur <= 10):
#     print("anak-anak")
# elif (umur <= 18):
#     print("remaja")
# elif (umur <= 60):
#     print("dewasa")

# angka = int(input("Masukkan angka: "))
# result = "genap" if angka % 2 == 0 else "ganjil"

# print(angka, "adalah angka", result)

# a = 10
# b = 20
# print("a lebih besar dari b") if a > b else print("a lebih kecil dari b") 

# if a > b:
#     print("a lebih besar dari b")
# else:
#     print("a lebih kecil dari b")

# string = ""
# int = 0
# print(bool(string))
# print(bool(int))

# #penggunaan and, or, not
# a = 10
# b = 20
# if a < b and a % 2 == 0:
#     print("a lebih kecil dari b dan a adalah bilangan genap")
# elif a > b or a % 2 == 0:
#     print("a lebih besar dari b atau a adalah bilangan genap")
# else:
#     print("a lebih kecil dari b dan a adalah bilangan ganjul")

print("""Pilih menu:
# 1. kondisi 1
# 2. kondisi 2
# 3. kondisi 3""")
opsi = input("pilih menu: ")
match opsi:
    case "1":
        print("kondisi 1")
    case "2":
        print("kondisi 2")
    case "3":
        print("kondisi 3")
    case _:
        print("input tidak valid")