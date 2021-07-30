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
        
        # calculate grade and salary based on bonus
    def salary(self):
        if self.empSalary <= 40000 :
            salary = (4/100 * self.empSalary) + self.empSalary
            print('Grade G1, Bonus of 4%')
            print('Salary: ',round(salary,2))
        elif 40000 < self.empSalary <= 60000 :
            salary = (6/100 * self.empSalary) + self.empSalary
            print('Grade G2, Bonus of 6%')
            print('Salary: ',round(salary,2))
        elif 60000 < self.empSalary <= 80000 :
            salary = (8/100 * self.empSalary) + self.empSalary
            print('Grade G3, Bonus of 8%')
            print('Salary: ',round(salary,2))
        elif self.empSalary > 80000 :
            salary = 10/100 * self.empSalary
            print('Grade G4, Bonus of 10%')
            print('Salary: ',round(salary,2))
            
    
def displayInformation():
    empID = input('Enter Emp ID: ')
    empName = input('Enter Emp Name: ')
    empSalary = float(input('Enter Emp Salary: '))


    empDetails = Employee(empID, empName, empSalary)

    print('#' * 35)
    print('EmpID: '+ empDetails.get_empID())
    print('EmpName: '+empDetails.get_empName())
    print('EmpSalary: ',empDetails.get_empSalary())
    empDetails.salary()

    
displayInformation()    