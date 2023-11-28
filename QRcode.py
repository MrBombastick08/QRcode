import tkinter as tk
from tkinter import ttk, filedialog
import qrcode
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        self.create_widgets()

        # Привязываем событие "Enter" к созданию QR-кода
        self.root.bind('<Return>', lambda event: self.generate_qr_code())

        # Привязываем событие "ESC" к выходу из приложения
        self.root.bind('<Escape>', lambda event: self.root.destroy())

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="Введите данные для кодирования в QR-код:").grid(row=0, column=0, pady=10, sticky=tk.W)
        self.data_entry = ttk.Entry(main_frame, width=40)
        self.data_entry.grid(row=1, column=0, pady=10, sticky=tk.W)

        ttk.Label(main_frame, text="Выберите размер QR кода:").grid(row=2, column=0, pady=10, sticky=tk.W)
        self.error_correction_var = tk.StringVar()
        self.error_correction_var.set("L")
        error_correction_menu = ttk.Combobox(main_frame, textvariable=self.error_correction_var,
                                            values=["L", "M", "Q", "H"], state="readonly")
        error_correction_menu.grid(row=3, column=0, pady=10, sticky=tk.W)

        ttk.Label(main_frame, text="Выберите цвет QR-кода:").grid(row=4, column=0, pady=10, sticky=tk.W)
        self.color_var = tk.StringVar()
        self.color_var.set("black")
        color_menu = ttk.Combobox(main_frame, textvariable=self.color_var,
                                  values=["black", "red", "green", "blue"], state="readonly")
        color_menu.grid(row=5, column=0, pady=10, sticky=tk.W)

        ttk.Button(main_frame, text="Сгенерировать", command=self.generate_qr_code).grid(row=6, column=0, pady=10, sticky=tk.W)
        ttk.Button(main_frame, text="Сохранить в PNG", command=self.save_qr_code).grid(row=7, column=0, pady=10, sticky=tk.W)

        qr_frame = ttk.Frame(self.root, padding="10")
        qr_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.qr_label = ttk.Label(qr_frame, text="Предпросмотр QR-кода", font=("Helvetica", 12))
        self.qr_label.grid(row=0, column=0, pady=10, padx=10, sticky=tk.E)

    def generate_qr_code(self):
        data_to_encode = self.data_entry.get()

        if data_to_encode:
            error_correction = self.error_correction_var.get()
            color = self.color_var.get()

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L if error_correction == "L" else
                                 qrcode.constants.ERROR_CORRECT_M if error_correction == "M" else
                                 qrcode.constants.ERROR_CORRECT_Q if error_correction == "Q" else
                                 qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )

            qr.add_data(data_to_encode)
            qr.make(fit=True)

            qr_img = qr.make_image(fill_color=color, back_color="white")

            img_tk = ImageTk.PhotoImage(qr_img)

            self.qr_label.config(image=img_tk)
            self.qr_label.image = img_tk

    def save_qr_code(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

            if file_path:
                img = Image.open(self.qr_label.image.cget("image"))
                img.save(file_path)
        except AttributeError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
