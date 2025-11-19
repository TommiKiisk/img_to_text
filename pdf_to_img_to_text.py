import pytesseract
from pdf2image import convert_from_path

poppler_path = r"C:\Users\tommi\Downloads\Release-25.11.0-0\poppler-25.11.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# converting pdf into images using pdf2image library

pdf_path = r"D:\Tommi\ohke_tekno\img_to_text\test_images\Catan_rules.pdf"

images = convert_from_path(pdf_path,)

# images from pdf to string
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image)
    print(f"Text from page {i + 1}: {text}")