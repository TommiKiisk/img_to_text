from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("start")

kuva = input("Give path of the image: ")

if kuva:
    image = cv2.imread(f"{kuva}")
else:
    image = cv2.imread('test_images/mathquote.jpg')

# convert into black and white
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


# save temporary image for PIL
cv2.imwrite("temporary.jpg", thresh)

text = pytesseract.image_to_string(Image.open("temporary.jpg"))

print(text)

print("end")