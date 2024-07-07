# QRcode-generator

This Python project is a simple and user-friendly QR code generator. It uses the qrcode library to generate QR codes and tkinter for the graphical user interface. Users can input the data to be encoded, choose the colors for the QR code, and save the generated image.


Features

1.User Input: Allows users to input data for the QR code through a dialog box. 

2.Customizable Colors: Users can specify the fill and background colors of the QR code.

3.Save to File: The generated QR code can be saved as an image file.

4.Error Handling: Provides error messages if the input is invalid or if an error occurs during QR code generation.

Usage

Follow the prompts:

1.Enter the data for the QR code.

2.Specify the fill color (e.g., black, red).

3.Specify the background color (e.g., white).

4.Enter the file name to save the QR code (e.g., qrcode.png).

Example

Here's a brief walkthrough of using the script:

1.After running the script, a dialog box will prompt you to enter the data for the QR code. 

2.Another dialog box will ask for the fill color, followed by one for the background color.

3.Finally, you'll be prompted to enter the file name to save the QR code.

4.The generated QR code will be displayed, and a success message will confirm that the QR code has been saved.

Explanation of code

1.The generate_qr_code function creates the QR code with the specified data and colors and saves it to a file.

2.The display_qr_code function opens the generated QR code image.

3.The main function handles the user input and orchestrates the QR code generation and display process.

5.The QR code will be generated and displayed, and a message box will confirm the success.

 
