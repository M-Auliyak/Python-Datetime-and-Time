# Tugas Sesi #7 – Python `datetime` & `time`

Kumpulan program contoh untuk setiap poin materi Sesi #7. Setiap file berdiri sendiri dan bisa dijalankan langsung.

## Prasyarat

- Python 3.6 atau lebih baru
- Tidak perlu menginstal library tambahan (hanya modul bawaan `datetime` dan `time`)

Cek versi Python:

```bash
python --version
```

## Cara Menjalankan

Buka terminal di folder ini, lalu jalankan salah satu file:

```bash
python 01_datetime_module.py
```

Di beberapa sistem (Linux/macOS), gunakan `python3` sebagai ganti `python`.

## Daftar Program

| No | File | Topik | Referensi |
|----|------|-------|-----------|
| 1 | `01_datetime_module.py` | Modul `datetime`: `date`, `datetime`, `timedelta` | [Programiz](https://www.programiz.com/python-programming/datetime) |
| 2 | `02_strftime.py` | `strftime()`: datetime menjadi string | [Programiz](https://www.programiz.com/python-programming/datetime/strftime) |
| 3 | `03_strptime.py` | `strptime()`: string menjadi datetime | [Programiz](https://www.programiz.com/python-programming/datetime/strptime) |
| 4 | `04_current_datetime.py` | Tanggal dan waktu saat ini | [Programiz](https://www.programiz.com/python-programming/datetime/current-datetime) |
| 5 | `05_current_time.py` | Waktu saat ini | [Programiz](https://www.programiz.com/python-programming/datetime/current-time) |
| 6 | `06_timestamp_to_datetime.py` | Timestamp ke datetime | [Programiz](https://www.programiz.com/python-programming/datetime/timestamp-datetime) |
| 7 | `07_time_module.py` | Modul `time` | [Programiz](https://www.programiz.com/python-programming/time) |
| 8 | `08_time_sleep.py` | `time.sleep()` | [Programiz](https://www.programiz.com/python-programming/time/sleep) |

## Ringkasan Singkat

- **`datetime`**: bekerja dengan tanggal dan jam (objek `date`, `time`, `datetime`, `timedelta`).
- **`strftime()`**: *string format time*, mengubah objek datetime menjadi teks dengan format tertentu.
- **`strptime()`**: *string parse time*, mengubah teks menjadi objek datetime.
- **Timestamp**: jumlah detik sejak 1 Januari 1970 (epoch), bisa dikonversi dari/ke datetime.
- **`time`**: modul untuk waktu tingkat rendah, misalnya `time()`, `ctime()`, `localtime()`.
- **`time.sleep(n)`**: menjeda program selama `n` detik.

## Kode Format Umum

| Kode | Arti | Contoh |
|------|------|--------|
| `%d` | Tanggal (2 digit) | 12 |
| `%m` | Bulan (angka) | 10 |
| `%B` | Nama bulan lengkap | October |
| `%b` | Nama bulan singkat | Oct |
| `%Y` | Tahun (4 digit) | 2026 |
| `%y` | Tahun (2 digit) | 26 |
| `%A` | Nama hari lengkap | Monday |
| `%H` | Jam (00–23) | 14 |
| `%I` | Jam (01–12) | 02 |
| `%M` | Menit | 30 |
| `%S` | Detik | 45 |
| `%p` | AM / PM | PM |
| `%f` | Mikrodetik | 000123 |

## Catatan

- `08_time_sleep.py` berhenti beberapa detik saat dijalankan, jadi tunggu sampai selesai.
- Hasil di `02`, `04`, `05`, dan `07` berbeda setiap kali dijalankan karena memakai waktu saat ini.
- Nama hari dan bulan di `strftime()` tampil dalam bahasa Inggris, mengikuti pengaturan *locale* bawaan Python.