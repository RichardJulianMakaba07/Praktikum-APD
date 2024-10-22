daftar_pemain = {
    "19": {"nama": "Lamine Yamal", "posisi": "Penyerang", "no_punggung": "19"},
    "9": {"nama": "Robert Lewandowski", "posisi": "Penyerang", "no_punggung": "9"},
    "21": {"nama": "Frankie De Jong", "posisi": "Gelandang", "no_punggung": "21"},
    "24": {"nama": "Eric Garcia", "posisi": "Back", "no_punggung": "24"},
    "1": {"nama": "Marc Ter Stegen", "posisi": "Kiper", "no_punggung": "1"}
}

# dictionary untuk menyimpan data pengguna {username: {password, role}}
daftar_pengguna = {
    "admin": {"password": "admin123", "role": "admin"}
}

user_role = None

def input_valid(pesan):
    try:
        pilihan = input(pesan).strip()
        if not pilihan:
            raise ValueError("Input tidak boleh kosong.\n")
        return pilihan
    except ValueError as e:
        print(f"{e}")
        return input_valid(pesan)
    
def tambah_pemain(nama, posisi, no_punggung):
    if no_punggung in daftar_pemain:
        print(f"Nomor punggung {no_punggung} sudah ada, pemain tidak bisa ditambahkan.\n")
    else:
        daftar_pemain[no_punggung] = {"nama": nama, "posisi": posisi, "no_punggung": no_punggung}
        print(f"Pemain {nama} berhasil ditambahkan.\n")

def tampilkan_pemain():
    print("\n=== Daftar Pemain Barcelona 24/25 ===")
    for pemain in daftar_pemain.values():
        print(f"No.Punggung: {pemain['no_punggung']}, Nama: {pemain['nama']}, Posisi: {pemain['posisi']}")
    print()

def update_pemain(no_punggung):
    if no_punggung in daftar_pemain:
        nama_baru = input_valid("Masukkan nama baru: ")
        posisi_baru = input_valid("Masukkan posisi baru: ")
        daftar_pemain[no_punggung] = {"nama": nama_baru, "posisi": posisi_baru, "no_punggung": no_punggung}
        print(f"Pemain dengan nomor punggung {no_punggung} berhasil diupdate menjadi {nama_baru}, {posisi_baru}.\n")
    else:
        print("Nomor punggung tidak ditemukan.\n")
        
def hapus_pemain():
    no_punggung = input_valid("Masukkan nomor punggung pemain yang ingin dihapus: ")
    if no_punggung in daftar_pemain:
        pemain_terhapus = daftar_pemain.pop(no_punggung)
        print(f"Pemain {pemain_terhapus['nama']} berhasil dihapus.\n")
    else:
        print("Nomor punggung tidak ditemukan.\n")
    

def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Pemain")
        print("2. Tampilkan Pemain")
        print("3. Update Pemain")
        print("4. Hapus Pemain")
        print("5. Logout")
        
        pilihan_admin = input("Pilih menu (1-5): ")

        if pilihan_admin == "1":
            print("\n=== Tambah Pemain ===")
            nama = input_valid("Masukkan nama pemain: ")
            posisi = input_valid("Masukkan posisi pemain: ")
            no_punggung = input_valid("Masukkan nomor punggung pemain: ")
            tambah_pemain(nama, posisi, no_punggung)

        elif pilihan_admin == "2":
            tampilkan_pemain()

        elif pilihan_admin == "3":
            tampilkan_pemain()
            no_punggung = input_valid("Masukkan nomor punggung pemain yang ingin diupdate: ")
            update_pemain(no_punggung)
        
        elif pilihan_admin == "4":
            tampilkan_pemain()
            hapus_pemain()

        elif pilihan_admin == "5":
            print()
            break
        else:
            print("Pilihan tidak valid!\n")

def menu_user():
    while True:
        print("\n=== Menu Pengguna ===")
        print("1. Tampilkan Pemain")
        print("2. Logout")
        
        pilihan_user = input("Pilih menu (1-2): ")

        if pilihan_user == "1":
            tampilkan_pemain()
        
        elif pilihan_user == "2":
            print()
            break
        else:
            print("Pilihan tidak valid!\n")

while True:
    print("=== Menu Utama ===")
    print("Selamat datang di list pemain sepakbola Barcelona 24/25")
    print('Silakan pilih "Registrasi" jika belum membuat akun, dan jika sudah memiliki akun silahkan pilih "Login"')
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1-3): ")
    
    if pilihan == "1":
        print("\n=== Registrasi Pengguna ===")
        username = input_valid("Masukkan username: ")
        password = input_valid("Masukkan password: ")
        
        if username in daftar_pengguna:
            print("Username sudah terdaftar!\n")
        else:
            daftar_pengguna[username] = {"password": password, "role": "user"}
            print(f"Registrasi berhasil! Anda sekarang terdaftar sebagai '{username}'.\n")

    elif pilihan == "2":
        print("\n=== Login Pengguna ===")
        username = input_valid("Masukkan username: ")
        password = input_valid("Masukkan password: ")
        
        if username in daftar_pengguna and daftar_pengguna[username]["password"] == password:
            user_role = daftar_pengguna[username]["role"]
            print(f"Login berhasil! Anda masuk sebagai {user_role}.")

            if user_role == "admin":
                menu_admin()
            elif user_role == "user":
                menu_user()
        else:
            print("Login gagal! Username atau password salah.\n")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan program!")
        break
    else:
        print("Pilihan tidak valid! Coba lagi.\n")
