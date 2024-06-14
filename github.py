
import qrcode

# QR kodu oluştur
url = "https://github.com/hassoonsy2/PepperGPT"
qr = qrcode.make(url)

# QR kodunu kaydet
qr.save("github.png")
