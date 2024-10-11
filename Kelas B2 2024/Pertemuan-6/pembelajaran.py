# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_buku = {}
# print(daftar_buku)
# daftar_buku["novel 1"] = "senyum pertama di pagi hari airin"
# daftar_buku[1] = "matahari"
# print(daftar_buku)

# daftar_buku = dict(buku1 = "harry potter", buku2 = "percy jakson")
# print(daftar_buku)

# print(daftar_buku["buku2"])
# print(daftar_buku.get("buku2"))

# nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# for i in nilai:
#     print(i)
    
# for i, j in nilai.items():
#     print(f"Nilai dari {i} itu valuenya adalah : {j}")
# for i, j in nilai.items():
#     print(j)

# nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# nilai["Matematika"] = 69
# print(nilai)
# nilai.update({"Struktur data" : 99})
# nilai.update({"Matematika" : 99})
# print(nilai)

# nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# print(nilai)
# trashbin = nilai.pop("Matematika")
# print(nilai)
# print(trashbin)

# del nilai["Fisika"]
# print(nilai)

# nilai.clear()
# print(nilai)

# nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# print(f"berapa banyak nilai adalah {len(nilai)}")

# daftar_nilai = nilai.copy()
# print(daftar_nilai)

# import os
# import datetime as dt
# import pandas

# os.system("cls")
# key = "motor", "mobil", "sepeda"
# value = 2
# daftar_kendaraan = dict.fromkeys(key, value)
# print(daftar_kendaraan)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "The Paris"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# # mengakses key dan value dari dictionary
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     #mengambil nilai dari list
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18, "hobi" : ["membaca", "menulis", "ngoding"]}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")
    
# print(mahasiswa[111]["Umur"])
# print(mahasiswa[111]["hobi"][-1])

