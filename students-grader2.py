# Determine Interim Grade Letter.
# The program allows the Subject Coordinator to type in multiple student’s 3 assessment marks separated by a comma.
# This was based on some business rules.

studentMarkList=[]
gradePointList=[]
gradesList=[]
cumStudentsMark1=0
cumStudentsMark2=0
cumStudentsMark3=0
cumStudentsFinalMark=0

while True:
    marksInput = input('Enter a student\'s assessment marks (separated by comma): ')
    studentMarkList.append(marksInput)
    
    if marksInput != 'N':
    
        studentMarks=marksInput.split(',')
        
        mark1 = float(studentMarks[0])
        mark2 = float(studentMarks[1])
        mark3 = float(studentMarks[2])
        finalMark = round(mark1 * 20/100 + mark2 * 40/100 + mark3 * 40/100)

        # Add mark1-3 to a list
        list = [mark1, mark2, mark3]
        lowMarkCheck = 0
        
        for i in list:
            if i < 50:
                lowMarkCheck += 1
                
        # Interim grade use case conditions
        if list.count(0) >= 2 and finalMark <= 44:
            gradesList.extend('F','AF')
        elif list.count(0) == 1 and finalMark <= 44:
            gradesList.extend('F')
        elif list.count(0) == 1 and 45 < finalMark < 49:
            gradesList.extend('F')
        elif lowMarkCheck == 2 and 45 < finalMark < 49:
            gradesList.extend('F')
        elif mark3 < 50 and 45 < finalMark < 49:
            SupExam = float(input('What is this student\'s supplementary exam mark: '))
            if round(SupExam) >= 50 :
                gradesList.extend('SP')
                gradePointList.append(0.5)
            else:
                gradesList.extend('F')
        elif mark1 < 50 or mark2 < 50 and 45 < finalMark < 49:
            supMark = float(input('What is this student\'s supplementary assessment mark: '))
            if round(supMark) >= 50 :
                gradesList.extend('SP')
                gradePointList.append(0.5)
            else:
                gradesList.extend('F')
        elif 50 < finalMark < 64:
            gradesList.extend('P')
            gradePointList.append(1.0)
        elif 65 < finalMark < 74:
            gradesList.extend('C')
            gradePointList.append(2.0)
        elif 75 < finalMark < 84:
            gradesList.extend('D')
            gradePointList.append(3.0)
        elif 85 < finalMark < 100:
            gradesList.extend('HD')
            gradePointList.append(4.0)
            
        cumStudentsMark1 += mark1
        cumStudentsMark2 += mark2
        cumStudentsMark3 += mark3
        cumStudentsFinalMark += finalMark
            
    if marksInput == 'N':
        break
    else:
        continue
            

noOfStudent = len(studentMarkList)-1
passRate = (gradesList.count('HD') + gradesList.count('D') 
            + gradesList.count('C') + gradesList.count('P') 
            + gradesList.count('SP'))*100/noOfStudent 
adjRate = ((gradesList.count('HD') + gradesList.count('D') + gradesList.count('C') 
            +gradesList.count('P') + gradesList.count('SP'))*100/noOfStudent 
            - gradesList.count('AF'))
avgMark1 = cumStudentsMark1 / noOfStudent
avgMark2 = cumStudentsMark2 / noOfStudent
avgMark3 = cumStudentsMark3 / noOfStudent
avgFinalMark = cumStudentsFinalMark / noOfStudent
avgGradeScore = sum(gradePointList) / noOfStudent

print('Number of students:',noOfStudent)
print('Student pass rate:',round(passRate,2),'%')
print('Student pass rate (adjusted):',round(adjRate,2),'%')
print('Average mark for Assessment 1:',round(avgMark1,2))
print('Average mark for Assessment 2:',round(avgMark2,2))
print('Average mark for Assessment 3:',round(avgMark3,2))
print('Average final mark:',round(avgFinalMark,2))
print('Average grade point:',round(avgGradeScore,1))
print('Number of HDs:',gradesList.count('HD'))
print('Number of Ds:',gradesList.count('D'))
print('Number of Cs:',gradesList.count('C'))
print('Number of Ps:',gradesList.count('P'))
print('Number of SPs:',gradesList.count('SP'))
print('Number of Fs:',gradesList.count('F'))
