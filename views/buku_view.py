import customtkinter as ctk
from tkinter import ttk


class BukuView(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)

        # Tema utama
        ctk.set_appearance_mode("light")
        self.configure(fg_color="white")

        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("1000x550")

        # Konfigurasi grid utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Warna
        pink = "#FF69B4"
        pink_hover = "#FFE4EF"
        putih = "#FFFFFF"

        # FRAME KIRI: FORM INPUT
        self.frame_kiri = ctk.CTkFrame(
            self,
            fg_color=putih,
            border_color=pink,
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
            text="Form Data Buku",
            font=("Arial", 18, "bold"),
            text_color=pink
        ).pack(pady=18)

        # Input judul
        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Judul Buku",
            fg_color=putih,
            text_color="#333333",
            border_color=pink,
            border_width=1,
            corner_radius=8
        )
        self.entry_judul.pack(
            pady=10, padx=15, fill="x"
        )

        # Input penulis
        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Penulis",
            fg_color=putih,
            text_color="#333333",
            border_color=pink,
            border_width=1,
            corner_radius=8
        )
        self.entry_penulis.pack(
            pady=10, padx=15, fill="x"
        )

        # Input tahun
        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Tahun Terbit (Misal: 2024)",
            fg_color=putih,
            text_color="#333333",
            border_color=pink,
            border_width=1,
            corner_radius=8
        )
        self.entry_tahun.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol simpan
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color=putih,
            text_color=pink,
            border_color=pink,
            border_width=2,
            hover_color=pink_hover,
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
            text_color=pink,
            border_color=pink,
            border_width=2,
            hover_color=pink_hover,
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
            text_color=pink,
            border_color=pink,
            border_width=2,
            hover_color=pink_hover,
            corner_radius=8
        )
        self.btn_hapus.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol Logout
        self.btn_logout = ctk.CTkButton(
            self.frame_kiri,
            text="Logout",
            fg_color="red",
            text_color=putih,
            hover_color="#CC0000",
            corner_radius=8
        )
        self.btn_logout.pack(
            pady=10, padx=15, fill="x"
        )

        # FRAME KANAN: TABEL BUKU
        self.frame_kanan = ctk.CTkFrame(
            self,
            fg_color=putih,
            border_color=pink,
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
            text="Daftar Koleksi Buku",
            font=("Arial", 18, "bold"),
            text_color=pink
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
            bordercolor=pink,
            borderwidth=1
        )

        style.configure(
            "Treeview.Heading",
            background="#FFE4EF",
            foreground="#333333",
            font=("Arial", 10, "bold"),
            relief="flat"
        )

        style.map(
            "Treeview",
            background=[("selected", "#FFC0CB")],
            foreground=[("selected", "#333333")]
        )

        # Tabel
        kolom = ("id", "judul", "penulis", "tahun")

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15
        )

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun Terbit")

        self.tabel.column(
            "id", width=50, anchor="center"
        )
        self.tabel.column("judul", width=200)
        self.tabel.column("penulis", width=160)
        self.tabel.column(
            "tahun", width=100, anchor="center"
        )

        self.tabel.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()
