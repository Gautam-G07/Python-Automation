from PyPDF2 import PdfReader, PdfWriter
import os
file_name=input("Enter the name of the PDF file (with extension): ")
file_path=os.path.join(r"D:\C Splitter", file_name)
reader=PdfReader(file_path)
output_folder=r"D:\C Splitter"
os.makedirs(output_folder, exist_ok=True)
for i,page in enumerate(reader.pages):
    splitter = PdfWriter() 
    splitter.add_page(page)
    output_path=os.path.join(output_folder,f"{file_name}_page_{i+1}.pdf")
    with open(output_path,'wb') as output_file:
        splitter.write(output_file)
print("PDF split into individual pages successfully.")
