from datetime import date, datetime, timedelta

tgl = date(2026, 10, 12)
jam = datetime(2026, 10, 12, 14, 30, 45)
selisih = timedelta(days=10, hours=5)
d1 = date(year = 2018, month = 7, day = 12)
d2 = date(year = 2017, month = 12, day = 23)
d3 = d1 - d2
y = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
now = datetime.now()
t = now.strftime("%H:%M:%S")
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")

print("Objek date     :", tgl)
print("Objek datetime :", jam)
print("Tahun/Bulan/Hari:", jam.year, jam.month, jam.day)
print("Jam/Menit/Detik :", jam.hour, jam.minute, jam.second)
print("Timestamp =", jam.timestamp())

# Operasi dengan timedelta
print("10 hari 5 jam setelahnya:", jam + selisih)
print("Selisih dua tanggal     :", date(2026, 12, 25) - tgl)
print("Hari ke-berapa dlm pekan:", tgl.weekday(), "(0 = Senin)")
print()
print("d3 =", d3)
print("Total seconds =", y.total_seconds())
print("Time:", t)
print("s1:", s1)
print("s2:", s2)