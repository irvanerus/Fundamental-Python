"""
data skalar digunakan untuk data yang sangat sederhana
berikut contoh2 nya

"""

print("contoh data list skalar (sederhana")
anak1 = "eko"
anak2 = "dwi"
anak3 = "tri"
anak4 = "putri"

print("anak1")
print("anak2")
print("anak3")
print("anak4")

"""
data list/daftar/array
digunakan untuk data yg lebih kompleks namun penggunaannya lebih mudah
berikut contohnya

"""

print("\ncontoh data list")

anak = ["eko", "dwi", "tri", "putri"]
#untuk menambahkan data nama anak
anak.append("jaka")

print(anak)
#untuk menyapa anak tertentu yang terdaftar dilist bisa digunakan coding dibawah
#sebagai catatan komputer menghitung dari 0, apabila ingin sapa anak ke 2 berarti input 1

print(f"halo {anak[1]}!")

# untuk sapa semua anak bisa dengan 2 cara, ribet dan simple

print("\ncara sapa semua anak cara simpel")
for a in anak:
    print(f"halo {a}!")
print("\ncara sapa semua anak cara ribet")
for a in range (0, len(anak)):
    print(f"halo {anak[a]}!")

"""
len digunakan untuk menghitung secara keseluruhan data, karena kemungkinan ada banyak data
dan apabila kita tidak mungkin hitung satu persatu ada berapa data

cara bacanya
untuk anak dalam jangkauan 0 sampai jumlah data di variabel anak maka
tampilkan halo anak (sesuai jumlah data)

anak dalam hal ini eko dll 
"""