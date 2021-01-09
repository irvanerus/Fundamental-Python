print("materi tipe sintaksis sequential/ berurutan")
print("Hello World!")

print ("\n materi tipe sintaksis percabangan")
jalan_sukses = False
jalan_hancur = True
if jalan_sukses:
    print("work hard, pray hard")
else:
    print("rebahan aja")
if jalan_hancur:
    print("Rebahan Aja")
else:
    print("work hard, pray hard")

print ("\n materi tipe data perulangan")

jumlah_anak = 4

for index_anak in range (1, jumlah_anak+1):
    print (f"1. halo anak {index_anak}")

print ("\n materi tipe sintaksis data list")
jumlah_anak = 10

anak1 = "eko"
anak2 = "dwi"
anak3 = "jajang"
anak4 = "tezar"

print(anak1)
print(anak2)
print(anak3)
print(anak4)

anak = ["eko", "dwi", "jajang", "tezar"]
print(anak)
anak.append("rita")
print(anak)
print ("\ntes sapa semua anak cara simpel")
for a in anak:
    print(f"Halo {a}")
print ("\ntes sapa semua anak cara ribet ")
for a in range (0, len(anak)):
    print(f"{a+1}. halo {anak[a]}!")
"""
naflajksadfsbdhas
"""