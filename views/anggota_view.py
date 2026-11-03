
import customtkinter as ctk
from tkinter import ttk


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Tema utama
        ctk.set_appearance_mode("light")
        self.configure(fg_color="white")

        self.title("Sistem Manajemen Perpustakaan - Data Anggota")
        self.geometry("1000x550")

        # Konfigurasi grid utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Warna
        hijau = "#198754"
        hijau_hover = "#E2F3E9"
        putih = "#FFFFFF"

        # FRAME KIRI: FORM INPUT
        self.frame_kiri = ctk.CTkFrame(
            self,
            fg_color=putih,
            border_color=hijau,
            border_width=2,
            corner_radius=12
        )
        self.frame_kiri.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Anggota",
            font=("Arial", 18, "bold"),
            text_color=hijau
        ).pack(pady=18)

        # Input nama anggota
        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Anggota",
            fg_color=putih,
            text_color="#333333",
            border_color=hijau,
            border_width=1,
            corner_radius=8
        )
        self.entry_nama.pack(
            pady=10, padx=15, fill="x"
        )

        # Input alamat
        self.entry_alamat = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Alamat Anggota",
            fg_color=putih,
            text_color="#333333",
            border_color=hijau,
            border_width=1,
            corner_radius=8
        )
        self.entry_alamat.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol simpan
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color=putih,
            text_color=hijau,
            border_color=hijau,
            border_width=2,
            hover_color=hijau_hover,
            corner_radius=8
        )
        self.btn_simpan.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol update
        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data (Update)",
            fg_color=putih,
            text_color=hijau,
            border_color=hijau,
            border_width=2,
            hover_color=hijau_hover,
            corner_radius=8
        )
        self.btn_update.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol hapus
        self.btn_hapus = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data (Delete)",
            fg_color=putih,
            text_color=hijau,
            border_color=hijau,
            border_width=2,
            hover_color=hijau_hover,
            corner_radius=8
        )
        self.btn_hapus.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol bersihkan form
        self.btn_bersihkan = ctk.CTkButton(
            self.frame_kiri,
            text="Bersihkan Form",
            fg_color=putih,
            text_color=hijau,
            border_color=hijau,
            border_width=2,
            hover_color=hijau_hover,
            corner_radius=8
        )
        self.btn_bersihkan.pack(
            pady=10, padx=15, fill="x"
        )

        # FRAME KANAN: TABEL ANGGOTA
        self.frame_kanan = ctk.CTkFrame(
            self,
            fg_color=putih,
            border_color=hijau,
            border_width=2,
            corner_radius=12
        )
        self.frame_kanan.grid(
            row=0, column=1,
            padx=10, pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Anggota Perpustakaan",
            font=("Arial", 18, "bold"),
            text_color=hijau
        ).pack(pady=18)

        # Gaya tabel Treeview
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="white",
            foreground="#333333",
            fieldbackground="white",
            rowheight=28,
            borderwidth=1
        )

        style.configure(
            "Treeview.Heading",
            background="#E2F3E9",
            foreground="#333333",
            font=("Arial", 10, "bold"),
            relief="flat"
        )

        style.map(
            "Treeview",
            background=[("selected", "#B7E4C7")],
            foreground=[("selected", "#333333")]
        )

        # Tabel anggota
        kolom = ("id", "nama", "alamat")

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15
        )

        self.tabel.heading("id", text="ID Anggota")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        self.tabel.column(
            "id", width=80, anchor="center"
        )
        self.tabel.column("nama", width=200)
        self.tabel.column("alamat", width=250)

        self.tabel.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )


if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()
