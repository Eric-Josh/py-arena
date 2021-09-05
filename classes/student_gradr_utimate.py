class Menus:
    
    def main_menu(self):
        print('Choose one of the following options:')
        print('1 - Enter student grade information')
        print('2 - Print all student grade information')
        print('3 - Print class performance statistics')
        print('4 - Exit')
        
    def menu_one_list(self):
        print('Choose one of the following options:')
        print('1.1 - Enter a BIT student information')
        print('1.2 - Enter a DIT student information')
        print('1.3 - Go back to the main menu')
        
    def menu_two_list(self):
        print('Choose one of the following options:')
        print('2.1 – Print all student grade information ascendingly by final mark')
        print('2.2 – Print all student grade information descendingly by final mark')
        print('2.3 – Go back to the main menu')
        
        
class Validations:
    
    def main_menu(self, choice):
        opts = ('1','2','3','4')
        while True:
            if choice in opts:
                break
            print('Invalid option, please try again!')
            choice = input('Choose an option: ')
        return choice
    
    def menu_one(self, choice):
        opts = ('1.1','1.2','1.3')
        while True:
            if choice in opts:
                break
            print('Invalid option, please try again!')
            choice = input('Choose an option: ')
        return choice
    
    def menu_two(self, choice):
        opts = ('2.1','2.2','2.3')
        while True:
            if choice in opts:
                break
            print('Invalid option, please try again!')
            choice = input('Choose an option: ')
        return choice


class Student_Records:
    
    def __init__(self, stdId, stdName, group, marks):
        self.stdId = stdId
        self.stdName = stdName
        self.group = group
        self.marks = marks


class DIT_Gradr(Student_Records):
            
    def gradr(self):
        marks=self.marks.split(',')
        mark1 = float(marks[0])
        mark2 = float(marks[1])
        mark3 = float(marks[2])
        finalMark = round(mark1 * 20/100 + mark2 * 40/100 + mark3 * 40/100)
        
        grade=None
        gpv=0
        # Interim grade use case conditions
        if 50 <= finalMark <= 100:
            grade = 'CP'
            gpv=4.0
        else:
            remarks = input('What is this student’s resubmission marks (separated by comma):')
            remarks=remarks.split(',')
            mark1 = float(remarks[0])
            mark2 = float(remarks[1])
            mark3 = float(remarks[2])
            finalMark = round(mark1 * 20/100 + mark2 * 40/100 + mark3 * 40/100)
            if finalMark >= 50:
                grade = 'CP'
            else:
                grade = 'NC'
                
        return finalMark, grade, gpv, mark1, mark2, mark3
    
    
class BIT_Gradr(Student_Records):
    
    def gradr(self):
        marks=self.marks.split(',')
        mark1 = float(marks[0])
        mark2 = float(marks[1])
        mark3 = float(marks[2])
        finalMark = round(mark1 * 20/100 + mark2 * 40/100 + mark3 * 40/100)
        
        # Add mark1-3 to a list
        list = [mark1, mark2, mark3]
        lowMarkCheck = 0

        for i in list:
            if i < 50:
                lowMarkCheck += 1
                
        grade=None
        gpv=0
        # Interim grade use case conditions
        if list.count(0) >= 2 and finalMark <= 44:
            grade='F'
        elif list.count(0) == 1 and finalMark <= 44:
            grade='F'
        elif list.count(0) == 1 and 45 < finalMark < 49:
            grade='F'
        elif lowMarkCheck == 2 and 45 < finalMark < 49:
            grade='F'
        elif mark3 < 50 and 45 < finalMark < 49:
            SupExam = float(input('What is this student\'s supplementary exam mark: '))
            if round(SupExam) >= 50:
                finalMark = round(SupExam)
                grade='SP'
                gpv=0.5
            else:
                grade='F'
        elif mark1 < 50 or mark2 < 50 and 45 < finalMark < 49:
            supMark = float(input('What is this student\'s supplementary assessment mark: '))
            if round(supMark) >= 50:
                finalMark = round(supMark)
                grade='SP'
                gpv=0.5
            else:
                grade='F'
        elif 50 < finalMark < 64:
            grade='P'
            gpv=1.0
        elif 65 < finalMark < 74:
            grade='C'
            gpv=2.0
        elif 75 < finalMark < 84:
            grade='D'
            gpv=3.0
        elif 85 < finalMark < 100:
            grade='HD'
            gpv=4.0
        
        return finalMark, grade, gpv, mark1, mark2, mark3


class Student_Data_Host:
    
    host=[]
    
    def student(self, Student_Records):
        host.append(Student_Records)
        
    def display_record_desc(self):  
        for i in range(len(self.host)):
            for j in range(i+1,len(self.host)):
                if self.host[i].grade[0] < self.host[j].grade[0]:
                    tmp=self.host[i]
                    self.host[i]=self.host[j]
                    self.host[j]=tmp
            
        print('='*50)
        for strs in self.host:
            print(strs.stdId,end='\t')
            print(strs.stdName,end='\t')
            print(strs.group,end='\t')
            print(strs.grade[0],end='\t')
            print(strs.grade[1])
        
    def display_record_asc(self):
        for i in range(len(self.host)):
            for j in range(i+1,len(self.host)):
                if self.host[i].grade[0] > self.host[j].grade[0]:
                    tmp=self.host[i]
                    self.host[i]=self.host[j]
                    self.host[j]=tmp
                    
        print('='*50)
        for strs in self.host:
            print(strs.stdId,end='\t')
            print(strs.stdName,end='\t')
            print(strs.group,end='\t')
            print(strs.grade[0],end='\t')
            print(strs.grade[1])
            
    def display_performance_stat(self):
        assessmentMark1=0
        assessmentMark2=0
        assessmentMark3=0
        finalMark=0
        gradeCount=[]
        group=[]
        gpv=[]
        
        for strs in self.host:
            assessmentMark1 += strs.grade[3]
            assessmentMark2 += strs.grade[4]
            assessmentMark3 += strs.grade[5]
            finalMark += strs.grade[0]
            gradeCount.append(strs.grade[1])
            group.append(strs.group)
            gpv.append(strs.grade[2])
        
        # perform analysis
        noStudents = len(self.host)
        noBITStudents = group.count('BIT')
        noDITStudents = group.count('DIT')
        studentPassRate = ((gradeCount.count('HD') + gradeCount.count('D') + gradeCount.count('C')
                             + gradeCount.count('P') + gradeCount.count('SP') + gradeCount.count('SP'))
                             * 100 / noStudents)
        studentPassRateAdj = ((gradeCount.count('HD') + gradeCount.count('D') + gradeCount.count('C')
                             + gradeCount.count('P') + gradeCount.count('SP') + gradeCount.count('SP'))
                             * 100 / noStudents - gradeCount.count('AF'))
        avgMarkAssessment1 = assessmentMark1/noStudents
        avgMarkAssessment2 = assessmentMark2/noStudents
        avgMarkAssessment3 = assessmentMark3/noStudents
        avgFinalMark = finalMark/noStudents
        avgGradePoint = sum(gpv)/noStudents
        
        print('='*50)
        print('Number of students:',noStudents)
        print('Number of BIT students:',noBITStudents)
        print('Number of DIT students:',noDITStudents)
        print('Student pass rate:',round(studentPassRate, 2),'%')
        print('Student pass rate (adjusted):',round(studentPassRateAdj, 2),'%')
        print('Average mark for Assessment 1:',round(avgMarkAssessment1, 2))
        print('Average mark for Assessment 2:',round(avgMarkAssessment2, 2))
        print('Average mark for Assessment 3:',round(avgMarkAssessment3, 2))
        print('Average final mark:',round(avgFinalMark, 2))
        print('Average grade point:',round(avgGradePoint, 1))
        print('Number of HDs:',gradeCount.count('HD'))
        print('Number of Ds:',gradeCount.count('D'))
        print('Number of Cs:',gradeCount.count('C'))
        print('Number of Ps:',gradeCount.count('P'))
        print('Number of SPs:',gradeCount.count('SP'))
        print('Number of CPs:',gradeCount.count('CP'))
        print('Number of Fs:',gradeCount.count('F'))
        
        
class Student_Manager:
    
    dataHost = Student_Data_Host()
    
    def student_record_collection(self):
        while True:
            menuList = Menus()
            menuList.main_menu()
            choice = input('')
            validate = Validations().main_menu(choice)
            
            if validate == '1':
                while True:
                    menuList.menu_one_list()
                    choice = input('')
                    validate = Validations().menu_one(choice)
                                            
                    if validate == '1.1':
                        stdId = input('Enter student ID: ')
                        stdName = input('Enter student name: ')
                        marks = input('Enter student assessment marks (separated by comma): ')
                        group = 'BIT'
                        bitStudent = BIT_Gradr(stdId, stdName, group, marks)
                        bitStudent.grade = bitStudent.gradr()
                        self.dataHost.host.append(bitStudent)
                    
                    if validate == '1.2':
                        stdId = input('Enter student ID: ')
                        stdName = input('Enter student name: ')
                        marks = input('Enter student assessment marks (separated by comma): ')
                        group = 'DIT'
                        ditStudent = DIT_Gradr(stdId, stdName, group, marks)
                        ditStudent.grade = ditStudent.gradr()
                        self.dataHost.host.append(ditStudent)
                        
                    if validate == '1.3':
                        break
                        
            if validate == '2':
                while True:
                    menuList.menu_two_list()
                    choice = input('')
                    validate = Validations().menu_two(choice) 
                    
                    if validate == '2.1':
                        self.dataHost.display_record_asc()
                        
                    if validate == '2.2':
                        self.dataHost.display_record_desc()
                        
                    if validate == '2.3':
                        break
            
            if validate == '3':
                self.dataHost.display_performance_stat()
                
            if validate == '4':
                print('You have exited!')
                break
                
                
st = Student_Manager()
st.student_record_collection()