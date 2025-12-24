print("---Python OOP Project: Employee Management System ---")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

     # protected use chid class call through to parent class
    def _display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")


class Employee(Person):
    def __init__(self,name,age,empid,salary):
        # chid class call through to parent class to key super key
        super().__init__(name,age)
        self.empid = empid
        self.salary = salary


    def get_employee_id(self):
        return self.empid
    
    def set_employee_id(self,empid):
        return self.empid == empid

    def display(self):
        super().display()
        print(f"Employee ID: {self.empid}")
        print(f"Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self,name,age,empid,salary,department):
        super().__init__(name,age,empid,salary)
        self.department = department


    def display(self):
        super().display()
        print(f"Department: {self.department}")

class developer(Employee):
    def __init__(self,name,age,empid,salary,department,Programming_language):
        super().__init__(name,age,empid,salary,department)
        self.programming_language = programming_language


    def display(self):
        super().display()
        print(f":programming language {self.programming_language}")

    
    person = None
    employee = None
    manager = None
    developer = None


    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")


        choice = input("Enter your choice: ")


        if choice == "1":
            name = input("Enter Name:")
            age = int(input("Enter Age:"))
            person = Person(name,age)
            print(f"person created with name:{name} and age:{age}")

        elif choice == "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            empid = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            employee = Employee(name, age, empid, salary)
            print(f"Employee Created with name:{name},age:{age},ID:{empid}, and salary:${salary}")
                  
        elif choice == "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            empid = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")
            manager = Manager(name, age, empid, salary, department)
            print(f"\nManager created with name: {name}, age: {age}, ID: {empid}, salary: ${salary}, and department: {department}.")

        elif choice == "4":
            print("Choose detalis show")
            print("1.Person")
            print("2.Employee")
            print("3.Manager")
            print("4.Developer")

            sub_choice = input("Enter your choice")

            if sub_choice == "1" and person:
                print("\nPerson Details:")
                person._display()

            
            elif sub_choice == "2" and Employee:
                print("\nEmployee Details:")
                employee.display()

                
            elif sub_choice == "3" and Manager:
                print("\nManager Details:")
                manager.display()

            elif sub_choice == "4" and developer:
                print("\ndeveloper Details:")
                developer.display()   

            else:
                print("\nNo data available or invalid choice.")

        elif choice == "5":
            print("Exiting the system. All resources have been freed")
            print("Good Bye")
            break

        else:
            print("\nInvalid choice. Please try again.")
