print("Program mengurutkan data dari terkecil ke terbesar")

n = int(input("Masukkan jumlah data (min 3): "))

data = []
for i in range(n):
    nilai = float(input(f"Masukkan data ke-{i+1}: "))
    data.append(nilai)

for i in range(len(data)):
    for j in range(0, len(data)-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print("Data setelah diurutkan:", data)
