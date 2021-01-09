#from geometri.luas_segitiga import hitung_luas_segitiga
#from geometri.luas_segitiga import hitung_luas_segitiga
from geometri.luas_segitiga import hitung_luas_segitiga, info as info_segitiga
from geometri.persegi_panjang import hitung_luas_persegi_panjang, info as info_persegi_panjang

print(f"hitung_luas_segitiga {hitung_luas_segitiga(10, 6)}")
print(f"hitung_luas_persegi_panjang {hitung_luas_persegi_panjang(10, 8)}")

print(info_segitiga())
print(info_persegi_panjang())