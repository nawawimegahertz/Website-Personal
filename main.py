info_rahasia = "Info rahasia:"
nilai = 909
nilai2 = nilai + 1
jumlah_percobaan = 0
maksimum_percobaan = 3

while jumlah_percobaan < maksimum_percobaan:
    try:
        input_nilai = input("Masukkan nilai Anda: ")
        nilai_input = int(input_nilai)
    except ValueError:
        print("Masukan harus berupa angka.")
        jumlah_percobaan += 1
        continue

    if nilai_input == nilai:
        try:
            input_dua = input("Silakan masukkan kode lapis kedua: ")
            nilai_dua = int(input_dua)
        except ValueError:
            print("Masukkan kode lapis kedua harus berupa angka.")
            jumlah_percobaan += 1
            continue

        if nilai_dua == nilai2:
            print(info_rahasia)
            break  # Keluar dari loop jika berhasil
        else:
            print('''
            Yah, kode ke-2 salah nih
            ''')
    else:
        print('''
        Yah, salah kode nih
        ''')
        jumlah_percobaan += 1

if jumlah_percobaan == maksimum_percobaan:
    print("Akses diblokir karena melebihi batas (3 kali) percobaan.")