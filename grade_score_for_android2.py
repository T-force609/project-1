from kivy.app import App
from kivy.uix.floatlayout import *
from kivy.uix.button import Button
from kivy.uix.label import *
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition


    
class info(FloatLayout):
    def __init__(self,):
        super().__init__()
        self.btn = Button(text ="submit", size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.07})
        self.btn.bind(on_press=self.submit)
        self.add_widget(self.btn)
        
        #Creating text and inoput field for user
        self.label = Label(text= "What is your full name:", size_hint=(0.124,0.09), pos_hint={'center_x':0.1, 'center_y':0.9})
        self.entry = TextInput(multiline=False, size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.9})
        self.add_widget(self.label)
        self.add_widget(self.entry)

        self.label1 = Label(text="What is your Matric Number:", size_hint=(0.124,0.09),pos_hint={'center_x':0.128, 'center_y':0.8})
        self.entry1 = TextInput(multiline=False,size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.8})
        self.add_widget(self.label1)
        self.add_widget(self.entry1)

        self.label2 = Label(text="What faculty:", size_hint=(0.124,0.09),pos_hint={'center_x':0.1, 'center_y':0.7})
        self.entry2 = TextInput(multiline=False, size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.7})
        self.add_widget(self.label2)
        self.add_widget(self.entry2)

        self.label3 = Label(text="Which Department:", size_hint=(0.124,0.09),pos_hint={'center_x':0.1, 'center_y':0.6})
        self.entry3 = TextInput(multiline=False, size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.6})
        self.add_widget(self.label3)
        self.add_widget(self.entry3)

        self.label4 = Label(text="What is your course of study:", size_hint=(0.124,0.09),pos_hint={'center_x':0.128, 'center_y':0.5})
        self.entry4 = TextInput(multiline=False, size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.5})
        self.add_widget(self.label4)
        self.add_widget(self.entry4)

        self.label5 = Label(text="What is the name of your school:", size_hint=(0.124,0.09),pos_hint={'center_x':0.128, 'center_y':0.4})
        self.entry5 = TextInput(multiline=False, size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.4})
        self.add_widget(self.label5)
        self.add_widget(self.entry5)

    # creating a Function
    def submit(self, screen):
        self.__name__ = self.entry._get_text()
        self.__name__1 = self.entry1._get_text()
        self.__name__2 = self.entry2._get_text()
        self.__name__3 = self.entry3._get_text()
        self.__name__4 = self.entry4._get_text()
        self.__name__5= self.entry5._get_text()
        Myapp.screen_manager.current = "score"


        print(self.__name__.upper(), self.__name__1.upper(), self.__name__2.upper(), self.__name__3, self.__name__4, self.__name__5.upper())

        
class score(FloatLayout):
    def __init__(self,):
        super().__init__()
        self.subject = {}
        self.unit = []
        self.count = 0
        self.text = Label(text='Do you wish to continue y/n:', size_hint=(0.124,0.09), pos_hint={'center_x':0.128, 'center_y':0.96})
        self.add_widget(self.text)
        self.condition = TextInput(size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.96})
        self.add_widget(self.condition)

        while self.condition != "n":
            t1_pos_y = 0.9
            t2_pos_y = 0.8
            
            self.text1 = Label(text='type "quit" to quit listting', size_hint=(0.124,0.09), pos_hint={'center_x':0.5, 'center_y':t1_pos_y})
            self.text2 = Label(text='enter the subject:', size_hint=(0.124,0.09), pos_hint={'center_x':0.5, 'center_y':t2_pos_y})
            self.sub = TextInput(size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':t1_pos_y})
            self.add_widget(self.text1)
            self.add_widget(self.text2)
            if self.sub =='quit':
                break
            else:
                T_un = Label(text='what is the unit of:', size_hint=(0.124,0.09), pos_hint={'center_x':0.5, 'center_y':t2_pos_y})
                self.add_widget(T_un)
                self.Un = TextInput(size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':t1_pos_y})
                
                self.add_widget(self.Un)
                '''self.score = TextInput('your grade in the subject:', size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':t1_pos_y})
                self.subject[self.sub.upper()] = self.score.capitalize()'''
                self.unit.append(self.Un)

                t1_pos_y -= 0.1
                t2_pos_y -= 0.1
                self.count +=1

        self.asign = self.subject.values()
        self.dict_len = len(self.subject)
        self.btn = Button(text='NEXT', size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.07})
        self.add_widget(self.btn)

    def next():
        pass



class GradescoreApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        firstpage = info()
        screen = Screen(name="info")
        screen.add_widget(firstpage)
        self.screen_manager.add_widget(screen)

        secondpage = score()
        screen2 = Screen(name="score")
        screen2.add_widget(secondpage)
        self.screen_manager.add_widget(screen2)

        return self.screen_manager
        
        
        

if __name__ == '__main__':
    Myapp = GradescoreApp()
    Myapp.run()