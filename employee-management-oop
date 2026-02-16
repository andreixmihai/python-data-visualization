class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"F25-{department}"
        Manager.mgr_count += 1

    def display_employee(self):
        print(f"Department: {self.department}")

if __name__ == "__main__":
    managers = [
        Manager("Manager1", 7000, "IT"),
        Manager("Manager2", 7500, "HR"),
        Manager("Manager3", 8000, "Finance"),
        Manager("Manager4", 8500, "Marketing")
    ]
    employees = [
        Employee("Employee1", 4000),
        Employee("Employee2", 4500)
    ]
    print("Manager Details:")
    for manager in managers:
        manager.display_employee()

    print("\nEmployee Details:")
    for employee in employees:
        employee.display_employee()

    print(f"\nTotal Employees: {employees[0].empCount}")
    print(f"Total Managers: {managers[0].mgr_count}")
