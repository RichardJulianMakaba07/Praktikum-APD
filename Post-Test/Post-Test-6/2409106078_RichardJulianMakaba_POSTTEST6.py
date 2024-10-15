daftar_pemain = {
    "19": {"nama": "Lamine Yamal", "posisi": "Penyerang", "no_punggung": "19"},
    "9": {"nama": "Robert Lewandowski", "posisi": "Penyerang", "no_punggung": "9"},
    "21": {"nama": "Frankie De Jong", "posisi": "Gelandang", "no_punggung": "21"},
    "24": {"nama": "Eric Garcia", "posisi": "Back", "no_punggung": "24"},
    "1": {"nama": "Marc Ter Stegen", "posisi": "Kiper", "no_punggung": "1"}
}

# Dictionary untuk menyimpan data pengguna [username: {password, role}]
daftar_pengguna = {
    "admin": {"password": "admin123", "role": "admin"}
}

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
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        
        if not username or not password:
            print("Username atau password tidak boleh kosong!\n")
        elif username in daftar_pengguna:
            print("Username sudah terdaftar!\n")
        else:
            daftar_pengguna[username] = {"password": password, "role": "user"}
            print(f"Registrasi berhasil! Anda sekarang terdaftar sebagai '{username}'.\n")

    elif pilihan == "2":
        print("\n=== Login Pengguna ===")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        
        if username in daftar_pengguna and daftar_pengguna[username]["password"] == password:
            role = daftar_pengguna[username]["role"]
            print(f"Login berhasil! Anda masuk sebagai {role}.")

            if role == "admin":
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
                        try:
                            nama = input("Masukkan nama pemain: ").strip()
                            posisi = input("Masukkan posisi pemain: ").strip()
                            no_punggung = input("Masukkan nomor punggung pemain: ").strip()

                            if not nama or not posisi or not no_punggung:
                                raise ValueError("Nama, posisi, atau nomor punggung tidak boleh kosong.")
                            
                            daftar_pemain[no_punggung] = {"nama": nama, "posisi": posisi, "no_punggung": no_punggung}
                            print(f"Pemain {nama} berhasil ditambahkan.\n")
                        except ValueError as e:
                            print(f"{e}\n")

                    elif pilihan_admin == "2":
                        print("\n=== Daftar Pemain Barcelona 24/25 ===")
                        for pemain in daftar_pemain.values():
                            print(f"Nama: {pemain['nama']}, Posisi: {pemain['posisi']}, No.Punggung: {pemain['no_punggung']}")

                    elif pilihan_admin == "3":
                        print("\n=== Update Pemain ===")
                        for no_punggung, pemain in daftar_pemain.items():
                            print(f"No.Punggung: {no_punggung}, Nama: {pemain['nama']}, Posisi: {pemain['posisi']}")

                        no_punggung = input("\nMasukkan nomor punggung pemain yang ingin diupdate: ").strip()
                        
                        if no_punggung in daftar_pemain:
                            try:
                                nama_baru = input("\nMasukkan nama baru: ").strip()
                                posisi_baru = input("Masukkan posisi baru: ").strip()
                                
                                if not nama_baru or not posisi_baru:
                                    raise ValueError("Nama atau posisi tidak boleh kosong.")
                                
                                daftar_pemain[no_punggung] = {"nama": nama_baru, "posisi": posisi_baru, "no_punggung": no_punggung}
                                print(f"Pemain berhasil diupdate menjadi: {nama_baru}, {posisi_baru}, {no_punggung}\n")
                            except ValueError as e:
                                print(f"{e}\n")
                        else:
                            print("Nomor punggung tidak ditemukan.\n")

                    elif pilihan_admin == "4":
                        print("\n=== Hapus Pemain ===")
                        for no_punggung, pemain in daftar_pemain.items():
                            print(f"No.Punggung: {no_punggung}, Nama: {pemain['nama']}, Posisi: {pemain['posisi']}")
                        
                        no_punggung = input("\nMasukkan nomor punggung pemain yang ingin dihapus: ").strip()
                        if no_punggung in daftar_pemain:
                            pemain_terhapus = daftar_pemain.pop(no_punggung)
                            print(f"Pemain {pemain_terhapus['nama']} berhasil dihapus.\n")
                        else:
                            print("Nomor punggung tidak ditemukan.\n")
                            
                    elif pilihan_admin == "5":
                        print()
                        break
                    else:
                        print("Pilihan tidak valid!\n")

            elif role == "user":
                while True:
                    print("\n=== Menu Pengguna ===")
                    print("1. Tampilkan Pemain")
                    print("2. Logout")
                    
                    pilihan_user = input("Pilih menu (1-2): ")

                    if pilihan_user == "1":
                        print("\n=== Daftar Pemain Barcelona 24/25 ===")
                        for pemain in daftar_pemain.values():
                            print(f"Nama: {pemain['nama']}, Posisi: {pemain['posisi']}, No.Punggung: {pemain['no_punggung']}")
                    
                    elif pilihan_user == "2":
                        print()
                        break
                    else:
                        print("Pilihan tidak valid!\n")
        else:
            print("Login gagal! Username atau password salah.\n")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan program!")
        break
    else:
        print("Pilihan tidak valid! Coba lagi.\n")
