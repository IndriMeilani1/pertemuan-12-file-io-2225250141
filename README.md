# Pertemuan 12 - File I/O dan Error Handling
Nama: Indri Meilani
NIM: 2225250141
Kelas: 3A

## Tujuan
Tujuan dari program ini adalah untuk membaca data mahasiswa dari file, memvalidasi data yang dimasukkan, mengolah nilai mahasiswa dengan menghitung rata-ratanya, kemudian menuliskan hasil pengolahan ke dalam file baru. Program ini juga dibuat agar dapat menangani kesalahan yang mungkin terjadi saat proses membaca maupun mengolah data menggunakan Python.

## Format File Input
Format file input yang digunakan adalah NIM,nilai, yaitu setiap baris berisi NIM mahasiswa dan nilai yang dipisahkan dengan tanda koma. Contohnya, A001,85, A002,78, dan A003,92. Data tersebut kemudian dibaca oleh program untuk diperiksa dan diolah sebelum hasilnya disimpan ke file rekap.

## Cara Menjalankan
python3 tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError, terjadi ketika file input yang ingin dibaca tidak ditemukan. Program akan menampilkan pesan bahwa file tidak ditemukan sehingga program dapat mengetahui letak kesalahannya.
- ValueError, terjadi ketika data nilai tidak sesuai dengan tipe data yang diharapkan, misalnya nilai berisi huruf atau karakter yang tidak dapat diubah menjadi angka. Program akan menampilkan pesan kesalahan dan melewati data yang tidak valid.

## Test Case
Pengujian dilakukan dengan beberapa kondisi untuk memastikan program dapat membaca, memvalidasi, mengolah, dan menulis data dengan benar. Pada test case pertama, file input berisi data NIM dan nilai yang valid, sehingga hasil yang diharapkan adalah seluruh data berhasil dibaca dan rata-rata nilai berhasil dihitung. Hasil aktual menunjukkan data berhasil diproses dan ditulis ke file rekap dengan status PASS. Pada test case kedua, file input tidak ditemukan, sehingga hasil yang diharapkan adalah program menampilkan pesan FileNotFoundError. Hasil aktual menunjukkan pesan bahwa file tidak ditemukan dan program dapat menangani kesalahan tersebut dengan status PASS. Pada test case ketiga, terdapat data nilai yang berupa huruf atau bukan angka, sehingga hasil yang diharapkan adalah program menampilkan pesan kesalahan ValueError dan melewati data yang tidak valid. Hasil aktual menunjukkan data yang tidak valid tidak ikut diolah, dengan status PASS. Pada test case keempat, file berisi beberapa data mahasiswa dengan nilai yang valid, sehingga hasil yang diharapkan adalah seluruh nilai berhasil dihitung dan hasil rekap tersimpan di file output. Hasil aktual menunjukkan rekap berhasil dibuat sesuai data input dengan status PASS.

## Refleksi
Salah satu error yang ditemukan dalam program ini adalah ValueError, yaitu ketika data nilai yang dibaca dari file ternyata berisi huruf atau karakter yang tidak dapat diubah menjadi angka. Cara mengatasinya adalah dengan menggunakan try-except pada saat proses mengubah nilai menggunakan fungsi float(). Jika terjadi kesalahan, program akan menampilkan pesan bahwa nilai tidak valid dan melewati baris tersebut agar data yang salah tidak ikut diproses. Dari proses ini, saya belajar bahwa validasi data sangat penting supaya program dapat berjalan dengan lebih baik dan tidak langsung berhenti ketika menemukan kesalahan pada file input.
