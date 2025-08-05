import pytesseract
from PIL import Image

image_path = r"image2.jpeg"
image = Image.open(image_path)

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\farra\Tesseract\tesseract.exe"

extracted_text = pytesseract.image_to_string(image)
print(extracted_text)