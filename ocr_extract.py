import pytesseract
from PIL import Image
import re
import io

# Agar Windows me ho toh Tesseract ka path set karo
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_image(uploaded_file):
    # Convert uploaded file to PIL image
    image = Image.open(io.BytesIO(uploaded_file.read()))
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

def verify_id_card(extracted_text):
    """
    Simple rule-based fake ID detection
    """
    # Rule 1: Student ID format check (123-456-7890)
    id_pattern = r"\d{3}-\d{3}-\d{4}"
    if not re.search(id_pattern, extracted_text):
        return "Fake", "Invalid ID format"

    # Rule 2: DOB realistic check (MM/YYYY or DD/MM/YYYY)
    dob_pattern = r"(\d{2})/(\d{4})"
    match = re.search(dob_pattern, extracted_text)
    if match:
        year = int(match.group(2))
        if year < 1990 or year > 2025:
            return "Fake", "DOB year not valid"
    else:
        return "Fake", "DOB missing"

    # Rule 3: Name should be alphabetic
    name_pattern = r"Name\s*:\s*[A-Za-z ]+"
    if not re.search(name_pattern, extracted_text):
        return "Fake", "Invalid name format"

    return "Real", "Document looks valid"

