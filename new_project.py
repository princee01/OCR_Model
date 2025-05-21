
#----------------------------------------------------------------main code---------------------
import easyocr
import cv2
import re

def extract_handwritten_text(image_path):
    reader = easyocr.Reader(['en'])  # Language = English
    result = reader.readtext(image_path)

    formatted_text = ""
    for detection in result:
        text = detection[1]
        # If text starts with a number (like "1", "2", etc.)
        if re.match(r"^\d", text):
            formatted_text += f"\n{text}\n"
        else:
            formatted_text += text + " "

    return formatted_text.strip()

if __name__ == "__main__":
    image_path = "Screenshot 2025-05-20 225502.png"
    text = extract_handwritten_text(image_path)
    print("Formatted Extracted Text:\n1.", text)

