class Employee:
    
    # constructor
    def __init__(self, empID, empName, empSalary):
        self.empID = empID
        self.empName = empName
        self.empSalary = empSalary
        
    # getters
    def get_empID(self):
        return self.empID
    def get_empName(self):
        return self.empName
    def get_empSalary(self):
        return self.empSalary
    
    # setters
    def set_empID(self, empID):
        self.empID = empID
    def set_empName(self, empName):
        self.empName = empName
    def set_acctType(self, empSalary):
        self.empSalary = empSalary
        
    # calculate salary and level
    def salary(self):
        if self.empSalary <= 50000 :
            bonus = 5/100 * self.empSalary
            print('Level D, Bonus of 5%')
            print(round(bonus,2))
        elif 50000 < self.empSalary <= 70000 :
            bonus = 7/100 * self.empSalary
            print('Level C, Bonus of 7%')
            print(round(bonus,2))
        elif 70000 < self.empSalary <= 90000 :
            bonus = 9/100 * self.empSalary
            print('Level B, Bonus of 9%')
            print(round(bonus,2))
        elif self.empSalary > 90000 :
            bonus = 10/100 * self.empSalary
            print('Level A, Bonus of 10%')
            print(round(bonus,2))
            

# request input from customer
empID = input('Enter Emp ID: ')
empName = input('Enter Emp Name: ')
empSalary = float(input('Enter Emp Salary: '))


empInput = Employee(empID, empName, empSalary)

print('*' * 35)
print('EmpID: '+ empInput.get_empID())
print('EmpName: '+empInput.get_empName())
print('EmpSalary: ',empInput.get_empSalary())
empInput.salary()
            