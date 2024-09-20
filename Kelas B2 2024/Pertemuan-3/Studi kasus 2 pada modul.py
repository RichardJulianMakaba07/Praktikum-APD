nama = input('Masukkan nama anda: ')
input_user = input('Jenis kelamin (L/P): ')
input_user = input_user.upper()
result = 'Laki-laki' if input_user == 'L' else 'Perempuan' if input_user == 'P' else 'Tidak valid'
print('jenis kelamin', nama, result)
