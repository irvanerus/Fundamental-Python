kamus_ind_eng = {}
kamus_ind_eng ["anak"] = ["son"]
kamus_ind_eng ["istri"] = ["wife"]
kamus_ind_eng ["ayah"] = ["father"]
kamus_ind_eng ["ibu"] = ["mother"]

print (kamus_ind_eng ["ayah"])
print (kamus_ind_eng ["ibu"])
print (kamus_ind_eng ["anak"])
print (kamus_ind_eng ["istri"])

print("data ini diambil dari server gojek untuk menampilkan info driver terdekat dengan lokasi pengguna")
data_dari_server_gojek = {
    "tanggal": [
                "2021-07-01",
                "2021-09-01",
                "2021-10-01",
                "2021-11-01"],
    "driver_list": [
                    {"nama": "eko", "jarak": 10},
                    {"nama": "dwi", "jarak": 50},
                    {"nama": "jajang", "jarak": 100},
                    {"nama": "tezar", "jarak": 1000}]
}
print("\n print dict semua driver gojek")
print(data_dari_server_gojek)

print("\n print dict hanya driver gojek disekitar")
print(f"driver disektiar anda {data_dari_server_gojek['driver_list']}")

print("\n print dict detail driver terdekat urutan pertama berdasarkan nama")
print(f"driver terdekat {data_dari_server_gojek['driver_list'][0]['nama']}")

print("\n print dict detail driver urutan pertama berdasarkan jarak")
print(f"driver terdekat {data_dari_server_gojek['driver_list'][0]['jarak']} meter")

print(f"driver terdekat {data_dari_server_gojek['driver_list'][0]['jarak']} meter")


























print(f"driver terdekat {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
