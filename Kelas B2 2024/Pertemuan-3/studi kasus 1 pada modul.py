jumlah_buku = int(input('Masukkan jumlah buku yang dibeli: '))
total_harga_pembelian = int(input('Masukkan total harga pembelian: '))

if jumlah_buku >= 5 and total_harga_pembelian > 100000:
    harga_akhir = total_harga_pembelian * 20 / 100
    print(f'Selamat Anda mendapat diskon sebesar 20%, sehingga total harga yang harus anda bayar adalah {harga_akhir}.')
else:
    print('Anda tidak mendapat diskon')
