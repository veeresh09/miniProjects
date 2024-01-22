import pytesseract
from PIL import Image

# Path to the image
image_path = 'text1.png'

# Open the image
img = Image.open(image_path)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# Print the text
print(text)
