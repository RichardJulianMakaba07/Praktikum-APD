print("""Haloo, Selamat datang di kalkulator BMI
Silahkan isi berat badan anda dalam satuan (mg) dan tinggi badan anda dalam satuan (km)
Contoh:
Berat badan anda 55 kg = 55000000 mg
Tinggi badan anda 165 cm = 0.00165 km
""")

berat_mg = int(input("Masukkan berat badan anda (mg): "))
tinggi_km = float(input("Masukkan tinggi badan anda (km): "))

berat_kg = berat_mg / 1000000
tinggi_m = tinggi_km * 1000

bmi = berat_kg / (tinggi_m ** 2)  

if bmi < 18.5:
    print("Berat badan anda kurang (Underweight)")
elif bmi < 24.9:
    print("Berat badan anda normal (Normal)")
elif bmi < 29.9:
    print("Berat badan anda berlebih (Overweight)")
else:
    print("Obesitas")
    
print("BMI anda adalah", bmi)
