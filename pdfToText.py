import os
import PyPDF2

# Ask user for the PDF file name
pdf_file_name = input("Enter the PDF file name (with .pdf extension): ").strip()

# Check if the file exists
if not os.path.exists(pdf_file_name):
    print("Error: File not found!")
    exit()

# Generate the output .txt file name
txt_file_name = pdf_file_name.replace(".pdf", ".txt")

# Open the PDF and extract text
with open(pdf_file_name, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    
    # Extract text from all pages
    extracted_text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

# Save extracted text into a .txt file
with open(txt_file_name, "w", encoding="utf-8") as txt_file:
    txt_file.write(extracted_text)

print(f"Text extracted and saved to {txt_file_name}")
