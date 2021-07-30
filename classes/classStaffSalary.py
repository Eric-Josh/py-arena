# Virtuoso Software Consultancy
# Staff Member Salary Calculation Based on Hourly Rate
# level1:hourly rate = 18
# level2:hourly rate = 25
# level3:hourly rate = 50
# level4:hourly rate = 100

class Staff:
	
	#constructor
	def __init__(self, staffId, staffName,  staffLevel, staffWorkHour ):
		self.staffId =staffId
		self.staffName = staffName
		self.staffLevel = staffLevel
		self.staffWorkHour = staffWorkHour
		
	#getters
	def get_staffId(self):
		return self.staffId
		
	def get_staffName(self):
		return self.staffName
		
	def get_staffLevel(self):
		return self.staffLevel
		
	def get_staffWorkHour(self):
		return self.staffWorkHour
		
	#setters
	def set_staffId(self, staffId):
		self.staffId = staffId
		
	def set_staffName(self, staffName):
		self.staffName = staffName
		
	def set_staffLevel(self, staffLevel):
		self.staffLevel = staffLevel
		
	def set_staffWorkHour(staff, staffWorkHour):
		self.staffWorkHour = staffWorkHour
	
	#methods
	def staffSalary(self):
		if self.staffLevel == 1 :
			sal = self.staffWorkHour * 18
			print("Staff Salary: ", sal)
		elif self.staffLevel == 2 :
			sal = self.staffWorkHour * 25
			print("Staff Salary: ", sal)
		elif self.staffLevel == 3 :
			sal = self.staffWorkHour * 50
			print("Staff Salary: ", sal)
		elif self.staffLevel == 4 :
			sal = self.staffWorkHour * 100
			print("Staff Salary:",sal)
	

staffId = input(("Enter Staff ID: "))
staffName = input(("Enter Name: "))

while True:
   staffLevel = int(input(("Enter Level within 1 and 4: ")))
   if staffLevel in range(1,5):
        break
   print('Please try again')

staffWorkHour = int(input(("Enter No. of hours worked: ")))

		
x = Staff(staffId, staffName, staffLevel, staffWorkHour)


print("=" * 30)
print("Staff ID: " + x.get_staffId())
print("Staff Name: " + x.get_staffName())
print("Staff Level: ", x.get_staffLevel())
print("Staff No. of hours worked: ", x.get_staffWorkHour())
x.staffSalary()
	