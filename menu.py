# =========================
# DAFTAR HARI
# =========================
hari_kampus = [
    "Senin",
    "Selasa",
    "Rabu",
    "Kamis",
    "Jumat"
]

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
# FUNCTION TAMPIL HARI
# =========================
def tampil_hari():

    print("\n===== DAFTAR HARI =====")

    for hari in hari_kampus:
        print("-", hari)


# =========================
# FUNCTION TAMPIL JAM
# =========================
def tampil_jam():

    print("\n===== JAM PERKULIAHAN =====")

    for sesi, jam in jam_kuliah.items():
        print(f"Sesi {sesi} : {jam}")


# =========================
# FUNCTION DAFTAR RUANG
# =========================

def lihat_ruang():
    print("\nlanjut pak rt.")


# =========================
# MENU UTAMA
# =========================
while True:

    print("\n===== MENU UTAMA =====")
    print("1. Lihat Daftar Hari")
    print("2. Lihat Jam Perkuliahan")
    print("3. Lihat Daftar Ruang")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    # =========================
    # PILIHAN MENU
    # =========================
    if pilihan == "1":
        tampil_hari()

    elif pilihan == "2":
        tampil_jam()

    elif pilihan == "3":
        lihat_ruang()

    elif pilihan == "4":
        print("\nTerima kasih!")
        break

    else:
        print("\nPilihan tidak valid.")