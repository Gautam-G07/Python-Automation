from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os
folderpath=r"C:\Users\Gautam G\Downloads"
files=os.listdir(folderpath)
def mergepdf():
    file1=input("Enter name of 1st pdf u want to merge:")
    file2=input("Enter name of 2nd pdf u want to merge:")
    path1=os.path.join(folderpath,file1)
    path2=os.path.join(folderpath,file2)

    merger=PdfMerger()  
    if not os.path.isfile(path1):  
        print(f"File '{file1}' not found in the folder.")
        return
    if not os.path.isfile(path2):  
        print(f"File '{file2}' not found in the folder.")
        return  
    merger.append(path1)
    merger.append(path2)
    output_path=os.path.join(folderpath,"merged.pdf")
    merger.write(output_path)
    merger.close()  
    print("PDFs merged successfully!")
def splitpdf(): 
    file_name=input("Enter the name of the PDF file (with extension): ")
    file_path=os.path.join(folderpath, file_name)
    if not os.path.isfile(file_path):
        print(f"File '{file_name}' not found in the folder.")
        return
    reader=PdfReader(file_path)
    output_folder=os.path.join(folderpath, "split_pages")
    os.makedirs(output_folder, exist_ok=True)
    for i,page in enumerate(reader.pages):
        splitter = PdfWriter() 
        splitter.add_page(page)
        output_path=os.path.join(output_folder,f"{file_name}_page_{i+1}.pdf")
        with open(output_path,'wb') as output_file:
            splitter.write(output_file)
    print("PDF split into individual pages successfully.")  
while True:
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Exit")
    choice=input("Enter your choice (1/2/3): ")
    if choice=="1":
        mergepdf()
    elif choice=="2":
        splitpdf()
    elif choice=="3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
