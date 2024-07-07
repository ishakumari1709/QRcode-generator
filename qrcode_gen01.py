import qrcode
import qrcode.constants
from PIL import Image
import tkinter as tk
from tkinter import simpledialog, messagebox

def generate_qr_code(data, fill_color, back_color, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=10,
    )

    # Add data to the QRCode object
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QRCode object
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image
    img.save(file_name)
    return img

def display_qr_code(img):
    img.show()

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    # Get user input for QR code data
    data = simpledialog.askstring("Input", "Enter the data for the QR code:")
    if not data:
        messagebox.showerror("Error", "No data provided. Exiting.")
        return

    # Get user input for QR code colors
    fill_color = simpledialog.askstring("Input", "Enter the fill color (e.g., black, red):", initialvalue="red")
    back_color = simpledialog.askstring("Input", "Enter the background color (e.g., white):", initialvalue="white")
    file_name = simpledialog.askstring("Input", "Enter the file name to save (e.g., qrcode.png):", initialvalue="wesev.png")

    try:
        # Generate and display the QR code
        img = generate_qr_code(data, fill_color, back_color, file_name)
        display_qr_code(img)
        messagebox.showinfo("Success", f"QR Code generated and saved as {file_name}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()


