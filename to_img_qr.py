import qrcode # pip install qrcode[pil]
qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
