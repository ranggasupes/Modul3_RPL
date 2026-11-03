import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController


class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()
        self.view.btn_login.configure(command=self.proses_login)

    def proses_login(self):
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan Password wajib diisi"
            )
            return

        user = self.model.autentikasi(username, password)

        if user:
            messagebox.showinfo(
                "Login berhasil",
                f"Selamat datang, {user['username']} ({user['role']})"
            )

            # Sembunyikan jendela Login
            self.view.withdraw()

            # Buka jendela utama Perpustakaan dengan mengirimkan role pengguna
            app_utama = BukuController(
                user_role=user['role'],
                master=self.view,
                on_logout=self.logout
            )

        else:
            messagebox.showerror(
                "Login Gagal",
                "Username atau Password salah"
            )

    def logout(self):
        # Tampilkan kembali jendela Login
        self.view.deiconify()

        # Kosongkan input username dan password
        self.view.entry_username.delete(0, "end")
        self.view.entry_password.delete(0, "end")

    def run(self):
        self.view.mainloop()