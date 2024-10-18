# def aku_fungsi():
#     print("helllo world")
    
# aku_fungsi()

# def tambah(a,b):
#     hasil = a+b
#     print(hasil)
    
# tambah(10,2)

# def tambah(a,b):
#     hasil = a+b
#     return hasil

# print(tambah(2,4))

# def tambah(a,b):
#     hasil = a+b
#     return 2

# print(tambah(2,4) + tambah(4,6))

# def pilihan(opsi):
#     match opsi:
#         case 1:
#             print(1)
#             return
#         case 2:
#             print(2)
#             return
    
#     print(3)
# # pilihan(2)

# def cetak(nama,nim,matkul):
#     print(nama,nim,matkul)
    
# cetak("fathir", 41,"kalkulus")

# def cetak(nama,nim,*matkul): #(*)menampung nilai sisa ke matkul dan bertipe tuple
#     print(nama,nim,matkul)
    
# cetak("fathir", 41,"kalkulus", "fisdas")

# def cetak(nama,nim,**matkul): #(**)menampung nilai sisa ke matkul dan bertipe dictionary
#     print(nama,nim,matkul)
    
# cetak("fathir", 41,kalkulus=2, fisdas=5, pti=4)

# rumus: sisi x sisi
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# # rumus: sisi x sisi x sisi
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)
# # pemanggilan Fungsi
# luas_persegi(4)
# volume_persegi(6)

# var = 2,4,5
# var1,var2,var3 = var
# print(var)
# print(var1)
# print(var2)
# print(var3)

# membuat variabel global
# Nama = "Informatika"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# kelas = "IT Asik"
# # membuat variabel lokal
# def info():
#     Nama = "Teknik Elektro"
#     Mata_Kuliah = "Pengantar Teknik ELektro"
#     # mengakses variabel lokal
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)
#     print(kelas)
# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)
# # memanggil fungsi info
# info()

# if __name__ == "__main__":
#     def cetak(nama,nim,matkul):
#         print(nama,nim,matkul)
    
def tambah(a,b):
    return a+b
print(tambah(3,4))