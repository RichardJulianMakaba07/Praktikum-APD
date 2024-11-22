import json #digunakan untuk mengolah data dalam format JSON
import os #digunakan untuk membersihkan layar terminal
from time import sleep #digunakan untuk jeda time sleep

# digunakan untuk membersihkan layar terminal
def hterminal():
    os.system("cls || clear")

# digunakan untuk memuat data dari file JSON
def memuat_data():
    try:
        with open("rental_motor_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"motor": [], "pengunjung": []}

# digunakan untuk menyimpan data yang telah dimodifikasi ke file JSON    
def menyimpan_data(data):
    with open("rental_motor_data.json", "w") as file:
        json.dump(data, file, indent=4)
    
data = memuat_data()

# Fungsi untuk menambah motor
def tambah_motor(data):
    hterminal()
    print("="*100)
    print("TAMBAH MOTOR".center(100))
    print("="*100)
    jenis_motor = input("===> Masukkan jenis motor : ")
    # Pengecekan apakah jenis motor sudah ada
    for motor in data["motor"]:
        if motor["jenis motor"].lower() == jenis_motor.lower():
            print("="*100)
            print("\nJenis motor sudah ada!")
            print("="*100)
            input("\nKlik enter untuk melanjutkan...")
            return
    try:
        jumlah_motor = int(input("===> Masukkan jumlah motor : "))
        harga_motor = int(input("===> Masukkan harga sewa per hari : "))
        print("="*100)
        # Validasi jumlah motor dan harga motor
        if jumlah_motor < 0:
            print("\nJumlah motor tidak boleh negatif.")
            print("="*100)
            input("\nKlik enter untuk melanjutkan...")
            return
        if harga_motor < 0:
            print("\nHarga motor tidak boleh negatif.")
            print("="*100)
            input("\nKlik enter untuk melanjutkan...")
            return
    except ValueError:
        print("\nHarus berupa angka! Silakan coba lagi.")
        print("="*100)
        input("\nKlik enter untuk melanjutkan...")
        return

    data["motor"].append({
        "jenis motor": jenis_motor.capitalize(),
        "jumlah motor": jumlah_motor,
        "harga sewa motor": harga_motor
    })
    menyimpan_data(data)
    print("\nMotor berhasil ditambahkan!")
    print("="*100)
    input("\nKlik enter untuk melanjutkan...")
    return

# Fungsi untuk menampilkan daftar motor
def tampilkan_motor(data):
    if not data["motor"]:
        print("="*100)
        print("Tidak ada data motor.")
        print("="*100)
    else:
        hterminal()
        print("="*100)
        print("DAFTAR MOTOR".center(100))
        print("="*100)
        for motor in data["motor"]:
            status = "Tersedia" if motor["jumlah motor"] > 0 else "Tidak Tersedia"
            print(f"| Jenis motor: {motor["jenis motor"]} | Jumlah motor: {motor["jumlah motor"]} | Harga Sewa/Hari: {motor["harga sewa motor"]} | Status: {status}")
            print("_"*100)
        input("\nKlik enter untuk melanjutkan...")

# Fungsi untuk memperbarui data motor
def update_motor(data):
    hterminal()
    tampilkan_motor(data)
    print("="*100)
    print("UPDATE MOTOR".center(100))
    print("="*100)
    jenis_motor = input("===> Masukkan jenis motor yang ingin diupdate : ")

    for motor in data["motor"]:
        if motor["jenis motor"].lower() == jenis_motor.lower():
            try:
                jumlah_motor_baru = int(input("===> Masukkan jumlah motor baru : "))
                if jumlah_motor_baru < 0:
                    print("\nJumlah motor tidak boleh negatif.")
                    print("="*100)
                    input("\nKlik enter untuk melanjutkan...")
                    return
                harga_motor_baru = int(input("===> Masukkan harga sewa baru per hari : "))
                if harga_motor_baru < 0:
                    print("\nHarga motor tidak boleh negatif.")
                    print("="*100)
                    input("\nKlik enter untuk melanjutkan...")
                    return
                
                motor["jumlah motor"] = jumlah_motor_baru
                motor["harga sewa motor"] = harga_motor_baru
                menyimpan_data(data)
                print("\nMotor berhasil diupdate!")
                print("="*100)
                input("\nKlik enter untuk melanjutkan...")
                return
            except ValueError:
                print("\nMasukkan jumlah motor dan harga sewa motor dengan benar (angka).")
                print("="*100)
                input("\nKlik enter untuk melanjutkan...")
                return
    else:
        print("\nMotor tidak ditemukan.")
        print("="*100)
        input("\nKlik enter untuk melanjutkan...")
        return

# Fungsi untuk menghapus data motor
def hapus_motor(data):
    hterminal()
    tampilkan_motor(data)
    print("="*100)
    print("HAPUS MOTOR".center(100))
    print("="*100)
    jenis_motor = input("===> Masukkan jenis motor yang ingin dihapus: ")

    for motor in data["motor"]:
        if motor["jenis motor"].lower() == jenis_motor.lower():
            data["motor"].remove(motor)
            menyimpan_data(data)
            print(f"\nMotor {motor["jenis motor"]} berhasil dihapus!")
            print("="*100)
            input("\nKlik enter untuk melanjutkan...")
            return
    else:
        print("\nMotor tidak ditemukan.")
        print("="*100)
        input("\nKlik enter untuk melanjutkan...")
        return

# Fungsi untuk melihat daftar pengunjung, memisahkan member dan user
def lihat_pengunjung(data):
    hterminal()
    member_list = [p for p in data["pengunjung"] if p.get("role") == "member"]
    user_list = [p for p in data["pengunjung"] if p.get("role") == "user"]
    print("="*115)
    print("DAFTAR MEMBER".center(115))
    print("="*115)
    if member_list:
        for member in member_list:
            print(f"| Nama: {member["nama"]} | Jenis motor: {member["motor_sewa"]} | Jumlah motor: {member["jumlah_motor_sewa"]} | Total Harga: {member["total_harga_sewa"]} | Status: {member["status_sewa"]}")
    else:
        print("Tidak ada data member.")

    print("="*115)
    print("DAFTAR USER".center(115))
    print("="*115)
    if user_list:
        for user in user_list:
            print(f"| Nama: {user["nama"]} | Jenis motor: {user["motor_sewa"]} | Jumlah motor: {user["jumlah_motor_sewa"]} | Total Harga: {user["total_harga_sewa"]} | Status: {user["status_sewa"]}")
    else:
        print("Tidak ada data user.")
    print("="*115)
    input("\nKlik enter untuk melanjutkan...")
    return
        
# Fungsi untuk mengecek motor tersedia atau tidak       
def cek_motor_tersedia(nama_motor, jumlah, data):
    for motor in data["motor"]:
        if motor["jenis motor"].lower() == nama_motor.lower():
            if motor["jumlah motor"] >= jumlah:
                return motor
    return None

# Fungsi untuk menghitung diskon
def hitung_diskon(durasi_sewa, total_harga):
    if durasi_sewa >= 5:
        diskon = 0.10 * total_harga
        total_harga -= diskon
        print(f"Selamat diskon 10% diterapkan.")
    return total_harga

# Fungsi untuk menyewa motor member
def sewa_motor_member(username, password, data):
    hterminal()
    tampilkan_motor(data)
    print("="*100)
    print("SEWA MOTOR MEMBER".center(100))
    print("="*100)
    motor_yang_ingin_disewa = input("===> Masukkan nama motor yang ingin disewa : ")
    try:
        jumlah_motor = int(input("===> Masukkan jumlah motor yang ingin disewa : "))
        if jumlah_motor <= 0:
            print("\nJumlah motor harus lebih dari 0")
            print("="*100)
            input("\nKlik enter untuk melanjutkan...")
            return
    except ValueError:
        print("\nInput tidak valid. Harap masukkan angka.")
        print("="*100)
        input("\nKlik enter untuk melanjutkan...")
        return
    
    motor_tersedia = cek_motor_tersedia(motor_yang_ingin_disewa, jumlah_motor, data)
    
    if motor_tersedia:
        try:
            durasi_sewa = int(input("===> Masukkan durasi sewa (hari): "))
            if durasi_sewa <= 0:
                print("\nDurasi sewa harus lebih dari 0")
                print("="*100)
                input("\nKlik enter untuk melanjutkan...")
                return
        except ValueError:
            print("\nInput tidak valid. Harap masukkan angka.")
            print("="*100)
            input("\nKlik enter untuk melanjutkan...")
            return
        
        total_harga = motor_tersedia["harga sewa motor"] * jumlah_motor * durasi_sewa
        total_harga = hitung_diskon(durasi_sewa, total_harga)
        motor_tersedia["jumlah motor"] -= jumlah_motor
        
        data["pengunjung"].append({
        "nama": username.capitalize(),
        "password": password,
        "role": "member",
        "motor_sewa": motor_yang_ingin_disewa.capitalize(),
        "harga_motor_sewa": motor_tersedia["harga sewa motor"],
        "jumlah_motor_sewa": jumlah_motor,
        "durasi_sewa": durasi_sewa,
        "total_harga_sewa": total_harga,
        "status_sewa": "disewa"
        })
        
        menyimpan_data(data)  
        
        print(f"\nMotor {motor_yang_ingin_disewa} berhasil disewa. Total harga sewa: {total_harga}")
        print("="*100)
        input("\nKlik enter untuk melanjutkan...")
        return
    else:
        print("\nMotor tidak tersedia.")
        print("="*100)
        input("\nKlik enter untuk melanjutkan...")
        return

# Fungsi untuk menyewa motor user
def sewa_motor_user(username, password, data):
    hterminal()
    tampilkan_motor(data)
    print("="*100)
    print("SEWA MOTOR USER".center(100))
    print("="*100)
    motor_yang_ingin_disewa = input("===> Masukkan nama motor yang ingin disewa : ")
    try:
        jumlah_motor = int(input("===> Masukkan jumlah motor yang ingin disewa: "))
        if jumlah_motor <= 0:
            print("\nJumlah motor harus lebih dari 0")
            print("="*100)
            input("\nKlik enter untuk melanjutkan...")
            return
    except ValueError:
        print("\nInput tidak valid. Harap masukkan angka.")
        print("="*100)
        input("\nKlik enter untuk melanjutkan...")
        return
    
    motor_tersedia = cek_motor_tersedia(motor_yang_ingin_disewa, jumlah_motor, data)
    
    if motor_tersedia:
        try:
            durasi_sewa = int(input("===> Masukkan durasi sewa (hari): "))
            if durasi_sewa <= 0:
                print("\nDurasi sewa harus lebih dari 0")
                print("="*100)
                input("\nKlik enter untuk melanjutkan...")
                return
        except ValueError:
            print("\nInput tidak valid. Harap masukkan angka.")
            print("="*100)
            input("\nKlik enter untuk melanjutkan...")
            return
        
        total_harga = motor_tersedia["harga sewa motor"] * jumlah_motor * durasi_sewa
        motor_tersedia["jumlah motor"] -= jumlah_motor
        
        data["pengunjung"].append({
        "nama": username.capitalize(),
        "password": password,
        "role": "user",
        "motor_sewa": motor_yang_ingin_disewa.capitalize(),
        "harga_motor_sewa": motor_tersedia["harga sewa motor"],
        "jumlah_motor_sewa": jumlah_motor,
        "durasi_sewa": durasi_sewa,
        "total_harga_sewa": total_harga,
        "status_sewa": "disewa"
        })
        
        menyimpan_data(data)  
        
        print(f"\nMotor {motor_yang_ingin_disewa} berhasil disewa. Total harga sewa: {total_harga}")
        print("="*100)
        input("\nKlik enter untuk melanjutkan...")
        return
    else:
        print("\nMotor tidak tersedia.")
        print("="*100)
        input("\nKlik enter untuk melanjutkan...")
        return
  
# Fungsi untuk mengembalikan motor
def kembalikan_motor(username, data):
    hterminal()
    print("="*100)
    print("KEMBALIKAN MOTOR".center(100))
    print("="*100)
    for pengunjung in data["pengunjung"]:
        if pengunjung["nama"].lower() == username.lower() and pengunjung["status_sewa"] == "disewa":
            print(f"| Motor yang disewa: {pengunjung["motor_sewa"]} | Jumlah motor: {pengunjung["jumlah_motor_sewa"]} | Durasi sewa: {pengunjung["durasi_sewa"]} hari | Harga sewa: {pengunjung["total_harga_sewa"]}")
            print("_"*100)
            input("\nKlik enter untuk melanjutkan...")
            motor_yang_ingin_dikembalikan = input("\n===> Masukkan nama motor yang ingin dikembalikan : ")
            
            if motor_yang_ingin_dikembalikan.lower() == pengunjung["motor_sewa"].lower():
                try:
                    jumlah_motor = int(input("===> Masukkan jumlah motor yang ingin dikembalikan: "))
                    if jumlah_motor < pengunjung["jumlah_motor_sewa"] or jumlah_motor > pengunjung["jumlah_motor_sewa"]:
                        print("\nJumlah motor tidak valid. Harap masukkan jumlah yang benar.")
                        print("_"*100)
                        input("\nKlik enter untuk melanjutkan...")
                        return
                    durasi_sewa = int(input("===> Masukkan durasi sewa (hari) : "))
                    if durasi_sewa < pengunjung["durasi_sewa"] or durasi_sewa > pengunjung["durasi_sewa"]:
                        print("\nDurasi sewa tidak valid. Harap masukkan durasi yang benar.")
                        print("_"*100)
                        input("\nKlik enter untuk melanjutkan...")
                        return
                    harga_sewa = int(input("===> Masukkan harga sewa : "))
                    if harga_sewa < pengunjung["total_harga_sewa"] or harga_sewa > pengunjung["total_harga_sewa"]:
                        print("\nHarga sewa tidak valid. Harap masukkan harga yang benar.")
                        print("_"*100)
                        input("\nKlik enter untuk melanjutkan...")
                        return
                except ValueError:
                    print("\nInput tidak valid. Harap masukkan angka.")
                    print("_"*100)
                    input("\nKlik enter untuk melanjutkan...")
                    return
                    
                for motor in data["motor"]:
                    if motor["jenis motor"].lower() == motor_yang_ingin_dikembalikan.lower():
                        motor["jumlah motor"] += jumlah_motor
                
                pengunjung["status_sewa"] = "dikembalikan"
                menyimpan_data(data)  
                print(f"\nMotor {motor_yang_ingin_dikembalikan} berhasil dikembalikan. Total harga sewa: {pengunjung["total_harga_sewa"]}")
                print("_"*100)
                input("\nKlik enter untuk melanjutkan...")
                return
                
            else:
                print("\nMotor yang dikembalikan tidak sesuai.")
                print("_"*100)
                input("\nKlik enter untuk melanjutkan...")
                return
    else:
        print("Tidak ada motor yang saat ini anda sewa.")
        print("_"*100)
        input("\nKlik enter untuk melanjutkan...")
        return
    
# Fungsi untuk melihat riwayat sewa
def lihat_riwayat_sewa(username, data):
    hterminal()
    print("="*115)
    print("RIWAYAT SEWA".center(115))
    print("="*115)
    ada_riwayat = False
    for pengunjung in data["pengunjung"]:
        if pengunjung["nama"].lower() == username.lower():
            if pengunjung.get("motor_sewa"):
                ada_riwayat = True
                print(f"| Motor disewa: {pengunjung["motor_sewa"]} | Total harga sewa: {pengunjung["total_harga_sewa"]} | Jumlah motor: {pengunjung["jumlah_motor_sewa"]} | Durasi sewa: {pengunjung["durasi_sewa"]} | Status Sewa: {pengunjung["status_sewa"]}")
                print("_"*115)  # Memisahkan setiap riwayat
    if not ada_riwayat:
        print("\nTidak ada riwayat sewa.")
        print("_"*115)         
    input("\nKlik enter untuk melanjutkan...")
    return
    


#====================================================== PROGRAM UTAMA ==========================================================================
hterminal()
print("="*100)
print("SELAMAT DATANG DI RENTAL MOTOR".center(100))
print("="*100)
input("\nKlik enter untuk melanjutkan...")
while True:
    hterminal()
    print("="*100)
    print("MENU UTAMA".center(100))
    print("="*100)
    print(" [1]  ADMIN ")
    print(" [2]  USER  ")
    print(" [3]  EXIT  ")
    print("="*100)
    pilihan = input("SILAHKAN PILIH MENU : ")
    if pilihan == "1":
        hterminal()
        print("="*100)
        print("ADMIN".center(100))
        print("="*100)
        username = input("===> Masukkan Username : ")
        password = input("===> Masukkan Password : ")
        if username == "admin" and password == "admin":
            print("\nANDA BERHASIL LOGIN")
            print("="*100)
            sleep(1)
            while True:
                hterminal()
                print("="*100)
                print("MENU ADMIN".center(100))
                print("="*100)
                print("[1] Tambah motor")
                print("[2] Tampilkan daftar motor")
                print("[3] Update motor")
                print("[4] Hapus motor")
                print("[5] Melihat daftar pengunjung")
                print("[6] Logout")
                print("="*100)
                pilihan = input("Silahkan pilih menu (1-6): ")

                if pilihan == "1":
                    tambah_motor(data)
                elif pilihan == "2":
                    tampilkan_motor(data)
                elif pilihan == "3":
                    update_motor(data)
                elif pilihan == "4":
                    hapus_motor(data)
                elif pilihan == "5":
                    lihat_pengunjung(data)
                elif pilihan == "6":
                    print(f"\nBerhasil logout...")
                    sleep(1)
                    break
                else:
                    print("\nPilihan tidak valid. Silakan pilih antara 1-6.")
                    print("="*100)
                    input("\nKlik enter untuk melanjutkan...")
        else:
            print("\nLogin gagal, ada yang salah🤔")
            print("="*100)
            input("\nKlik enter untuk melanjutkan...")
            
        
    elif pilihan == "2":
        while True:
            hterminal()
            print("="*100)
            print("MENU USER".center(100))
            print("="*100)
            print(" [1]  REGISTRASI ")
            print(" [2]  LOGIN      ")
            print(" [3]  MENU UTAMA ")
            print("="*100)
            pilihan_user = input("SILAHKAN PILIH MENU (1-3) : ")
            if pilihan_user == "1":
                hterminal()
                print("="*100)
                print("REGISTRASI".center(100))
                print("="*100)
                username = input("===> Masukkan Username : ").strip()
                password = input("===> Masukkan Password : ").strip()
                if username == "" or password == "":
                    print("\nUsername atau password tidak boleh kosong!😤")
                    print("="*100)
                    input("\nKlik enter untuk melanjutkan...")
                    continue
                for pengunjung in data["pengunjung"]:
                    if pengunjung["nama"].lower() == username.lower():
                        print("\nUsername sudah digunakan")
                        print("="*100)
                        input("\nKlik enter untuk melanjutkan...")
                        break 
                else:
                    print("="*100)
                    print("Jika bergabung sebagai member akan mendapatkan diskon 10% pada saat menyewa motor minimal 5 hari")
                    role = input("\n===> Apakah ingin bergabung sebagai member?(y/n): ")
                    print("="*100)
                    if role.lower() == "y":
                        data["pengunjung"].append({
                        "nama": username.capitalize(),
                        "password": password,
                        "role": "member",
                        "motor_sewa": None,
                        "harga_motor_sewa": None,
                        "jumlah_motor_sewa": None,
                        "durasi_sewa": None,
                        "total_harga_sewa": None,
                        "status_sewa": None
                        })
                        menyimpan_data(data)
                        print("\nSelamat anda berhasil bergabung sebagai member")
                        print("="*100)
                        input("\nKlik enter untuk melanjutkan...")
                        
                    elif role.lower() == "n":
                        data["pengunjung"].append({
                        "nama": username.capitalize(),
                        "password": password,
                        "role": "user",
                        "motor_sewa": None,
                        "harga_motor_sewa": None,
                        "jumlah_motor_sewa": None,
                        "durasi_sewa": None,
                        "total_harga_sewa": None,
                        "status_sewa": None
                        })
                        menyimpan_data(data)
                        print("\nSelamat anda berhasil bergabung sebagai user")
                        print("="*100)
                        input("\nKlik enter untuk melanjutkan...")
                    else:
                        print("\nPilihan tidak valid")
                        print("="*100)
                        input("\nKlik enter untuk melanjutkan...")
                    
            
            elif pilihan_user == "2":
                hterminal()
                print("="*100)
                print("LOGIN".center(100))
                print("="*100)
                username = input("===> Masukkan Username: ")
                password = input("===> Masukkan Password: ")
                for pengunjung in data["pengunjung"]:
                    if pengunjung["nama"].lower() == username.lower() and pengunjung["password"] == password :
                        if pengunjung["role"] == "member":
                            print(f"\nSelamat datang {pengunjung["nama"]}, anda berhasil login sebagai {pengunjung["role"]}")
                            print("="*100)
                            sleep(1.3)
                            while True:
                                hterminal()
                                print("="*100)
                                print("MENU MEMBER".center(100))
                                print("="*100)
                                print("[1] Tampilkan daftar motor")
                                print("[2] Menyewa motor")
                                print("[3] Kembalikan motor")
                                print("[4] Lihat riwayat sewa")
                                print("[5] Logout")
                                print("="*100)
                                pilihan = input("Silahkan pilih menu (1-5): ")

                                if pilihan == "1":
                                    tampilkan_motor(data)
                                elif pilihan == "2":
                                    sewa_motor_member(username, password, data)
                                elif pilihan == "3":
                                    kembalikan_motor(username, data)
                                elif pilihan == "4":
                                    lihat_riwayat_sewa(username, data)
                                elif pilihan == "5":
                                    print(f"\nBerhasil logout...")
                                    sleep(1)
                                    break
                                else:
                                    print("\nPilihan tidak valid. Silakan coba lagi.")
                                    print("="*100)
                                    input("\nKlik enter untuk melanjutkan...")
                            break        
                        else:
                            print(f"\nSelamat datang {pengunjung["nama"]}, anda berhasil login sebagai {pengunjung["role"]}")
                            print("="*100)
                            sleep(1.3)
                            while True:
                                hterminal()
                                print("="*100)
                                print("MENU USER".center(100))
                                print("="*100)
                                print("[1] Tampilkan daftar motor")
                                print("[2] Menyewa motor")
                                print("[3] Kembalikan motor")
                                print("[4] Lihat riwayat sewa")
                                print("[5] Logout")
                                print("="*100)

                                pilih = input("Silahkan pilih menu (1-5): ")

                                if pilih == "1":
                                    tampilkan_motor(data)
                                elif pilih == "2":
                                    sewa_motor_user(username, password, data)
                                elif pilih == "3":
                                    kembalikan_motor(username, data)
                                elif pilih == "4":
                                    lihat_riwayat_sewa(username, data)
                                elif pilih == "5":
                                    print("\nBerhasil logout...")
                                    sleep(1)
                                    break
                                else:
                                    print("\nPilihan tidak valid. Silakan pilih menu yang benar.")
                                    print("="*100)
                                    input("\nKlik enter untuk melanjutkan...")
                            break
                else:
                    print("\nLogin gagal, ada yang salah🤔")
                    print("="*100)
                    input("\nKlik enter untuk melanjutkan...")
                    
            elif pilihan_user == "3":
                break
            else:
                print("\nPilihan tidak valid")
                print("="*100)
                input("\nKlik enter untuk melanjutkan...")
                
    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan sistem rental motor kami🤗🤩✌️\n")
        break     
    else:
        print("\nPILIHAN TIDAK VALID, SILAHKAN PILIH YANG BETUL😤")
        print("="*100)
        input("\nKlik enter untuk melanjutkan...")

