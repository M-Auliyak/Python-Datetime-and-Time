from datetime import datetime

sekarang = datetime.now()
print("Format default      :", sekarang)
print("%d-%m-%Y            :", sekarang.strftime("%d-%m-%Y"))
print("%H:%M:%S            :", sekarang.strftime("%H:%M:%S"))
print("%A, %d %B %Y        :", sekarang.strftime("%A, %d %B %Y"))
print("%I:%M %p (12 jam)   :", sekarang.strftime("%I:%M %p"))
print("%y/%b/%d            :", sekarang.strftime("%y/%b/%d"))