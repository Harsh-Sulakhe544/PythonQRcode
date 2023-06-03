import qrcode
from PIL import Image

# QRCode reduces the error
qr=qrcode.QRCode(version = 1 , 
                error_correction = qrcode.constants.ERROR_CORRECT_H, 
                box_size=10 , border=4)

qr.add_data("https://www.harvard.edu/")
qr.make(fit=True)
img=qr.make_image(fill_color = "red" , back_color = "white")  # back_color can be changable (but white sacns easily )
img.save("Harvard_University_website.png")
 