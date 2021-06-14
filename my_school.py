from datetime import date, datetime
import copy
import sys
###################################################################################################################################################
#Class School
###################################################################################################################################################

# initizing the school class
class School:
      
    #instance variables 
    def __init__(self):

        self.student_id = []
        self.course_id = []
        self.student_data = []
        
        
    #method to read scores.txt
    def read_scores(self, file_name):
        
        #function def: used to convet str to float
        def isfloat(x):

            try:
                a = float(x)

            except (TypeError, ValueError):
                return False
            else:
                return True
        #function def: used to convert str to int
        def to_int(x):
            print('abc')
            y = int(x)
            return(y)

        #file opening and reading the file and handling the errors
        try:
            student = []
            student_scores = open(file_name,"r")
            line = student_scores.readline()
            while(line != ""):
                line = line.strip().split(" ")
                line = [x.strip()for x in line]
                student.append(line)
                line = student_scores.readline()
            student_scores.close()

            index = [int(index) for index in student[0][0]]

            #validating the number of subjects given in [0][0] vs actual given in file
            try:
                
                if index[0]+1 == len(student):
                    for j in student:
                        try:
                            if index[1]+1 == len(j):
                               self.student_data.append(j)
                            else:
                                raise Exception("scoreError")
                        except Exception:
                            print("Student has data for '"+ str(len(j)-1) + "' subjects but expected to have data for '" + str(index[0])+"'")
                            exit()
                else:
                    raise Exception("studentError")

            except Exception:
                print("Number of student related data in file are '"+ str(len(student)-1) + "' but expected to have data for '" + str(index[0])+"'")
                exit()

            #validating the scores and raises exception id there are any errors in data 
            for i in range(1,len(self.student_data)):
                for j in range(1,len(self.student_data[i])): 
                    try:

                        
                        if (self.student_data[i][j]).isnumeric() :
                            

                            if ( int(self.student_data[i][j]) <= 100 and int(self.student_data[i][j]) >= -1):

                                self.student_data[i][j] = str(self.student_data[i][j])    

                        elif(isfloat(self.student_data[i][j])):
                                
                                
                                abc = to_int(self.student_data[i][j])
                                print(abc)
                                
                                if ( abc <= 100 and abc >= -1):
                                    
                                    print( self.student_data[i][j])
                                    self.student_data[i][j] = str(abc)       

                        elif (self.student_data[i][j] == "TBA") or (self.student_data[i][j] == "888") :
                            self.student_data[i][j] = '888'
                        
                        elif (self.student_data[i][j]) == str:

                            self.student_data[i][j] = '-1'
                        
                        else:
                            
                            self.student_data[i][j] = '-1'
                                
                    except Exception:

                        print("wrong value provided in scores")
                        exit()
                    
            #Validates the course ID given all the course Id needs to start with 'C'
            for i in self.student_data[0][1:]:
                try:
                    if i[0].lower() == 'c':
                        pass
                    else:
                        self.student_data =[]
                        raise Exception("wrong course ID")
                except Exception:

                    print("wrong course ID")
                    exit()
            #Validates the course ID given all the course Id needs to start with 'S'
            for i in self.student_data[1:]:
                for j in i[0][0]: 
                    try:
                        
                        if (j[0] == 'S'):
                            pass
                        else:
                            self.student_data = []
                            raise Exception("wrong Student ID")
                            
                    except Exception:

                        print("wrong Student ID")
                        exit()


        except:
            print("Invalid File, Quitting program")


    #Setting the student list 
    def set_student_id(self):

        for i in self.student_data[1:]:
            
            self.student_id.append(i[0])

    #getting the student list
    def get_student_id(self):
        return self.student_id

    #Setting the Course id
    def set_course_id(self):

        self.course_id = self.student_data[0][1:]
    
    #getting the course ID
    def get_course_id(self):
        return self.course_id



###################################################################################################################################################
#Class course
###################################################################################################################################################

# initizing the course class

class Course(School):
    #instance variables
    def __init__(self) :
        super().__init__()
        self.course_list = []
        #private variable can be used only in this class
        self.__course_student_data = []

    #setting the student data fetched from schoolclass
    def set_student_data_to_course(self):

        self.__course_student_data = copy.deepcopy(self.student_data)
        return self.__course_student_data

    #reading the course.txt file
    def read_courses(self,file_name):
        course_data = open(file_name,"r")
        line = course_data.readline()
        while(line != ""):
            line = line.strip().split(" ")
            line = [x.strip()for x in line]
            self.course_list.append(line)
            line = course_data.readline()
        course_data.close()
        return self.course_list
    
    #Gets the course summary and also prints the file
    def get_course_average(self):

    
        for n in range(len(self.course_list)):
            
            m = self.course_list[n][0]
            j = self.__course_student_data[0].index(m)
            enl = 0
            k = 0
            average = 0

            #finding the average of each course by seperating actual marks and not enrolled and result expected soon 
            for i in range(1,len(self.__course_student_data)):

                if (int(self.__course_student_data[i][j] ) >=0 and int(self.__course_student_data[i][j] ) <=100):
                    average += int(self.__course_student_data[i][j])
                    k+=1
                    enl+=1
                elif (int(self.__course_student_data[i][j]) == 888) or (self.__course_student_data[i][j] == 'TBA'):   
                    enl+=1

            if k != 0:    
                average = str(round(average/k,2))
            else:
                average = str('--')
            self.course_list[n].append(str(enl))
            self.course_list[n].append(average)

       
       #adding * and - to respected coures by seperating the course into compullsary and electives
        for i in range(len(self.course_list)):

            if (self.course_list[i][2] == 'C1') or (self.course_list[i][2] == 'C2') or (self.course_list[i][2] == 'C3'):
                self.course_list[i][1] = ('* '+ self.course_list[i][1])
            elif (self.course_list[i][2]) == 'E':
        
                self.course_list[i][1] = ('- '+ self.course_list[i][1])
        #Generating  the course report and course report file
        time = datetime.now()
        date_and_time_1 = time.strftime("%d/%m/%Y %H:%M")
        try:
            src = open("courses_report.txt","r+")
            b = src.read()

        except:
            pass
        print('\n')
        file = open("courses_report.txt","w+")
        file.write('\n')
        file.write(" ")
        file.write('\n')
        file.write("Report Generated on : ")
        file.write(date_and_time_1)
        file.write('\n')
        print(f"{'CID':8s}{'Name':13s}{'Pt.':4s}{'Enl.':5s}{'Avg'}")
        file.write(f"{'CID':8s}{'Name':13s}{'Pt.':4s}{'Enl.':5s}{'Avg'}")
        file.write('\n')
        print('-'*34,end='')
        file.write('-'*34)
        file.write('\n')
        print()
        
        
        for i in range(len(self.course_list)):
            

            print(f"{self.course_list[i][0]:6s}{self.course_list[i][1]:15s}{self.course_list[i][3]:4s}{self.course_list[i][4]:5s}{self.course_list[i][5]}")
            file.write(f"{self.course_list[i][0]:6s}{self.course_list[i][1]:15s}{self.course_list[i][3]:4s}{self.course_list[i][4]:5s}{self.course_list[i][5]}\n")

        print('-'*34+'\n')
        file.write('-'*34+'\n')
        
       

        hieghest_avg =[]
        for i in range(len(self.course_list)):
            hieghest_avg.append(self.course_list[i][-1])
        hieghest_avg_index = hieghest_avg.index(min(hieghest_avg))

        print("The worse performing course is "+ self.course_list[hieghest_avg_index][0] + " with an average "+self.course_list[hieghest_avg_index][-1])
        file.write("The worse performing course is "+ self.course_list[hieghest_avg_index][0] + " with an average "+self.course_list[hieghest_avg_index][-1])
        file.close

        try:
            file = open("courses_report.txt","a+")
            file.write(b)
            file.close()
        except:
            pass
        print('\ncourses_report.txt generated!')
    
    #Methods to change the course title
    def modify_course_title():
        pass
    #methods to change the course points
    def modify_course_points():
        pass
        
        

###################################################################################################################################################
#Class Student
###################################################################################################################################################
       
# initizing the Student class
class Student(Course):
    #initilizing the instance variables
    def __init__(self) :
        super().__init__()
        self.student_data_copy = []
        self.students = []
    #setting the student realated dat fetched from school class
    def set_student_data_copy_to_student(self):
        self.student_data_copy = copy.deepcopy(self.student_data)
        return self.student_data_copy

    #setting the course realated data fetched from course class
    def set_course_data_copy(self):
        self.course_data_copy = copy.deepcopy(self.course_list)

    #getting the filnal result
    def get_result(self):
 
        for i in range(1,len(self.student_data_copy)):
            k = 0
            average = 0
            
            for j in range(1,len(self.student_data_copy[i])):
                
                if (int(self.student_data_copy[i][j]) >= 0 and int(self.student_data_copy[i][j]) <= 100):
                    average += int(self.student_data_copy[i][j])
                    k+=1

                elif (int(self.student_data_copy[i][j]) == -1): 
                    self.student_data_copy[i][j] = " " 
                elif (int(self.student_data_copy[i][j]) == 888 or self.student_data_copy[i][j]== 'TBA') :   
                    self.student_data_copy[i][j] = "--"
            
            if k != 0:
                average_cal = round(average/k,2)
                average_cal = str(average_cal)
            else:
                average_cal = str(0)
            self.student_data_copy[i].append(average_cal)

        print('\n')

        self.student_data_copy[0][0] = "     "

        
        print(' | '.join(map(str,self.student_data_copy[0])))

        table_design =[]    
        for i in range(len(self.student_data_copy[0])):
            table_design.append('------') 

        print('|'.join(table_design))

        for i in range(len(self.student_data_copy[1:])):   
            padding = [std.center(5) for std in self.student_data_copy[1:][i][:-1]]
            print(' |'.join(map(str,padding)))
        print('|'.join(table_design))
        print('\n')

        hieghest_avg =[]
        for i in range(1,len(self.student_data_copy)):
            hieghest_avg.append(self.student_data_copy[i][-1])

        hieghest_avg_index = hieghest_avg.index(max(hieghest_avg))

        print(str(len(self.student_id))+ ' students, '+str(len(self.course_id))+
        ' courses, the top student is '+ self.student_id[int(hieghest_avg_index)] +', average '+ str(max(hieghest_avg))+'\n')
    
    #method to read the student related data this reads students .txt
    def read_students(self,file_name):
        student_data = open(file_name,"r")
        line = student_data.readline()
        while(line != ""):
            line = line.strip().split(" ")
            line = [x.strip()for x in line]
            self.students.append(line)
            line = student_data.readline()
        student_data.close()
        return self.students
    
    #generating the student repot and also generating the txt file
    def get_student_report(self):
        compulsary_course =[]
        for i in self.course_data_copy:

            if (i[2] == 'C1') or i[2] == 'C2' or i[3] == 'C3':
                compulsary_course.append(i[0])


        for i in self.students:

            for j in range(1,len(self.student_data_copy)):

                if i[0::2][0] == self.student_data_copy[j][0]:
                    compulsary_course_count = 0
                    enrolement_count = 0
                    GPA = 0
                    crpt = 0
                    GPA_Count_marks = 0
                    for k in range(1,len(self.student_data_copy[j])):

                        
                        if (int(self.student_data_copy[j][k]) >= 0) and (int(self.student_data_copy[j][k]) <=100) or (int(self.student_data_copy[j][k]) == 800) or ((self.student_data_copy[j][k]) == 'TBA'):
                            
                            
                            if (self.student_data_copy[0][k]) in compulsary_course:
                                compulsary_course_count+=1
                                enrolement_count += 1
                            else:
                                enrolement_count += 1
                            

                            if (int(self.student_data_copy[j][k]) >= 0) and (int(self.student_data_copy[j][k]) <=100):

                                for a in self.course_data_copy:

                                    if self.student_data_copy[0][k] in a:
                                        credit_score = a[3]
                                        
                                

                                if int(self.student_data_copy[j][k]) >= 80:

                                    GPA += (4* int(credit_score))
                                    GPA_Count_marks+= int(credit_score)
                                    crpt+= int(credit_score)
                                elif int(self.student_data_copy[j][k]) > 69 and int(self.student_data_copy[j][k]) < 80:
                                    GPA += (3* int(credit_score))
                                    GPA_Count_marks+= int(credit_score)
                                    crpt += int(credit_score)
                                elif int(self.student_data_copy[j][k]) > 59 and int(self.student_data_copy[j][k]) < 70:
                                    GPA += (2* int(credit_score))
                                    GPA_Count_marks+= int(credit_score)
                                    crpt += int(credit_score)
                                elif int(self.student_data_copy[j][k]) > 49 and int(self.student_data_copy[j][k]) < 60:
                                    GPA += (1* int(credit_score))
                                    GPA_Count_marks+= int(credit_score)
                                    crpt += int(credit_score)
                                elif int(self.student_data_copy[j][k]) < 49:
                                  
                                    GPA +=  (0* int(credit_score))
                                    GPA_Count_marks+= int(credit_score)
                                    crpt += 0
                    #calculating GPA

                    if GPA_Count_marks != 0:
                        GPA = round(GPA/GPA_Count_marks,2)
                    else:
                        GPA = 0       

                    if i[0::2][1] == 'FT':
                        if compulsary_course_count < 3 or crpt < 50:

                            crpt = str(crpt) + ' !'
                            i.append(crpt)
                        else:
                            i.append(str(crpt))

                    elif i[0::2][1] == 'PT':
                        if compulsary_course_count < 2 or crpt < 30:

                            crpt = str(crpt) + ' !'
                            i.append(crpt)
                        else:
                            i.append(str(crpt))

                    i.append(str(GPA))
        print('\n')
        time = datetime.now()
        date_and_time = time.strftime("%d/%m/%Y %H:%M")
        try:
            srf = open("student_report.txt","r+")
            a = srf.read()

        except:
            pass

        srf = open("student_report.txt","w+")
        srf.write('\n')
        srf.write(" ")
        srf.write('\n')
        srf.write("Report Generated on : ")
        srf.write(date_and_time)
        srf.write('\n')
        
        print(f"{'SID':7s}{'Name':12s}{'Mode.':6s}{'Enl.':6s}{'GPA'}")
        srf.write(f"{'SID':7s}{'Name':12s}{'Mode.':6s}{'Enl.':6s}{'GPA'}\n")
        print('-'*36,end='')
        srf.write('-'*36+'\n')
        print()
        
        def sorting(a):
            return (sorted(a, key = lambda x:x[4] , reverse=True))


        self.students = sorting(self.students)
        


        for i in range(len(self.students)):
            

            print(f"{self.students[i][0]:7s}{self.students[i][1]:13s}{self.students[i][2]:6s}{self.students[i][3]:5s}{self.students[i][4]}")
            srf.write(f"{self.students[i][0]:7s}{self.students[i][1]:13s}{self.students[i][2]:6s}{self.students[i][3]:5s}{self.students[i][4]}\n")

        print('-'*36+'\n')
        srf.write('-'*36+'\n')
        srf.close
        print("student_report.txt generated!")

        try:
            srf = open("student_report.txt","a+")
            srf.write(a)
            srf.close()
        except:
            pass

# main class  
def main():

    
    #initilizing the student method
    b = Student()
    #loading all the files 
    b.read_scores(sys.argv[1])
    b.read_courses(sys.argv[2])
    b.read_students(sys.argv[3])
    #setting up all the important methods
    b.set_course_id()
    b.set_student_id()
    b.set_student_data_copy_to_student()
    b.set_student_data_to_course()
    b.set_course_data_copy()
    #getting the reports or files
    b.get_result()
    b.get_course_average()
    b.set_student_data_copy_to_student()    
    b.get_student_report()

    
    
    


if __name__=="__main__":
    main()

###############################################################################################################################################################################################

# Student Name  : Srujan Basavaraj
# completed HD Level -90%
# created all the required classes and also designed the 
# programm will not work if flot digits are given as scores(HD level 3 task )
#everything else is working
#no variables, methods or code snippets dangling outside a class
#programm runs from the terminal 
#This programm can be run like the below example
#the class explination diagram is avilable in ProgFunFinal_s3856311.zip
# eg: Python my_school.py scores.txt courses.txt students.txt

###############################################################################################################################################################################################

