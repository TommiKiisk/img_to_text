from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
print("start")
image = Image.open('test_images/mathquote.jpg')
grayImage = image.convert('L')
text = pytesseract.image_to_string(grayImage)
print(text)
print("end")