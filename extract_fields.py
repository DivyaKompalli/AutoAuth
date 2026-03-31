import sys
from pypdf import PdfReader

reader = PdfReader("PA-Request-Form-UHC-Community-Plan.pdf")
fields = reader.get_form_text_fields()
if fields:
    print("Form fields found:")
    for k, v in fields.items():
        print(f"{k}: {v}")
else:
    print("No AcroForm text fields found.")
