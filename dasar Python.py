# Membuat nomer urut
"""
  Disini kita akan membuat no urut dari 1 sampai 100
"""
angka = 1
while angka <=100:
  print(angka)
  angka +=1

# Membuat fungsi sederhana
"""
  Membuat fungsi untuk menentukan rata-rata
"""
def hitung_mean(daftar_angka):
    if len(daftar_angka) == 0:
        return 0  # Menghindari pembagian oleh nol jika daftar kosong.
    
    total = sum(daftar_angka)
    mean = total / len(daftar_angka)
    return mean

# Contoh penggunaan fungsi
angka = [6, 10, 18, 29, 33]
rata_rata = hitung_mean(angka)
print(f"Mean dari {angka} adalah {rata_rata}")

# Membuat list
"""
  membuat list berisi angka dari 1 sampai 50
"""
deret_angka = list(range(1:50))


