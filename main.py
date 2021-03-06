import kivy
import os
import dog
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
#import image
#from PIL import *
import io
from kivy.core.image import Image as CoreImage
from kivy.properties import StringProperty

import time

class ScreenOne(Screen):
    def read_rankings(self, application):
        if os.stat("rankings.inp").st_size == 0:
            return 0
        else:
            f = open("rankings.inp", "r")
            for x in range(5):
                inp = f.readline()
                inp = inp.rstrip('\n')
                application.rank.append(inp)
            f.close()

            self.manager.screens[16].ids['rank_one'].text = "Rank 1: " + app.rank[0]
            self.manager.screens[16].ids['rank_two'].text = "Rank 2: " + app.rank[1]
            self.manager.screens[16].ids['rank_three'].text = "Rank 3: " + app.rank[2]
            self.manager.screens[16].ids['rank_four'].text = "Rank 4: " + app.rank[3]
            self.manager.screens[16].ids['rank_five'].text = "Rank 5: " + app.rank[4]

            print (application.rank)

class SelectPhoto(Screen):
    pass

class Cam (Screen):
	def capture(self):
        # '''
        # Function to capture the images and give them the names
        # according to their captured time and date.
        # '''
		camera = self.ids['camera']
		timestr = time.strftime("%Y%m%d_%H%M%S")
		filename = "IMG_{}.png".format(timestr)
		camera.export_to_png("IMG_{}.png".format(timestr))
		#to get the image from the camera, pwedeng just select the image name agad. make filename global. Sa desktop it puts the images where your code is saved.
		return filename

	def select(self, arg):
		try:
			imgArg = arg
			imgSrc = imgArg
			print (imgSrc)
			return imgSrc
		except:
			pass

	def set_path(self, imgpath):
		global imgArg
		imgArg=imgpath

class ConfirmPhoto(Screen):
    pass

class ScreenTwo(Screen):


    def select_to(self,*args):

        try:
            imgArg= args[1][0]
            imgSrc=imgArg
            print (imgSrc)
            return imgSrc

        except:
            pass
    def set_path(self,*imgpath):
        global imgArg
        imgArg=imgpath

    def classifier_result(self,ar1):
        return dog.ResNet50_predict_breed(ar1)

class AlgoResult(Screen):

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
    # def getMax(self):
    #     c = max(app.qscore, key=app.qscore.get)

    #     if c == "corgi":
    #         app.img_src = "corgi.jpg"
    #         #app.img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "corgi.jpg")
    #         app.breed_name = "Corgi"
    #     elif c == "pug":
    #         app.img_src = "pug.jpg"
    #         #app.img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pug.jpg")
    #         app.breed_name = "Pug"
    #     elif c == "husky":
    #         app.img_src = "husky.jpg"
    #         #app.img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "husky.jpg")
    #         app.breed_name = "Husky"
    #     elif c == "german_shepherd":
    #         app.img_src = "german_shepherd.jpg"
    #         #app.img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "german_shepherd.jpg")
    #         app.breed_name = "German Shepherd"
    #     elif c == "chihuahua":
    #         app.img_src = "chihuahua.jpg"
    #         #app.img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chihuahua.jpg")
    #         app.breed_name = "Chihuahua"
    def create_rankings(self, application):
        for x in range(5):
            c = max(application.qscore, key=application.qscore.get)

            # if c == "corgi": root.manager.current = 'corgi'
            # elif c == "pug": root.manager.current = 'pug'
            # elif c == "husky": root.manager.current = 'husky'
            # elif c == "german_shepherd": root.manager.current = 'gs'
            # elif c == "chihuahua": root.manager.current = 'chihuahua'

            if c == "corgi": application.rank.append("Corgi"); application.qscore['corgi'] = 0
            elif c == "pug": application.rank.append("Pug"); application.qscore['pug'] = 0
            elif c == "husky": application.rank.append("Husky"); application.qscore['husky'] = 0
            elif c == "german_shepherd": application.rank.append("German Shepherd"); application.qscore['german_shepherd'] = 0
            elif c == "chihuahua": application.rank.append("Chihuahua"); application.qscore['chihuahua'] = 0

    def write_rankings(self, application):
        f = open("rankings.inp", "w")
        for x in range(5):
            f.write(application.rank[x] + "\n")
        f.close()

class Rankings_Page(Screen):
    pass
class No_Rankings(Screen):
    pass
class TermsandConditions(Screen):
    pass
class Privacy_Policy(Screen):
    pass
class Corgi_Result(Screen):
    pass

class Pug_Result(Screen):
    pass

class Husky_Result(Screen):
    pass

class GS_Result(Screen):
    pass

class Chihuahua_Result(Screen):
    pass


class WYPupper(App):
    # scores
    qscore = {
        'corgi': 0,
        'pug': 0,
        'husky': 0,
        'german_shepherd': 0,
        'chihuahua': 0
    }

    rank = []

    # for quiz result
    breed_name = ''


    ar1 = StringProperty("")
    result = StringProperty("")

    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(ScreenOne(name = "screen_one")) #home

        screen_manager.add_widget(SelectPhoto(name = "select_photo")) #Select Photo - 0
        screen_manager.add_widget(Cam(name = "cam")) #Camera - 1
        screen_manager.add_widget(ConfirmPhoto(name = "confirm_photo")) #Camera -2
        screen_manager.add_widget(ScreenTwo(name = "screen_two")) #filechooser - 3
        screen_manager.add_widget(AlgoResult(name = "result")) #algo results screen - 4
        screen_manager.add_widget(ScreenThree(name = "screen_three")) #quizstart - 5
        screen_manager.add_widget(Question2(name = "question_2")) #q2 - 6
        screen_manager.add_widget(Question3(name = "question_3")) #q3 - 7
        screen_manager.add_widget(Question4(name = "question_4")) #q4 - 8
        screen_manager.add_widget(Question5(name = "question_5")) #q5 - 9
        screen_manager.add_widget(Question6(name = "question_6")) #q6 - 10
        screen_manager.add_widget(Question7(name = "question_7")) #q7 - 11
        screen_manager.add_widget(Question8(name = "question_8")) #q8 - 12
        screen_manager.add_widget(Question9(name = "question_9")) #q9 - 13
        screen_manager.add_widget(Question10(name = "question_10")) #q10 - 14

        # result pages
        screen_manager.add_widget(Rankings_Page(name = "rankings")) # - 16
        screen_manager.add_widget(Corgi_Result(name = "corgi"))
        screen_manager.add_widget(Pug_Result(name = "pug"))
        screen_manager.add_widget(Husky_Result(name = "husky"))
        screen_manager.add_widget(GS_Result(name = "gs"))
        screen_manager.add_widget(Chihuahua_Result(name = "chihuahua"))

        screen_manager.add_widget(No_Rankings(name = "no_rankings"))
        screen_manager.add_widget(Privacy_Policy(name = "privacy_policy"))
        screen_manager.add_widget(TermsandConditions(name = "terms_and_conditions"))

        return screen_manager


if __name__ == '__main__':
    app = WYPupper()
    app.run()
