print("=== Kalkulator Sederhana ===")

while True:
    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == "5":
        print("Terima kasih! Program selesai.")
        break

    # Input angka dari pengguna
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")
        continue

    # Logika menggunakan if, elif, else
    if pilihan == "1":
        hasil = angka1 + angka2
        print(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif pilihan == "2":
        hasil = angka1 - angka2
        print(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif pilihan == "3":
        hasil = angka1 * angka2
        print(f"Hasil: {angka1} * {angka2} = {hasil}")
    elif pilihan == "4":
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"Hasil: {angka1} / {angka2} = {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan!")
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")