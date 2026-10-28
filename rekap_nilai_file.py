
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Lewati baris kosong
                if not baris:
                    continue

                bagian = baris.split(",")

                # Validasi jumlah data
                if len(bagian) != 3:
                    print(f"Baris {nomor_baris} tidak valid, dilewati.")
                    continue

                nama = bagian[0].strip()

                # Validasi nilai harus berupa angka
                try:
                    nilai = float(bagian[1].strip())
                    tugas = float(bagian[2].strip())
                except ValueError:
                    print(f"Nilai pada baris {nomor_baris} tidak valid, dilewati.")
                    continue

                # Validasi rentang nilai
                if not (0 <= nilai <= 100 and 0 <= tugas <= 100):
                    print(f"Nilai di luar rentang pada baris {nomor_baris}, dilewati.")
                    continue

                data.append({
                    "nama": nama,
                    "nilai": nilai,
                    "tugas": tugas
                })

    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
    except OSError as error:
        print(f"Terjadi kesalahan saat membaca file: {error}")

    return data


def tulis_rekap(nama_file, data):
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write("REKAP NILAI MAHASISWA\n")
            file.write("=====================\n")

            if not data:
                file.write("Tidak ada data valid untuk direkap.\n")
                return

            total = 0

            for nomor, mahasiswa in enumerate(data, start=1):
                rata_rata = (mahasiswa["nilai"] + mahasiswa["tugas"]) / 2
                total += rata_rata

                file.write(
                    f"{nomor}. Nama: {mahasiswa['nama']}, "
                    f"Nilai: {mahasiswa['nilai']}, "
                    f"Tugas: {mahasiswa['tugas']}, "
                    f"Rata-rata: {rata_rata:.2f}\n"
                )

            rata_rata_kelas = total / len(data)

            file.write("=====================\n")
            file.write(f"Jumlah mahasiswa: {len(data)}\n")
            file.write(f"Rata-rata kelas: {rata_rata_kelas:.2f}\n")

        print(f"Rekap berhasil ditulis ke {nama_file}.")

    except OSError as error:
        print(f"Terjadi kesalahan saat menulis file: {error}")


# Alur utama
input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data_mahasiswa = baca_data(input_file)
tulis_rekap(output_file, data_mahasiswa)
