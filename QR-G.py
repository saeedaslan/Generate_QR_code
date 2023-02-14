import pyqrcode
import png
from PIL import Image
link = input("enter anython to generate QR : ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCcode.png")