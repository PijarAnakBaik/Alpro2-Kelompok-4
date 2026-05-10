# SIRUANG
## Sistem Informasi Peminjaman Ruang Kampus

SIRUANG adalah program berbasis Python yang dibuat untuk membantu proses pengelolaan peminjaman ruang kampus secara sederhana, terstruktur, dan efisien melalui Command Line Interface (CLI).

Program ini dikembangkan sebagai tugas kelompok mata kuliah Algoritma Pemrograman II dengan menerapkan berbagai konsep dasar pemrograman dan logika algoritma.

---

# Deskripsi Proyek

Sistem ini memungkinkan pengguna untuk:
- Melihat jadwal peminjaman ruang
- Mengecek ketersediaan ruang
- Melakukan peminjaman ruang
- Menghapus data peminjaman
- Mengelola jadwal berdasarkan hari dan jam perkuliahan

Program menggunakan struktur data dictionary untuk menyimpan data jadwal ruang secara dinamis.

---

# Fitur Utama

- Melihat seluruh jadwal peminjaman
- Melihat jadwal ruang tertentu
- Mengecek ketersediaan ruang
- Melakukan peminjaman ruang
- Menghapus data peminjaman
- Validasi input pengguna
- Sistem jadwal berdasarkan hari dan jam
- Tampilan terminal interaktif

---

# Konsep Pemrograman yang Digunakan

Program ini mengimplementasikan beberapa konsep dasar Algoritma Pemrograman II, seperti:

- Variabel dan tipe data
- Percabangan (`if`, `elif`, `else`)
- Perulangan (`for`, `while`)
- Fungsi (`function`)
- Dictionary dan nested dictionary
- Validasi input
- Modular programming

---

# Struktur Sistem

## Daftar Ruang Kampus

- Ruang 101
- Ruang 102
- Ruang 103
- LabKom A
- LabKom B
- Lab Jaringan
- Lab Multimedia
- Ruang Rapat
- Aula Seminar

---

# Hari Operasional

- Senin
- Selasa
- Rabu
- Kamis
- Jumat

---

# Jam Perkuliahan

| Jam Ke | Waktu |
|--------|--------|
| 1 | 07:30 |
| 2 | 08:20 |
| 3 | 09:10 |
| 4 | 10:00 |
| 5 | 10:50 |
| 6 | 11:40 |
| 7 | 13:00 |
| 8 | 13:50 |
| 9 | 14:40 |
| 10 | 15:30 |
| 11 | 16:20 |
| 12 | 17:10 |

---

# Sistem Peminjaman

Peminjaman ruang dilakukan berdasarkan:
- Hari
- Jam mulai
- Jam selesai

### Contoh:
- Senin | Jam 1 - Jam 3
- Rabu | Jam 7 - Jam 9

Sistem akan otomatis:
- Mengecek bentrok jadwal
- Menolak peminjaman jika ruang sedang digunakan

---

# Fitur Hapus Peminjaman

Sistem menyediakan fitur penghapusan data peminjaman berdasarkan:
- Nama ruang
- Hari
- Rentang jam

Pengguna juga dapat melihat data peminjaman terlebih dahulu sebelum menghapus jadwal.

---

# Teknologi yang Digunakan

- Python
- Visual Studio Code
- Command Line Interface (CLI)
- Git & Github

---

# Tujuan Pengembangan

- Mengimplementasikan materi Algoritma Pemrograman II
- Melatih logika pemrograman
- Mengembangkan studi kasus sistem informasi sederhana
- Melatih kerja sama tim dalam pengembangan program

---

# Pengembangan Selanjutnya

Sistem ini masih dapat dikembangkan menjadi:

- GUI Desktop Application
- Web Application
- Database Integration
- Login Multi-user System
- Sistem Reservasi Online Kampus
- Penyimpanan data otomatis (JSON/Database)

---

# Tim Pengembang

Proyek SIRUANG dikembangkan oleh kelompok mahasiswa sebagai tugas mata kuliah Algoritma Pemrograman II.

## Anggota Kelompok

| No | Nama |
|----|------|
| 1 | Much. Mentari Adriansyah |
| 2 | Muhammad Abdurrahman |
| 3 | Hafidzar Ashyawal Sinatryas |
| 4 | Wafah Khonia |

## Catatan
Repository ini dibuat sebagai tugas akademik sekaligus referensi pengembangan sistem informasi sederhana berbasis Python.
