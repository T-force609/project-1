
class Grade:
    def __init__(self):
        Grade.A = 5
        Grade.B = 4
        Grade.C = 3
        Grade.D = 2
        Grade.E = 1
        Grade.F = 0
        self.info()
        self.subject_list()
        self.grade_asign()
        self.result()
        

    def info(self):
        print('Hi welcome to grade score program, answer the follow')
        Grade.Fn = input('your first name?:')
        Grade.Sn = input('Your surname?:')
        Grade.On = input('Your other name?:')
        Grade.reg = input('what is your matric number:')
        Grade.faculty = input('What faculty:')
        Grade.department = input('Which department:')
        Grade.option = input('what is your course of study:')
        

    def subject_list(self):
        print('please kindly list the subject your offer in your previous semeter')
        global subject
        subject = {}
        Grade.unit = []
        Grade.count = 0
        Grade.condition = input('Do you wish to continue y/n:')
        

        while Grade.condition != "n":
            print('type "quit" to quit listting')
            Grade.sub = input('enter the subject:')
            if Grade.sub =='quit':
                break
            else:
                Grade.Un = int(input('what is the unit of'+' ' +Grade.sub+':'))
                Grade.score = input('your grade in the subject:')
                subject[Grade.sub.upper()] = Grade.score.capitalize()
                Grade.unit.append(Grade.Un)
                Grade.count +=1
        Grade.asign = subject.values()
        Grade.dict_len = len(subject)


    def grade_asign(self):
        Grade.list = []
        for data in Grade.unit:
            for var in subject.values():
                if var == 'A':
                    vars =  Grade.A*data
                elif var == 'B':
                    vars = Grade.B*data
                elif var == 'C':
                    vars = Grade.C*data
                elif var == 'D':
                    vars = Grade.D*data
                elif var == 'E':
                    vars = Grade.E*data
                else:
                    vars = Grade.F*data
    
                
            print(vars)
        print(Grade.unit)
        
               
    def calculation(self):
        Total_unit = sum(Grade.unit)



    def result(self):
        print('NAME:'+Grade.Fn.upper(),' '+Grade.Sn.upper(),' '+Grade.On.upper())
        print('FACULTY:'+Grade.faculty.upper())
        print('DEPARTMENT:'+Grade.department.upper())
        print('OPTION:'+Grade.option.upper())
        print('REG, NUMBER:'+ Grade.reg.upper())

        for score, subjects in subject.items():
            print(f"Your score of {score} is {subjects}")
            


my_grade=Grade()