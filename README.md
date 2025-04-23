# Steganography-tool
This project focuses on steganography, the art of hiding secret information within media files like images, audio, or videos. The aim is to develop a secure tool for embedding confidential data inside seemingly innocent media, without altering its appearance to the human eye.

Language: Python

Libraries: OpenCV, NumPy, Pillow (PIL), Tkinter (if GUI)

Algorithm: Least Significant Bit (LSB) steganography
Encoding: Converts your message into binary, then modifies the least significant bits of image pixels to embed the data.

Decoding: Reads the modified LSBs to extract and reconstruct the original hidden message.
