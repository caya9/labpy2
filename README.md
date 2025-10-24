# LAPORAN PRAKTIKUM 2 - KONDISIONAL DAN PERULANGAN 

Nama      : Chaya Aulia

Nim       : 312510197

Kelas     : TI.25.A2

Matkul    : Pengantar Pemrograman

Dosen     :Agung Nugroho, M.Kom

# 🧩 Lab 2: Struktur Kondisi
## Latihan 1
### Deskripsi
Buat program sederhana dengan input 4 buah bilangan, kemudian tentukan bilangan terbesar dari keempat bilangan tersebut menggunakan statement if.

#### Kode Jawaban :
```python
print("Program mengurutkan data dari terkecil ke terbesar")

n = int(input("Masukkan jumlah data (min 3): "))

data = []
for i in range(n):
    nilai = float(input(f"Masukkan data ke-{i+1}: "))
    data.append(nilai)

# Proses pengurutan manual (bubble sort)
for i in range(len(data)):
    for j in range(0, len(data)-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
```
## penjelasan 
Program menggunakan struktur if berurutan untuk membandingkan nilai setiap bilangan dan menyimpan nilai terbesar.

print("Data setelah diurutkan:", data)

## 🔹 Latihan 2

### Deskripsi
Buat program untuk mengurutkan sejumlah data (minimal 3 variabel input atau lebih), kemudian tampilkan hasilnya dari terkecil ke terbesar.

#### Kode Jawaban :
```python
# Latihan 2: Mengurutkan data
print("Program mengurutkan data dari terkecil ke terbesar")

n = int(input("Masukkan jumlah data (min 3): "))

data = []
for i in range(n):
    nilai = float(input(f"Masukkan data ke-{i+1}: "))
    data.append(nilai)

# Proses pengurutan manual (bubble sort)
for i in range(len(data)):
    for j in range(0, len(data)-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print("Data setelah diurutkan:", data)
```
## Penjelasan
Program membaca sejumlah data, lalu mengurutkannya dengan algoritma bubble sort agar konsep perulangan dan kondisi digunakan secara eksplisit.

# 🔁 Lab 3: Perulangan
## Latihan 1
### Deskripsi
Buat program dengan perulangan bertingkat (nested for) yang menghasilkan pola bintang.

#### Kode Jawaban :
```python
# Latihan 1: Nested for pattern
print("Program pola segitiga bintang")
n = int(input("Masukkan tinggi segitiga: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
```
## Latihan 2
###  Deskripsi
Tampilkan n bilangan acak yang lebih kecil dari 0.5. Nilai n diisi saat runtime.
Bisa menggunakan kombinasi while dan for.

#### Kode Jawaban:
```python
# Latihan 2: Bilangan acak < 0.5
import random

n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan: "))

count = 0
while count < n:
    r = random.random()  # menghasilkan angka antara 0.0–1.0
    if r < 0.5:
        print(r)
        count += 1
```
## Penjelasan:
Program menggunakan while agar terus menghasilkan bilangan acak sampai jumlah yang ditentukan terpenuhi. Hanya bilangan < 0.5 yang dicetak.
