import qrcode
import qrcode.constants
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=10,
)

# Add data to the QRCode object
qr.add_data("https://www.linkedin.com/in/ishakumari1709")

qr.make(fit=True)

# Create an image from the QRCode object
img = qr.make_image(fill_color="red", back_color="white")

# Save the image
img.save("linkedinqr.png")
