from PyPDF2 import PdfReader, PdfWriter
import os
file_path=r"C:\Users\Gautam G\Python\merged2.pdf"
reader=PdfReader(file_path)
output_folder=r"D:\C Splitter"
os.makedirs(output_folder, exist_ok=True)
for i,page in enumerate(reader.pages):
    splitter = PdfWriter() 
    splitter.add_page(page)
    output_path=os.path.join(output_folder,f"page_{i+1}.pdf")
    with open(output_path,'wb') as output_file:
        splitter.write(output_file)
print("PDF split into individual pages successfully.")
