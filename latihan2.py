class Siswa:
    # Atribut class (sama untuk semua objek)
    sekolah = "SMK PGRI 35 Solokanjeruk"

    # Konstruktor untuk menginisialisasi atribut instance
    def __init__(self, nama, nis, kelas):
        self.nama = nama
        self.nis = nis
        self.kelas = kelas

    # Method untuk menampilkan profil siswa
    def tampilkan_profil_siswa(self):
        print("=== Profil Siswa ===")
        print(f"Nama   : {self.nama}")
        print(f"NIS    : {self.nis}")
        print(f"Kelas  : {self.kelas}")
        print(f"Sekolah: {Siswa.sekolah}")
        print("====================")


# Membuat 3 objek dari class Siswa
siswa1 = Siswa("Ayunda adiarthy G.V", "12345", "XI RPL 3")
siswa2 = Siswa("elsa destiani", "12346", "XI TKJ 3")
siswa3 = Siswa("anomali", "12347", "XI RPL 21")

# Menampilkan data ketiga siswa
siswa1.tampilkan_profil_siswa()
siswa2.tampilkan_profil_siswa()
siswa3.tampilkan_profil_siswa()