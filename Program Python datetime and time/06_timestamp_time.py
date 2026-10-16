from datetime import datetime, timezone

ts = 1760254245  # detik sejak 1 Januari 1970 (epoch)
print("Timestamp           :", ts)
print("fromtimestamp()     :", datetime.fromtimestamp(ts))
print("Versi UTC           :", datetime.fromtimestamp(ts, tz=timezone.utc))

# Kebalikannya: datetime -> timestamp
dt = datetime(2026, 10, 12, 14, 30, 45)
print("datetime -> timestamp:", dt.timestamp())

# Timestamp saat ini
print("Timestamp sekarang  :", datetime.now().timestamp())