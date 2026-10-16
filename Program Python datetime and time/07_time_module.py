import time

print("time.time()         :", time.time())
print("time.ctime()        :", time.ctime())
print("time.localtime()    :", time.localtime())

lt = time.localtime()
print("Tahun/Bulan/Hari    :", lt.tm_year, lt.tm_mon, lt.tm_mday)
print("strftime            :", time.strftime("%d-%m-%Y %H:%M:%S", lt))

# strptime dari modul time
st = time.strptime("12 10 2026", "%d %m %Y")
print("time.strptime()     :", st)

# mktime: struct_time -> timestamp
print("time.mktime()       :", time.mktime(st))

# Mengukur lama eksekusi
awal = time.perf_counter()
jumlah = sum(i * i for i in range(1_000_000))
akhir = time.perf_counter()
print(f"Hitung 1 juta kuadrat selesai dalam {akhir - awal:.4f} detik")

# time.sleep()
print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")