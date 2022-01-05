"""
Schedule generator.
Given employees, their schedule, and time frame needed to be covered, returns a schedule that satisfies the employees availabilities.
"""
from employee import Employee
from employee_list import Employee_List

def create_employee_list():
    #create employee list
    employee_list = Employee_List()

    #obtain the number of employees to be added
    number_of_employees = int(input("How many employees would you like to add? "))

    #for loop that adds employees to the employee list
    for i in range(number_of_employees):
        print("Please enter employee number ", i + 1, "'s first name.")
        first_name = input()
        print("Please enter employee number ", i + 1, "'s last name.")
        last_name = input()
        print("Please enter employee number ", i + 1, "'s availability start time.")
        avail_start_time = int(input())
        print("Please enter employee number ", i + 1, "'s availability end time.")
        avail_end_time = int(input())

        employee = Employee(first_name, last_name,avail_start_time,avail_end_time)

        employee_list.add_employee(employee)
    
    print("Here are the employees that you added.")

    employee_list.print_employees()

    return employee_list

def generate_schedule(employee_list, work_day_start, work_day_end):
    
    coverage_at_opening = False
    coverage_at_close = False
    for employee in employee_list:
        if employee.get_avail_start() <= work_day_start:
            coverage_at_opening = True

        if employee.get_avail_end() >= work_day_end:
            coverage_at_close = True

    if not(coverage_at_opening) or not(coverage_at_close):
        print("You do not have any employees to cover either opening or close.")


        







#function executed when user decided to create a schedule
def run():
    #obtaining the start time and end time of work day
    work_day_start_time = int(input("Please enter the beginning of the work day in military time. (0000 - 2400) "))
    work_day_end_time = int(input("Please enter the end of the work day in military time. (0000-2400) "))

    #function that creates employee list
    employee_list = create_employee_list()

    #function that contains algorithm to generate a schedule
    generate_schedule(employee_list, work_day_start_time, work_day_end_time)


    


    






#capture whether user wants to generate a schedule or not
choice = input("Would you like to generate a schedule?(y/n) ")

#lower case input for input validation
choice = choice.lower()

if choice == "y":
    print("Let's generate a schedule!")
    run()
elif choice == "n":
    print("Program is now exiting.")
else:
    print("Invalid Input. Program is now exiting.")

