import os

# ==========================================
# SIRUANG
# Sistem Informasi Peminjaman Ruang Kampus
# ==========================================

# =========================
# FUNGSI CLEAR TERMINAL
# =========================
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def kembali_ke_menu():
    input("\nTekan Enter untuk kembali ke menu utama...")
    clear_screen()

# =========================
# DATA RUANG KAMPUS
# =========================
jadwal_ruang = {
    "Ruang 101": {},
    "Ruang 102": {},
    "Ruang 103": {},
    "LabKom A": {},
    "LabKom B": {},
    "Lab Jaringan": {},
    "Lab Multimedia": {},
    "Ruang Rapat": {},
    "Aula Seminar": {}
}

# =========================
# DAFTAR HARI
# =========================
hari_kampus = ["senin", "selasa", "rabu", "kamis", "jumat"]

# =========================
# JAM PERKULIAHAN
# =========================
jam_kuliah = {
    1: "07:30",
    2: "08:20",
    3: "09:10",
    4: "10:00",
    5: "10:50",
    6: "11:40",
    7: "13:00",
    8: "13:50",
    9: "14:40",
    10: "15:30",
    11: "16:20",
    12: "17:10"
}

# =========================
# FUNGSI CEK KETERSEDIAAN RUANG
# =========================
def cek_ruang(nama_ruang, hari, jam_mulai, jam_selesai):
    if nama_ruang not in jadwal_ruang:
        return False
    if hari not in jadwal_ruang[nama_ruang]:
        return True
    for jam in range(jam_mulai, jam_selesai + 1):
        if jam in jadwal_ruang[nama_ruang][hari]:
            return False
    return True

# =========================
# FUNGSI SIMPAN DATA PEMINJAMAN
# =========================
def simpan_peminjaman(nama_ruang, hari, jam_mulai, jam_selesai, nama_peminjam, keperluan):
    if cek_ruang(nama_ruang, hari, jam_mulai, jam_selesai):
        if hari not in jadwal_ruang[nama_ruang]:
            jadwal_ruang[nama_ruang][hari] = {}
        for jam in range(jam_mulai, jam_selesai + 1):
            jadwal_ruang[nama_ruang][hari][jam] = {"nama": nama_peminjam, "keperluan": keperluan}
        print("\nPeminjaman berhasil disimpan.")
    else:
        print("\nRuang sedang digunakan pada waktu tersebut.")
        

# =========================
# FITUR PINJAM RUANG
# =========================
def pinjam_ruang():
    print("===== PINJAM RUANG =====")

    # Tampilkan daftar ruang
    daftar_ruang = list(jadwal_ruang.keys())

    print("\nDaftar Ruang:")
    for ruang in daftar_ruang:
        print(f"- {ruang}")

    # =========================
    # INPUT NAMA RUANG (LANGSUNG)
    # =========================
    while True:
        nama_ruang = input("\nMasukkan nama ruang: ").strip()
        
        if nama_ruang in jadwal_ruang:
            break
        else:
            print("Nama ruang tidak tersedia. Silakan cek daftar ruang di atas.")

    # =========================
    # INPUT HARI
    # =========================
    print("\nDaftar Hari:")
    for i, hari in enumerate(hari_kampus, start=1):
        print(f"{i}. {hari.capitalize()}")

    while True:
        try:
            pilih_hari = int(input("\nPilih nomor hari: "))

            if 1 <= pilih_hari <= len(hari_kampus):
                hari = hari_kampus[pilih_hari - 1]
                break
            else:
                print("Pilihan hari tidak tersedia.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # TAMPILKAN JAM
    # =========================
    print("\nJam Perkuliahan:")
    for kode, jam in jam_kuliah.items():
        print(f"{kode}. {jam}")

    # =========================
    # INPUT JAM MULAI
    # =========================
    while True:
        try:
            jam_mulai = int(input("\nMasukkan jam mulai: "))

            if jam_mulai in jam_kuliah:
                break
            else:
                print("Jam mulai tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # INPUT JAM SELESAI
    # =========================
    while True:
        try:
            jam_selesai = int(input("Masukkan jam selesai: "))

            if jam_selesai in jam_kuliah:
                if jam_selesai >= jam_mulai:
                    break
                else:
                    print("Jam selesai tidak boleh sebelum jam mulai.")
            else:
                print("Jam selesai tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # INPUT NAMA PEMINJAM
    # =========================
    while True:
        nama_peminjam = input("Masukkan nama peminjam: ").strip()

        if nama_peminjam != "":
            break
        else:
            print("Nama peminjam tidak boleh kosong.")

    # =========================
    # INPUT KEPERLUAN
    # =========================
    while True:
        keperluan = input("Masukkan keperluan (mata kuliah/acara): ").strip()

        if keperluan != "":
            break
        else:
            print("Keperluan tidak boleh kosong.")

    # =========================
    # SIMPAN PEMINJAMAN
    # =========================
    simpan_peminjaman(
        nama_ruang,
        hari,
        jam_mulai,
        jam_selesai,
        nama_peminjam,
        keperluan
    )

# =========================
# FITUR LIHAT JADWAL
# =========================
def lihat_semua_jadwal():
    print("===== DAFTAR PEMINJAMAN =====")
    
    ada_peminjaman = False
    for ruang, data in jadwal_ruang.items():
        if data:
            ada_peminjaman = True
            print(f"\nRuang: {ruang}")
            for hari, jam_data in data.items():
                for jam, value in jam_data.items():
                    waktu = jam_kuliah[jam]
                    nama = value["nama"] if isinstance(value, dict) else value
                    keperluan = value["keperluan"] if isinstance(value, dict) else "-"
                    print(f"  - {hari.capitalize()} ({waktu}): {nama} - {keperluan}")
    
    if not ada_peminjaman:
        print("\nBelum ada peminjaman ruang.")

def lihat_jadwal_per_ruang():
    while True:
        clear_screen()
        print("===== CEK JADWAL PER RUANG =====")
        
        # Tampilkan daftar ruang yang tersedia
        print("\nDaftar Ruang yang Tersedia:")
        for ruang in jadwal_ruang.keys():
            print(f"- {ruang}")

        print("\nKetik 'menu' untuk kembali ke utama")
        nama = input("\nMasukkan Nama Ruang: ").strip()
        
        if nama.lower() == "menu":
            break
        
        if nama == "":
            print("\nNama ruang tidak boleh kosong!")
            input("\nTekan Enter untuk mencoba lagi...")
            continue
        
        # Cek apakah input cocok dengan nama ruang (case insensitive)
        ruang_ditemukan = None
        for ruang in jadwal_ruang.keys():
            if ruang.lower() == nama.lower():
                ruang_ditemukan = ruang
                break
        
        if ruang_ditemukan:
            data = jadwal_ruang[ruang_ditemukan]
            if data:
                print(f"\nJadwal {ruang_ditemukan}:")
                for hari, jam_data in data.items():
                    for jam, value in jam_data.items():
                        waktu = jam_kuliah[jam]
                        nama_peminjam = value["nama"] if isinstance(value, dict) else value
                        keperluan = value["keperluan"] if isinstance(value, dict) else "-"
                        print(f"  - {hari.capitalize()} ({waktu}): {nama_peminjam} - {keperluan}")
            else:
                print(f"\n{ruang_ditemukan} masih kosong, belum ada peminjaman!")
        else:
            print("\nNama ruang salah atau tidak ada.")
        
        input("\nTekan Enter untuk cek ruang lain...")

# =========================
# FITUR HAPUS PEMINJAMAN
# =========================
def hapus_peminjaman():
    print("===== HAPUS PEMINJAMAN =====")

    # Tampilkan daftar ruang
    print("\nDaftar Ruang:")
    for ruang in jadwal_ruang.keys():
        print(f"- {ruang}")

    # =========================
    # INPUT NAMA RUANG
    # =========================
    while True:
        nama_ruang = input("\nMasukkan nama ruang: ").strip()

        if nama_ruang in jadwal_ruang:
            break
        else:
            print("Nama ruang tidak tersedia.")

    # =========================
    # TAMPILKAN DATA PEMINJAMAN
    # =========================
    data_ruang = jadwal_ruang[nama_ruang]

    if data_ruang:
        print(f"\nData peminjaman di {nama_ruang}:")

        for hari, jam_data in data_ruang.items():
            for jam, value in jam_data.items():

                waktu = jam_kuliah[jam]
                nama = value["nama"]
                keperluan = value["keperluan"]

                print(f"- {hari.capitalize()} ({waktu}) : {nama} - {keperluan}")

    else:
        print("\nBelum ada peminjaman pada ruang ini.")
        return

    # =========================
    # INPUT HARI
    # =========================
    print("\nDaftar Hari:")
    for i, hari in enumerate(hari_kampus, start=1):
        print(f"{i}. {hari.capitalize()}")

    while True:
        try:
            pilih_hari = int(input("\nPilih nomor hari: "))

            if 1 <= pilih_hari <= len(hari_kampus):
                hari = hari_kampus[pilih_hari - 1]
                break
            else:
                print("Pilihan hari tidak tersedia.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # TAMPILKAN JAM
    # =========================
    print("\nJam Perkuliahan:")
    for kode, jam in jam_kuliah.items():
        print(f"{kode}. {jam}")

    # =========================
    # INPUT JAM MULAI
    # =========================
    while True:
        try:
            jam_mulai = int(input("\nMasukkan jam mulai yang ingin dihapus: "))

            if jam_mulai in jam_kuliah:
                break
            else:
                print("Jam mulai tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # INPUT JAM SELESAI
    # =========================
    while True:
        try:
            jam_selesai = int(input("Masukkan jam selesai yang ingin dihapus: "))

            if jam_selesai in jam_kuliah:
                if jam_selesai >= jam_mulai:
                    break
                else:
                    print("Jam selesai tidak boleh sebelum jam mulai.")
            else:
                print("Jam selesai tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # PROSES HAPUS
    # =========================
    data_ditemukan = False

    if hari in jadwal_ruang[nama_ruang]:

        for jam in range(jam_mulai, jam_selesai + 1):

            if jam in jadwal_ruang[nama_ruang][hari]:
                del jadwal_ruang[nama_ruang][hari][jam]
                data_ditemukan = True

        # Hapus hari jika kosong
        if not jadwal_ruang[nama_ruang][hari]:
            del jadwal_ruang[nama_ruang][hari]

    if data_ditemukan:
        print("\nPeminjaman berhasil dihapus.")
    else:
        print("\nData peminjaman tidak ditemukan.")

# =========================
# MENU UTAMA
# =========================
def menu_utama():
    while True:
        print("\n===== SISTEM INFORMASI PEMINJAMAN RUANG KAMPUS =====")
        print("1. Pinjam Ruang")
        print("2. Lihat Semua Jadwal")
        print("3. Lihat Jadwal Per Ruang")
        print("4. Hapus Peminjaman")
        print("5. Keluar")
        pilihan = input("\nPilih menu (1-5): ").strip()
        
        if pilihan == "1":
            clear_screen()
            pinjam_ruang()
            kembali_ke_menu()
        elif pilihan == "2":
            clear_screen()
            lihat_semua_jadwal()
            kembali_ke_menu()
        elif pilihan == "3":
            clear_screen()
            lihat_jadwal_per_ruang()
            clear_screen()
        elif pilihan == "4":
            clear_screen()
            hapus_peminjaman()
            kembali_ke_menu()
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan SIRUANG!")
            break
        else:
            print("\nPilihan tidak valid! Silakan pilih 1-5.")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()

# =========================
# MENJALANKAN PROGRAM
# =========================
clear_screen()
menu_utama()
