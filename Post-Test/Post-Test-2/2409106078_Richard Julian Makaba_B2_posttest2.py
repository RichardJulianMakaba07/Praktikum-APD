nama_barang = input('Masukkan nama barang: ')
harga_barang = float(input('Masukkan harga barang: '))
jumlah_barang = int(input('Masukkan jumlah barang: '))
diskon = float(input('Masukkan diskon dalam persen: '))
    
total_harga_sebelum_diskon = harga_barang * jumlah_barang
total_diskon = diskon / 100 * total_harga_sebelum_diskon
total_harga_akhir = total_harga_sebelum_diskon - total_diskon
sisa_bagi = diskon % 3

print(f'Anda membeli {jumlah_barang} {nama_barang} dengan harga satuan {harga_barang}, total sebelum diskon adalah {total_harga_sebelum_diskon}, total diskon adalah {total_diskon}, dan total yang harus dibayar adalah {total_harga_akhir}.')
print(f'{diskon} dibagi dengan 3 sisanya {sisa_bagi}')
