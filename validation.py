import re
from datetime import datetime

def validate_name(name):
    if not name:
        return False, "Name not found"
    elif not all(x.isalpha() or x.isspace() for x in name):
        return False, "Name contains invalid characters"
    else:
        return True, "Valid name"

def validate_student_id(student_id):
    if not student_id:
        return False, "Student ID not found"
    elif re.match(r'^\d{3}-\d{3}-\d{4}$', student_id):
        return True, "Valid Student ID"
    else:
        return False, "Invalid Student ID format"

def validate_dob(dob_str):
    if not dob_str:
        return False, "DOB not found"
    try:
        if len(dob_str.split('/')) == 2:
            dob = datetime.strptime(dob_str, '%m/%Y')
        else:
            dob = datetime.strptime(dob_str, '%m/%d/%Y')

        if dob > datetime.now():
            return False, "DOB is in the future"
        else:
            return True, "Valid DOB"
    except ValueError:
        return False, "Invalid DOB format"

def validate_address(address):
    if not address:
        return False, "Address not found"
    else:
        return True, "Address found"

def validate_id_text(text):
    results = {}

    name_match = re.search(r'Name\s*[:\-]?\s*(.+)', text)
    student_id_match = re.search(r'Student ID\s*[:\-]?\s*([\d\-]+)', text)
    dob_match = re.search(r'DOB\s*[:\-]?\s*(\d{2}/\d{4}|\d{2}/\d{2}/\d{4})', text)
    address_match = re.search(r'Address\s*[:\-]?\s*(.+)', text)

    # Validate fields, store (bool, message)
    results['Name'] = validate_name(name_match.group(1).strip() if name_match else None)
    results['Student ID'] = validate_student_id(student_id_match.group(1).strip() if student_id_match else None)
    results['DOB'] = validate_dob(dob_match.group(1).strip() if dob_match else None)
    results['Address'] = validate_address(address_match.group(1).strip() if address_match else None)

    return results
