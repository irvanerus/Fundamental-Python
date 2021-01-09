"""
contoh perintah fungsi dengan contoh segitiga sama sisi

"""
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2

print(f"luas segitiga dengan alas = {alas} dan tinggi {tinggi} adalah = {luas_segitiga}")

def hitung_luas_segitiga (alas, tinggi):
    luas_segitiga = alas * tinggi /2
    return luas_segitiga
print(hitung_luas_segitiga(10, 6))
