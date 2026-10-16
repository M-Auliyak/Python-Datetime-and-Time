from datetime import datetime, date, timedelta, timezone

print("datetime.now()      :", datetime.now())
print("datetime.today()    :", datetime.today())
print("date.today()        :", date.today())
print("UTC sekarang        :", datetime.now(timezone.utc))

# Zona waktu WIB (UTC+7)
wib = timezone(timedelta(hours=7))
print("Waktu WIB (UTC+7)   :", datetime.now(wib))
print()

# dalam berbagai format
print("\n" + "=" * 35)
print("Dalam berbagai format")
print("=" * 35)
today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)