from PyPDF2 import PdfMerger
import os
folder_path = r"C:\Users\Gautam G\Downloads"
files=os.listdir(folder_path)
merger=PdfMerger()
pdf_files=[]
for file in files:
    if file.endswith(".pdf"):
        pdf_files.append(file)
pdf_files.sort()
file1=input("Enter name of first pdf u want to merge:")
file2=input("Enter name of second pdf u want to merge:")
for file in pdf_files:
    if file1 in file:
        merger.append(os.path.join(folder_path,file))
    if file2 in file:
        merger.append(os.path.join(folder_path,file))
merger.write("merged2.pdf")
merger.close()
print("PDFs merged successfully!")