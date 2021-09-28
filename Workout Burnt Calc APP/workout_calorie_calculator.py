from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
import requests


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Workout_calories(MainScreen):

    def on_slide_running(self, widget):
        self.running_speed = int(widget.value)
        print("Running :" + str(int(widget.value)))
        print(self.running_speed)

    def on_duration1(self, widget):
        self.duration1 = int(widget.value)
        print("duration ran:" + str(int(widget.value)))
        print(self.duration1)

    def on_slide_walking(self, widget):
        self.walking_speed = int(widget.value)
        print("Walking speed :" + str(int(widget.value)))
        print(self.walking_speed)

    def on_duration2(self, widget):
        self.duration2 = int(widget.value)
        print("duration walked:" + str(int(widget.value)))
        print(self.duration2)

    def on_slide_yoga(self, widget):
        self.yoga_list = ["nadisodhana", "hatha", "surya namaskara", "power"]
        self.yoga_val = self.yoga_list[int(widget.value)-1]
        print("yoga type :" + str(self.yoga_val))
        print(self.yoga_val)

    def on_duration3(self, widget):
        self.duration3 = int(widget.value)
        print("duration of yoga:" + str(int(widget.value)))
        print(self.duration3)

    cardio_in = StringProperty("[b] Enter cardio excercise name: [b]")

    def on_text_cardio(self, widget):
        self.cardio = str(widget.text)
        print(self.cardio)

    def on_duration4(self, widget):
        self.duration4 = int(widget.value)
        print("duration of workout:" + str(int(widget.value)))
        print(self.duration4)

    def workout_calc(self, widget):
        self.running = {5: 6, 5.5: 7, 6: 7, 6.5: 8, 7: 9, 7.5: 9, 8: 10, 8.5: 10, 9: 11, 9.5: 11, 10: 12, 10.5: 13,
                        11: 14}
        self.walking = {2: 1.7, 2.5: 2.1, 3: 2.5, 3.5: 3, 4: 3.38, 4.5: 3.83, 5: 4.23, 5.5: 4.66, 6: 5.08, 6.5: 5.55,
                        7: 5.93,
                        7.5: 6.35, 8: 6.78}
        self.cardio_ex = {"inchworm": 6, "highknee": 8, "jumprope": 17, "jumpingjacks": 12, "burpees": 10,
                          "pushpups": 7,
                          "squats": 8, "lunges": 6, "mountainclimbers": 10, "plank": 3, "russiantwist": 11.5,
                          "supermanpull": 3,
                          "sicsorkicks": 10, "situps": 3, "highplank kneencrossess": 8, "catcow": 2, "childpose": 4,
                          "armcircles": 15,
                          "bridges": 8, "crunches": 7}

        self.yoga = {"nadisodhana": 2, "hatha": 3, "surya namaskara": 4, "power": 5}


        self.calories_run = 0
        self.calories_walk = 0
        self.calories_cardio = 0
        self.calories_yoga = 0
        self.calories_run = (self.running[int(self.running_speed)]) * self.duration1
        self.calories_walk = (self.walking[int(self.walking_speed)]) * self.duration2
        self.calories_yoga = (self.yoga[str(self.yoga_val)]) * self.duration3

        self.calories_cardio = (self.cardio_ex[str(self.cardio)]) * self.duration4

        self.total_calories = self.calories_run + self.calories_walk + self.calories_cardio + self.calories_yoga
        self.ids.output1.text = str(f"Total calories burned is{round(self.total_calories,2)}")


class wcalsApp(App):
    def build(self):
        return Workout_calories()


wcalsApp().run()
