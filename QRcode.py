import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор QR кодов")

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

        # Добавление обработчиков событий для клавиш ESC и Enter
        root.bind('<Escape>', self.exit_fullscreen)
        root.bind('<Return>', self.generate_qr)

    def generate_qr(self, event=None):
        data = self.entry.get()
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((300, 300), Image.LANCZOS)

            self.photo = ImageTk.PhotoImage(img)
            self.qr_label.config(image=self.photo)
            self.qr_label.image = self.photo

    def save_qr(self):
        data = self.entry.get()
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((300, 300), Image.LANCZOS)

            filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

            if filename:
                img.save(filename)

    def exit_fullscreen(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.geometry("400x400")  # Устанавливаем размер окна
    root.mainloop()
