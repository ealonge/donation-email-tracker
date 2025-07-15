import re

def parse_cashapp_email(email_text):
    name_match = re.search(r"from ([A-Z][a-z]+ [A-Z][a-z]+)", email_text)
    amount_match = re.search(r"\$(\d+\.\d{2})", email_text)
    note_match = re.search(r"Note: (.+)", email_text)
    date_match = re.search(r"Date: (.+)", email_text)

    return {
        "name": name_match.group(1) if name_match else None,
        "amount": float(amount_match.group(1)) if amount_match else None,
        "note": note_match.group(1) if note_match else None,
        "date": date_match.group(1) if date_match else None
    }

# Load and test
with open("sample_cashapp_email.txt", "r") as f:
    text = f.read()
    result = parse_cashapp_email(text)
    print(result)
