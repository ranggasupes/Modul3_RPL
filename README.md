# Sistem Manajemen Perpustakaan

## 1. Deskripsi Aplikasi

Sistem Manajemen Perpustakaan merupakan aplikasi desktop berbasis Python yang digunakan untuk mengelola data koleksi buku. Aplikasi ini menerapkan arsitektur Model-View-Controller (MVC) dan menggunakan MySQL sebagai database.

Fitur utama aplikasi meliputi:
- Login pengguna.
- Menampilkan daftar buku.
- Menambahkan data buku.
- Memperbarui data buku.
- Menghapus data buku.
- Pembatasan hak akses berdasarkan role admin dan anggota.

## 2. Struktur Direktori MVC

Struktur direktori proyek:

```text
Modul 3/
├── config/
│   └── database.py
├── controllers/
│   ├── auth_controller.py
│   └── buku_controller.py
├── models/
│   ├── user_model.py
│   └── buku_model.py
├── views/
│   ├── login_view.py
│   └── buku_view.py
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
├── main.py
├── requirements.txt
└── README.md
```

Pembagian MVC:
- **Model:** Mengelola data pengguna, data buku, dan komunikasi dengan database.
- **View:** Mengatur tampilan antarmuka login dan pengelolaan buku.
- **Controller:** Mengatur proses autentikasi dan operasi pengelolaan buku.
- **Config:** Menyimpan konfigurasi koneksi database.

## 3. Panduan Instalasi dan Konfigurasi Database MySQL

### A. Persyaratan Sistem

- Python 3.11
- MySQL Server
- pip
- Visual Studio Code (opsional)

### B. Instalasi Aplikasi

1. Clone repositori GitHub:

   ```bash
   git clone URL_REPOSITORI
   ```

2. Masuk ke direktori proyek:

   ```bash
   cd "Modul 3"
   ```

3. Buat virtual environment:

   ```bash
   python -m venv env
   ```

4. Aktifkan virtual environment pada Windows:

   ```powershell
   env\Scripts\activate
   ```

5. Instal dependensi:

   ```bash
   pip install -r requirements.txt
   ```

### C. Konfigurasi Database MySQL

1. Jalankan MySQL Server melalui Laragon atau aplikasi pengelola MySQL lainnya.
2. Buat database sesuai nama database yang digunakan dalam konfigurasi proyek.
3. Periksa konfigurasi koneksi pada file `config/database.py`.
4. Sesuaikan host, username, password, dan nama database dengan konfigurasi MySQL lokal.
5. Pastikan tabel pengguna dan buku sudah tersedia sesuai struktur yang digunakan oleh aplikasi.

## 4. Cara Menjalankan Aplikasi

1. Pastikan MySQL Server sudah berjalan.
2. Aktifkan virtual environment:

   ```powershell
   env\Scripts\activate
   ```

3. Jalankan aplikasi:

   ```bash
   python main.py
   ```

4. Masukkan username dan password pada halaman login.
5. Setelah berhasil login, pengguna akan diarahkan ke halaman aplikasi sesuai hak aksesnya.