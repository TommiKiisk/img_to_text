from PIL import Image
import pytesseract
import cv2
from pdf2image import convert_from_path

poppler_path = r"C:\Users\tommi\Downloads\Release-25.11.0-0\poppler-25.11.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("start")
import sys
print(sys.executable)
import subprocess
print(subprocess.getoutput("pdfinfo -v"))

# read img with
image = cv2.imread('test_images/mathquote.jpg')

# convert into black and white
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


# save temporary image for PIL
cv2.imwrite("temporary.jpg", thresh)

text = pytesseract.image_to_string(Image.open("temporary.jpg"))

print(text)

print("part 2: pdf to text")

# converting pdf into images using pdf2image library

pdf_path = r"D:\Tommi\ohke_tekno\img_to_text\test_images\Catan_rules.pdf"

images = convert_from_path(pdf_path, userpw="",)

# images from pdf to string
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image)
    print(f"Text from page {i + 1}: {text}")


print("end")