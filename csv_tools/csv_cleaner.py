import csv
clean_data=[]
with open(r"C:\\Users\\Gautam G\\Python\\day12\\student.csv", "r") as file:
    reader = csv.reader(file)
    next(reader,None) 
    for row in reader:
        name,marks=row
        name=name.strip()
        try:
            marks=int(marks.strip())
        except ValueError:
            continue
        if name=="":
            continue
        clean_data.append([name, marks])
highest=-1
name1=""    
for name, marks in clean_data:
    if marks>highest:
        highest=marks
        name1=name
print(f"The highest marks are {highest} obtained by {name1}.")
with open("clean_students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerows(clean_data)
print("Clean CSV FILE CREATED!")
