import time
from datetime import datetime

sekarang = datetime.now()
print("Waktu saat ini      :", sekarang.time())
print("Format HH:MM:SS     :", sekarang.strftime("%H:%M:%S"))
print("Dengan mikrodetik   :", sekarang.strftime("%H:%M:%S.%f"))

# Menggunakan modul time
print("time.localtime()    :", time.strftime("%H:%M:%S", time.localtime()))
print("time.gmtime() (UTC) :", time.strftime("%H:%M:%S", time.gmtime()))