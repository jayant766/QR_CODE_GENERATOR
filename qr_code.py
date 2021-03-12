import qrcode
qr=qrcode.QrCode(
    version=1,
    box_size=10,
    border=5
)

data="https://github.com/jayant766"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",black_color="White")
img.save("3.png")