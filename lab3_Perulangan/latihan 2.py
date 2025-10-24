import random

n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan: "))

count = 0
while count < n:
    r = random.random()
    if r < 0.5:
        print(r)
        count += 1
