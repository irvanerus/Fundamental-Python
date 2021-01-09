"""
tipe data perulangan adalah apabila programmer diminta untuk menampilkan data yang variabel nya banyak
dan berulang, contoh seorang ayah yang memiliki banyak anak, karena variabel nya sama2 anak
hanya perlu untuk mengganti menjadi anak ke 1 ke 2 dst sesuai jumlah anak tsb
"""
print("\nberikut contoh tipe data perulangan")

#variabel
jumlah_anak = 100
print("halo anak#1")
print("halo anak#2")
print("halo anak#3")
print("halo anak#4")

#jika data variabel berjumlah 1000 tidak mungkin dibuat perintah print sebanyak seribu
#untuk menampilkan halo anak 1-1000
#berikut coding untuk menampilkan data perulangan agar bisa memunculkan data sesai variabel
print("\nberikut contoh codingnya")
for index_anak in range (0, jumlah_anak+1):
    print(f"halo anak{index_anak}!")
"""
berikut penjelasan
for : untuk
index : jumlah anak bisa 
        dibuat index untuk menunjukan range 
cara baca codingnya
untuk jumlah anak dalam jangakauan 0 sampai jumlah anak yang diinginkan maka
tampilkan halo anak+1

kenapa 0 - jumlah anak
karena data komputer menghitung dari 0 bukan 1
jadi apabila data ada 5 akan dihitung bukan mulai dari satu melainkan dari 0
sehingga apabila data variabel berjumlah 100 dan tidak ditambahkan+1 maka
variabel yang muncul akan 99 sehingga dibuat +1 untuk menyesuaikan dengan jumlah variabel
"""