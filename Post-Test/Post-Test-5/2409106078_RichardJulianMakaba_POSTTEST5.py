daftar_pemain = [["Lamine Yamal", "Penyerang", "19"],
                 ["Robert Lewandowski", "Penyerang", "9"],
                 ["Frankie De Jong", "Gelandang", "21"],
                 ["Eric Garcia", "Back", "24"],
                 ["Marc Ter Stegen", "Kiper", "1"]]

# List untuk menyimpan data pengguna [username, password, role]
daftar_pengguna = [["admin", "admin123", "admin"]]

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
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        terdaftar = False
        for user in daftar_pengguna:
            if user[0] == username:
                print("Username sudah terdaftar!\n")
                terdaftar = True
                break
        
        if not terdaftar:
            daftar_pengguna.append([username, password, "user"])
            print(f"Registrasi berhasil! Anda sekarang terdaftar sebagai '{username}'.\n")

    elif pilihan == "2":
        print("\n=== Login Pengguna ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        role = None
        for user in daftar_pengguna:
            if user[0] == username and user[1] == password:
                print(f"Login berhasil! Anda masuk sebagai {user[2]}.")
                role = user[2]
                break
        
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
                    nama = input("Masukkan nama pemain: ")
                    posisi = input("Masukkan posisi pemain: ")
                    no_punggung = input("Masukkan nomor punggung pemain: ")
                    daftar_pemain.append([nama, posisi, no_punggung])
                    print(f"Pemain {nama} berhasil ditambahkan.\n")

                elif pilihan_admin == "2":
                    print("\n=== Daftar Pemain Barcelona 24/25 ===")
                    for i, pemain in enumerate(daftar_pemain):
                        print(f"{i + 1}. Nama: {pemain[0]}, Posisi: {pemain[1]}, No.Punggung: {pemain[2]}")

                elif pilihan_admin == "3":
                    print("\n=== Update Pemain ===")
                    for i, pemain in enumerate(daftar_pemain):
                        print(f"{i + 1}. Nama: {pemain[0]}, Posisi: {pemain[1]}, No.Punggung: {pemain[2]}")
                    
                    try:
                        nomor = int(input("Masukkan nomor pemain yang ingin diupdate: ")) - 1
                        if nomor < 0 or nomor >= len(daftar_pemain):
                            print("Nomor tidak ditemukan.\n")
                        else:
                            nama_baru = input("Masukkan nama baru: ")
                            posisi_baru = input("Masukkan posisi baru: ")
                            no_punggung_baru = input("Masukkan nomor punggung baru: ")
                            daftar_pemain[nomor] = [nama_baru, posisi_baru, no_punggung_baru]
                            print(f"Pemain berhasil diupdate menjadi: {nama_baru}, {posisi_baru}, {no_punggung_baru}\n")
                    except ValueError:
                        print("Input tidak valid! Masukkan nomor yang benar.\n")

                elif pilihan_admin == "4":
                    print("\n=== Hapus Pemain ===")
                    for i, pemain in enumerate(daftar_pemain):
                        print(f"{i + 1}. Nama: {pemain[0]}, Posisi: {pemain[1]}, No.Punggung: {pemain[2]}")
                    
                    try:
                        nomor = int(input("Masukkan nomor pemain yang ingin dihapus: ")) - 1
                        if nomor < 0 or nomor >= len(daftar_pemain):
                            print("Nomor tidak ditemukan.\n")
                        else:
                            pemain_terhapus = daftar_pemain.pop(nomor)
                            print(f"Pemain {pemain_terhapus[0]} berhasil dihapus.\n")
                    except ValueError:
                        print("Input tidak valid! Masukkan nomor yang benar.\n")

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
                    for i, pemain in enumerate(daftar_pemain):
                        print(f"{i + 1}. Nama: {pemain[0]}, Posisi: {pemain[1]}, No.Punggung: {pemain[2]}")
                        
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
