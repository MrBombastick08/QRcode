import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.maken(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    data_to_encode = input("Введите данные для кодирования в QR-код: ")
    file_name = input("Введите имя файла для сохранения QR-кода (включая расширение .png): ")

    generate_qr_code(data_to_encode, file_name)
    print(f"QR-код сохранен в файл {file_name}")