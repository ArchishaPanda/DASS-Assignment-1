import csv
from prettytable import PrettyTable
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
PINK = '\033[95m'
RESET = '\033[0m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RED = '\033[31m'

def add_entry(directory):
    new_entry = []
    new_entry.append(input("Enter First Name: "))
    new_entry.append(input("Enter Last Name: "))
    new_entry.append(input("Enter Roll Number: "))
    new_entry.append(input("Enter Course Name: "))
    new_entry.append(input("Enter Semester: "))
    new_entry.append(input("Enter Exam Type: "))
    new_entry.append(float(input("Enter Total Marks: ")))
    new_entry.append(float(input("Enter Scored Marks: ")))

    try:
        with open(directory,mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                new_entry_list = [str(element) for element in new_entry]
                if list(row.values()) == new_entry_list:
                    print(f"{GREEN}Same entry already exists in directory!{RESET}")
                    return
        with open(directory,mode='a') as file:    
            csv_writer = csv.writer(file)
            csv_writer.writerow(new_entry)        
            print(f"{GREEN}Entry added successfully!{RESET}")            
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def add_entry_csv(new_entry,directory):
    try:
        with open(directory,mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                new_entry_list = [str(element) for element in new_entry]
                if list(row.values()) == new_entry_list:
                    print(f"{GREEN}Same entry already exists in directory!")
                    return
            
        with open(directory,mode='a',newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(new_entry)        
        print(f"{GREEN}Entry added successfully!{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")


def load_from_file(file,directory):
    try:
        with open(file,mode='r') as source:
            csv_reader = csv.reader(source)
            next(csv_reader)
            for row in csv_reader:
                add_entry_csv(row,directory) 
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}") 


def display_directory(directory):
    try:
        with open(directory,mode='r') as file:
            csv_reader=csv.reader(file)
            header = next(csv_reader)
            table = PrettyTable(header)

            for row in csv_reader:
                table.add_row(row)
        if len(table._rows) == 0:
            print(f"{GREEN}No entries in the directory.{RESET}")
        else:
            print(f"{PINK}Marks Directory:{RESET}")
            print(table)
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def delete_entry(directory):
    try:
        rno = input("Enter the roll number whose record you wish to delete: ")
        rows_to_keep = []
        rows_with_req_roll_number = []

        with open(directory, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in  csv_reader:
                if row['Roll Number'] != rno:
                    rows_to_keep.append(row)
                else:
                    rows_with_req_roll_number.append(row)

        if len(rows_with_req_roll_number) == 0:
            print(f"{RED}No student with roll number",rno,f"exists in database!{RESET}")
            return

        print("Follwing are the entries corresponding to the roll number entered: ")
        for row in rows_with_req_roll_number:
            print(list(row.values()))

        choice = int(input("Please enter which record you wish to delete: "))
        if choice >= len(rows_with_req_roll_number) or choice <= 0:
            print(f"{RED}Wrong index entered")
            return
        
        rows_with_req_roll_number.pop(choice-1)        

        with open(directory, mode='w', newline='') as file:
            fieldnames = csv_reader.fieldnames
            csv_writer = csv.DictWriter(file, fieldnames)        
            csv_writer.writeheader()
            csv_writer.writerows(rows_to_keep)
            csv_writer.writerows(rows_with_req_roll_number)
        
        print(f"{GREEN}Record for student with roll number",rno,f"has been deleted successfully!{RESET}") 
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")  

def print_columns():
    print("1. First Name")
    print("2. Second Name")
    print("3. Roll Number")
    print("4. Course Name")
    print("5. Semester")
    print("6. Exam Type")
    print("7. Total Marks")
    print("8. Scored Marks")
    print("9. Return to Main Menu")

def update_entry(directory):
    try:
        rno = input("Enter roll number of student whose details you want to update: ")    
        rows = []
        rows_with_req_roll_number = []
        with open(directory,mode='r') as file:
            csv_reader = csv.DictReader(file)
            header = csv_reader.fieldnames
            table = PrettyTable(header)
            
            flag = 0
            print("The current data stored for student with roll number",rno,"is: ")
            for row in csv_reader:
                if row['Roll Number'] == rno:   
                    flag = 1
                    table.add_row(row.values())
                    rows_with_req_roll_number.append(row)
                else:
                    rows.append(row)
            
            if flag == 0:
                print(f"{RED}No such student found in directory{RESET}") 
                return
            
            print(table)

            entry = int(input("Enter which entry you want to update: "))
            while 1:
                print_columns()
                choice = int(input("Enter which column you want to update: "))
                if choice == 1:
                    fname = input(("Enter new first name: "))
                    rows_with_req_roll_number[entry-1]['First Name'] = fname
                elif choice == 2:
                    lname = input("Enter new last name: ")
                    rows_with_req_roll_number[entry-1]['Last Name'] = lname
                elif choice == 3:
                    roll = input("Enter new roll number")
                    rows_with_req_roll_number[entry-1]['Roll Number'] = roll
                elif choice == 4:
                    cname = input("Enter new course name: ")
                    rows_with_req_roll_number[entry-1]['Course Name'] = cname
                elif choice == 5:
                    sem = input("Enter new semester: ")
                    rows_with_req_roll_number[entry-1]['Semester'] = sem
                elif choice == 6:
                    exam = input("Enter new exam type: ")
                    rows_with_req_roll_number[entry-1]['Exam Type'] = exam
                elif choice == 7:
                    tmarks = float(input("Enter new total marks: "))
                    rows_with_req_roll_number[entry-1]['Total Marks'] = tmarks
                elif choice == 8:
                    smarks = float(input("Enter new scored marks: "))
                    rows_with_req_roll_number[entry-1]['Scored Marks'] = smarks
                elif choice == 9:
                    return
                else:
                    print("Invalid choice")
                c = input("Do you want to update any other columns? Enter y for yes and n for no: ")
                if(c == 'n'):
                    break
                elif c=='y':
                    continue
                else:
                    print("Invalid choice")  

            for r in rows_with_req_roll_number:
                rows.append(r)        

            with open(directory, mode='w', newline='') as file:
                fieldnames = csv_reader.fieldnames
                csv_writer = csv.DictWriter(file, fieldnames)        
                csv_writer.writeheader()
                csv_writer.writerows(rows)                                 
            
            print(f"{GREEN}Student record updated successfully{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

    
def search(directory):
    try:
        flag = 0
        with open(directory, mode='r') as file:
            csv_reader = csv.DictReader(file)
            header = csv_reader.fieldnames
            table = PrettyTable(header)

            print_columns()
            choice = int(input("Enter the column based on what you want to search: "))
            if choice == 1:
                fname = input("Enter first name: ")
                for row in csv_reader:
                    if row['First Name'] == fname:
                        flag = 1
                        table.add_row(row.values())
            elif choice == 2:
                lname = input("Enter last name: ")
                for row in csv_reader:
                    if row['Last Name'] == lname:
                        flag = 1
                        table.add_row(row.values())
            elif choice == 3:
                rno = input("Enter roll number: ")
                for row in csv_reader:
                    if row['Roll Number'] == rno:
                        flag = 1
                        table.add_row(row.values())
            elif choice == 4:
                cname = input("Enter course name: ")
                for row in csv_reader:
                    if row['Course Name'] == cname:
                        flag = 1
                        table.add_row(row.values())
            elif choice == 5:
                sem = input("Enter semester: ")
                for row in csv_reader:
                    if row['Semester'] == sem:
                        flag = 1
                        table.add_row(row.values())
            elif choice == 6:
                exam = input("Enter exam type: ")
                for row in csv_reader:
                    if row['Exam Type'] == exam:
                        flag = 1
                        table.add_row(row.values())
            elif choice == 7:
                tm = input("Enter total marks: ")
                for row in csv_reader:
                    if row['Total Marks'] == tm:
                        flag = 1
                        table.add_row(row.values())
            elif choice == 8:
                sm = input("Enter scored marks: ")
                for row in csv_reader:
                    if row['Scored Marks'] == sm:
                        flag = 1
                        table.add_row(row.values())
            else:
                print("Invalid Input")
        if flag == 0:
            print(f"{RED}No such entry exists!")
            return
        print(table)
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def print_menu():
    print(f"{PINK}Marks Directory Management Menu: {RESET}")
    print(f"{YELLOW}1. Add a new entry{RESET}")
    print(f"{YELLOW}2. Add records from another file{RESET}")
    print(f"{YELLOW}3. Display directory{RESET}")
    print(f"{YELLOW}4. Delete an entry{RESET}")
    print(f"{YELLOW}5. Update an entry{RESET}")
    print(f"{YELLOW}6. Search for an entry{RESET}")
    print(f"{YELLOW}7. Exit{RESET}")

directory = input("Enter name of csv file to store the directory: ")
with open(directory, mode='w', newline='') as new_file:
    fieldnames = ['First Name','Last Name','Roll Number','Course Name','Semester','Exam Type','Total Marks','Scored Marks']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    
while(1):    
    print_menu()
    choice = int(input(f"{BLUE}Enter your choice: {RESET}"))
    if choice == 1:
        add_entry(directory)
    elif choice == 2:
        source_file = input("Enter file name: ")
        load_from_file(source_file,directory)
    elif choice == 3:
        display_directory(directory)
    elif choice == 4:
        delete_entry(directory)
    elif choice == 5:
        update_entry(directory)
    elif choice == 6:
        search(directory)
    elif choice == 7:
        print(f"{RED}Exiting Marks Directory Management.{RESET}")
        break
    else:
        print(f"{RED}Invalid choice. Please enter a valid option.\n{RESET}")