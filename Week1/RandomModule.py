import random
# Tinh xac suat so lan sap/ngua

N = 10000

dem = 0
for i in range(N):
    sap = random.random()
    if sap <= 0.5:
        dem += 1
print("Xac suat xuat hien mat sap:", dem/N)
print("Xac suat xuat hien mat ngua:", 1-dem/N)

    