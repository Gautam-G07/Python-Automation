from openpyxl import load_workbook, Workbook
wb=load_workbook(r"C:\Users\Gautam G\OneDrive\Desktop\students.xlsx")
sheet=wb.active
highest=-1
lowest=101
topstudent=""
bottomstudent=""    
total=0
count=0
new_wb=Workbook()
new_sheet=new_wb.active
for row in sheet.iter_rows(min_row=2,values_only=True):
    name,marks=row
    if name is None and marks is None:
        continue    
    if marks>highest:
        highest=marks
        topstudent=name
    if marks<lowest:
        lowest=marks
        bottomstudent=name
    total+=marks
    count+=1
    average=total/count
print(f"The highest marks are {highest} obtained by {topstudent}.") 
print(f"The lowest marks are {lowest} obtained by {bottomstudent}.")
print(f"The average marks of the students are {average:.2f}.")
print("Total students:", count)
