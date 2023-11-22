import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import qrcode

class QRCodeGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR Code Generator")

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Введите данные для QR-кода:").grid(row=0, column=0, padx=10, pady=10)

        self.entry = ttk.Entry(self.root)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Button(self.root, text="Создать QR-код", command=self.generate_qr_code).grid(row=1, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Сохранить в PNG", command=self.save_qr_code).grid(row=3, column=0, columnspan=2, pady=10)

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

            # Сохранение изображения QR-кода в объекте
            self.generated_image = img
            self.generated_qr = qr

    def save_qr_code(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if filename:
                img = self.generated_qr.make_image(fill_color="black", back_color="white")
                img.save(filename)
                tk.messagebox.showinfo("Сохранено", f"QR-код сохранен в файл: {filename}")
        except Exception as e:
            tk.messagebox.showerror("Ошибка", f"Не удалось сохранить QR-код. {str(e)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = QRCodeGenerator()
    app.run()

