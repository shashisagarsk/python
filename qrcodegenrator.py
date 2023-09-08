# pip install qrcode
# pip install image
import qrcode
import image
qr=qrcode.QRCode(
    version=15, # 15 means the version of the qr code 
    box_size=10, # size of the box
    border=5
)
data="https://www.youtube.com/watch?v=g7uvbjuRIpM&t=3s"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")
