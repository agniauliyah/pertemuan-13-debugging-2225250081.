
def baca_nilai(nama_file):
    nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                data = baris.strip().split(",")

                if len(data) == 2:
                    try:
                        angka = int(data[1])
                        nilai.append(angka)
                    except ValueError:
                        print(f"Nilai tidak valid: {baris.strip()}")

        return nilai

    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return []


if __name__ == "__main__":
    hasil = baca_nilai(
        r"C:\Users\agnia\OneDrive\Documents\OneDrive\KULIAH\Semester 3\Alpro\Pertemuan 12\pertemuan-12-file-io-2225250081\data\nilai.txt"
    )

    print("Data nilai dari file:", hasil)
