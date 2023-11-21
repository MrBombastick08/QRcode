import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import qrcode

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Введите данные для QR-кода:").grid(row=0, column=0, padx=10, pady=10)

        self.entry = ttk.Entry(self.root)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Button(self.root, text="Создать QR-код", command=self.generate_qr_code).grid(row=1, column=0, columnspan=2, pady=10)

        # Метка для отображения QR-кода
        self.qr_label = ttk.Label(self.root)
        self.qr_label.grid(row=2, column=0, columnspan=2, pady=10)

    def generate_qr_code(self):
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

            # Преобразование изображения для отображения в Tkinter
            img = ImageTk.PhotoImage(img)
            self.qr_label.config(image=img)
            self.qr_label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
