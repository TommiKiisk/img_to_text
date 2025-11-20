import pytesseract
from pdf2image import convert_from_path

poppler_path = r"C:\Users\tommi\Downloads\Release-25.11.0-0\poppler-25.11.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# converting pdf into images using pdf2image library


kysypdf = input("Give path to the pdf: ")

print("start")
if kysypdf:
    pdf_path = kysypdf
else:
    pdf_path = r"D:\Tommi\ohke_tekno\img_to_text\test_images\Catan_rules.pdf"
images = convert_from_path(pdf_path,)
whole_text = ""

# images from pdf to string
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image.convert('L'))
    whole_text += text

print(whole_text)
    
print("converting end")

nimi = input("Name the output file (without .txt): ")

filename = nimi + ".txt"

with open(filename, 'w') as file:
    file.write(whole_text)
    
