import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog
import pyperclip  # Для работы с буфером обмена

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

        self.theme_label = ttk.Label(root, text="Выберите тему:")
        self.theme_label.pack(pady=5)

        self.theme_combobox = ttk.Combobox(root, values=self.style.theme_names())
        self.theme_combobox.set("clam")
        self.theme_combobox.pack(pady=5)

        self.paste_button = ttk.Button(root, text="Вставить из буфера", command=self.paste_from_clipboard)
        self.paste_button.pack(pady=5)

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

    def paste_from_clipboard(self):
        clipboard_data = pyperclip.paste()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, clipboard_data)

    def change_theme(self):
        selected_theme = self.theme_combobox.get()
        if selected_theme:
            try:
                self.style.theme_use(selected_theme)
                print(f"Тема изменена на {selected_theme}")
            except tk.TclError as e:
                print(f"Ошибка при установке темы: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.geometry("400x400")
    root.mainloop()
