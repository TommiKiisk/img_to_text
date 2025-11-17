from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
print("start")

print(pytesseract.image_to_string(Image.open('test_images/mathquote.jpg')))
print("end")