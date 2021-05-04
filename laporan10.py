#Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topik : Tuple

'''Perpustakan Kota Yogyakarta memerlukan data harian buku yang dipinjam dan buku yang kembali, buatlah programnya'''

#input : judul buku-buku yang dipinjam dan kembali
#proses : menggunakan perulangan for untuk menampilkan judul di tiap index
#output : buku (judul) dipinjam hari ini, buku (judul) kembali hari ini

bukuDipinjam = ("Dilan 1991", "Panduan Sukses CPNS", "Resep Masakan Nusantara", "Pemrograman Web")
bukuKembali = ("Algoritma Pemrograman", "Sweet Escape", "Kumpulan Cerita Rakyat", "Sains Anatomi")

for pinjam in bukuDipinjam:
    print("Buku", pinjam, "dipinjam hari ini")
print()
for kembali in bukuKembali:
    print("Buku", kembali, "kembali hari ini")