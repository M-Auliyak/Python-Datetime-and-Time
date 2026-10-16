import time
from datetime import datetime

print("Mulai   :", datetime.now().strftime("%H:%M:%S"))
time.sleep(2)  # jeda 2 detik
print("Selesai :", datetime.now().strftime("%H:%M:%S"))

# Hitung mundur
print("\nHitung mundur:")
for i in range(3, 0, -1):
    print(i, end=" ", flush=True)
    time.sleep(1)
print("Selesai!")

# Jeda kurang dari 1 detik (animasi teks)
print("\nMengetik: ", end="")
for huruf in "Halo Python!":
    print(huruf, end="", flush=True)
    time.sleep(0.15)
print()