# LAPORAN PRAKTIKUM 2 - KONDISIONAL DAN PERULANGAN 

Nama      : Chaya Aulia
Nim       : 312510197
Kelas     : TI.25.A2
Matkul    : Pengantar Pemrograman
Dosen     :Agung Nugroho, M.Kom

# Tujuan
Untuk memahami dan mempraktikkan penggunaan struktur kondisi (if, elif, else) dan struktur perulangan (for, while) dalam bahasa pemrograman Python.

# Folder
Praktikum 2 (labpy2)

├── README.md

├── Lab2_Strukur_Kondisi

 ├── latihan1.py

 └── latihan2.py
├── Lab_Perulangan

├── latihan1.py

└── latihan2.py

#  LAB 2 – STRUKTUR KONDISI
## 🔹 Latihan 1 – Menentukan Bilangan Terbesar
Deskripsi:
Membuat program untuk menentukan bilangan terbesar dari empat bilangan input.

Kode Program :

print("Menentukan bilangan terbesar dari 4 bilangan")

a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))
c = float(input("Masukkan bilangan ketiga: "))
d = float(input("Masukkan bilangan keempat: "))

terbesar = a

if b > terbesar:
    terbesar = b
if c > terbesar:
    terbesar = c
if d > terbesar:
    terbesar = d

print("Bilangan terbesar adalah:", terbesar)
### Penjelasan
Program menggunakan struktur if berurutan untuk membandingkan nilai setiap bilangan dan menyimpan nilai terbesar.

## 🔹 Latihan 2 – Mengurutkan Bilangan
Deskripsi:
Membuat program untuk mengurutkan tiga bilangan dari terkecil ke terbesar.

Kode Program:
print("Program mengurutkan data dari terkecil ke terbesar")

n = int(input("Masukkan jumlah data (min 3): "))

data = []
for i in range(n):
    nilai = float(input(f"Masukkan data ke-{i+1}: "))
    data.append(nilai)

### Proses pengurutan manual (bubble sort)
for i in range(len(data)):
    for j in range(0, len(data)-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print("Data setelah diurutkan:", data)
### Penjelasan:
Program membaca sejumlah data, lalu mengurutkannya dengan algoritma bubble sort agar konsep perulangan dan kondisi digunakan secara eksplisit.

 # Lab 3 - Perulangan
# Latihan 1

Soal:
Buat program dengan perulangan bertingkat (nested for) yang menghasilkan pola bintang.

Kode Jawaban (contoh pola segitiga bintang):
## Latihan 1: Nested for pattern
print("Program pola segitiga bintang")
n = int(input("Masukkan tinggi segitiga: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

# Latihan 2

Soal:
Tampilkan n bilangan acak yang lebih kecil dari 0.5. Nilai n diisi saat runtime.
Bisa menggunakan kombinasi while dan for.
Kode Jawaban :
# Latihan 2: Bilangan acak < 0.5
import random

n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan: "))

count = 0
while count < n:
    r = random.random()  # menghasilkan angka antara 0.0–1.0
    if r < 0.5:
        print(r)
        count += 1
# Penjelasan:
Program menggunakan while agar terus menghasilkan bilangan acak sampai jumlah yang ditentukan terpenuhi. Hanya bilangan < 0.5 yang dicetak.

