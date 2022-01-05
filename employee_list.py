from employee import Employee

class Employee_List:
    def __init__(self):
        self.list = []

    def add_employee(self, employee):
        self.list.append(employee)

    def remove_employee(self, employee):
        self.list.remove(employee)
    
    def print_employees(self):
        
        for employee in self.list:
            print(employee.get_first_name(), employee.get_last_name())
            print("Available from ", employee.get_avail_start(), "to ", employee.get_avail_end())
            print()
            