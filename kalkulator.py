

print("=== Kalkulator Sederhana ===")
print("Pilih operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

# Meminta input dari pengguna
pilihan = input("Masukkan pilihan operasi (1/2/3/4): ")

# Memasukkan dua angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Percabangan untuk menentukan operasi
if pilihan == '1':
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")

elif pilihan == '2':
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")

elif pilihan == '3':
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")

elif pilihan == '4':
    # Tambahkan pengecekan agar tidak membagi dengan nol
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Tidak bisa membagi dengan nol!")

else:
    print("Pilihan operasi tidak valid. Silakan coba lagi.")