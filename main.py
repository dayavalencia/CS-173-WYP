import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

# quiz -------------------------------
class ScreenThree(Screen):
    pass

class Question2(Screen):
    pass

class Question3(Screen):
    pass

class Question4(Screen):
    pass

class Question5(Screen):
    pass

class Question6(Screen):
    pass

class Question7(Screen):
    pass

class Question8(Screen):
    pass

class Question9(Screen):
    pass

class Question10(Screen):
    pass

class WYPupper(App):

    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(ScreenOne(name = "screen_one")) #home
        screen_manager.add_widget(ScreenTwo(name = "screen_two")) #filechooser

        screen_manager.add_widget(ScreenThree(name = "screen_three")) #quizstart
        screen_manager.add_widget(Question2(name = "question_2")) #q2
        screen_manager.add_widget(Question3(name = "question_3")) #q3
        screen_manager.add_widget(Question4(name = "question_4")) #q4
        screen_manager.add_widget(Question5(name = "question_5")) #q5
        screen_manager.add_widget(Question6(name = "question_6")) #q6
        screen_manager.add_widget(Question7(name = "question_7")) #q7
        screen_manager.add_widget(Question8(name = "question_8")) #q8
        screen_manager.add_widget(Question9(name = "question_9")) #q9
        screen_manager.add_widget(Question10(name = "question_10")) #q10

        return screen_manager


if __name__ == '__main__':
    app = WYPupper()
    app.run()