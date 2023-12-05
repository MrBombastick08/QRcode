import tkinter as tk
from tkinter import ttk, simpledialog
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор QR кодов")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.qr_label = ttk.Label(root)
        self.qr_label.pack(pady=10)

        self.entry_label = ttk.Label(root, text="Введите текст:")
        self.entry_label.pack(pady=5)

        self.entry = ttk.Entry(root, width=30)
        self.entry.pack(pady=5)

        self.generate_button = ttk.Button(root, text="Сгенерировать", command=self.generate_qr)
        self.generate_button.pack(pady=5)

        self.save_button = ttk.Button(root, text="Сохранить в PNG", command=self.save_qr)
        self.save_button.pack(pady=5)

        self.theme_button = ttk.Button(root, text="Выбрать тему", command=self.change_theme)
        self.theme_button.pack(pady=5)

        root.bind('<Escape>', self.exit_fullscreen)
        root.bind('<Return>', self.generate_qr)

    def generate_qr(self, event=None):
        data = self.entry.get()
        if data:
            data_bytes = data.encode('utf-8')

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data_bytes)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((300, 300), Image.LANCZOS)

            self.photo = ImageTk.PhotoImage(img)
            self.qr_label.config(image=self.photo)
            self.qr_label.image = self.photo

    def save_qr(self):
        data = self.entry.get()
        if data:
            data_bytes = data.encode('utf-8')

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data_bytes)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((300, 300), Image.LANCZOS)

            filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

            if filename:
                img.save(filename)

    def exit_fullscreen(self, event):
        self.root.destroy()

    def change_theme(self):
        # Список доступных тем
        available_themes = self.style.theme_names()

        # Строка с информацией о темах
        themes_info = "Доступные темы:\n" + "\n".join(available_themes)

        # Диалоговое окно для ввода имени темы
        theme_name = simpledialog.askstring("Выбор темы", "Введите имя темы:\n\n" + themes_info)

        if theme_name:
            try:
                self.style.theme_use(theme_name)
                print(f"Тема изменена на {theme_name}")
            except tk.TclError as e:
                print(f"Ошибка при установке темы: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.geometry("400x400")
    root.mainloop()
