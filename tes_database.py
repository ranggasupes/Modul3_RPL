from config.database import Database

print("1. Memulai tes database")

db = Database()
print("2. Objek Database berhasil dibuat")

conn = db.get_connection()
print("3. Hasil koneksi:", conn)

if conn:
    print("4. Database berhasil terhubung")
    conn.close()
else:
    print("4. Koneksi database gagal")

input("Tekan Enter untuk keluar...")