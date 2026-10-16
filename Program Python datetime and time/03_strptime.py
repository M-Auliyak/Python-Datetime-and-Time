from datetime import datetime

teks1 = "12/10/2026"
dt1 = datetime.strptime(teks1, "%d/%m/%Y")
print(f"'{teks1}' -> {dt1} (tipe: {type(dt1).__name__})")

teks2 = "12 October, 2026 14:30:45"
dt2 = datetime.strptime(teks2, "%d %B, %Y %H:%M:%S")
print(f"'{teks2}' -> {dt2}")

# Penanganan format yang salah
try:
    datetime.strptime("2026-10-12", "%d/%m/%Y")
except ValueError as e:
    print("Format tidak cocok ->", e)