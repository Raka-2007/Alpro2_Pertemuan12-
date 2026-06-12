#Raka Emillul Fata
#Praktikum 12

#A. Menampilkan menu utama
def tampilan_menu():
    print("\n=====SISTEM NILAI MAHASISWA=====")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Cari Data Mahasiswa")
    print("4. Hitung Rata-rata Nilai Mahasiswa")
    print("5. Keluar")

#B. Menambahkan data mahasiswa
def tambah_data_mahasiswa(data, nim_set):
    nim = input("Masukkan NIM: ")

    #Set data
    if nim in nim_set:
        print("NIM sudah ada!")
        return
    try:
        nilai = float(input("Masukkan Nilai: "))
        data[nim] = nilai
        nim_set.add(nim)
        print("Data mahasiswa berhasil ditambahkan.")
    except ValueError:
        print("Nilai harus berupa angka.")

#C. Menampilkan data mahasiswa
def tampilkan_data_mahasiswa(data):
    if not data:
        print("Data mahasiswa kosong.")
    else:
        for nim, nilai in data.items():
            print(f"NIM: {nim}, Nilai: {nilai}")

#D. Mencari data mahasiswa
def cari_data_mahasiswa(data):
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in data:
        print(f"NIM: {nim}, Nilai: {data[nim]}")
    else:
        print("Data mahasiswa tidak ditemukan.")

#E. Menghapus data mahasiswa
def hitung_rata(data):
    if not data:
        print("Data mahasiswa kosong.")
        return 0
    total = sum(data.values())
    rata_rata = total / len(data)
    print(f"Rata-rata nilai mahasiswa: {rata_rata}")
    return rata_rata

#F. Program utama
def main():
    data = {}
    nim_set = set()
    while True:
        tampilan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_data_mahasiswa(data, nim_set)
        elif pilihan == '2':
            tampilkan_data_mahasiswa(data)
        elif pilihan == '3':
            cari_data_mahasiswa(data)
        elif pilihan == '4':
            hitung_rata(data)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()