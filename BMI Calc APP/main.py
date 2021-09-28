from kivy.app import App
from kivy.uix import dropdown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.pagelayout import PageLayout
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Meta_Function(MainScreen):

    def on_slide_weight(self, widget):
        self.weight = int(widget.value)
        print("Weight :" + str(int(widget.value)))
        print(self.weight)

    def on_slide_height(self, widget):
        self.heigh = int(widget.value)
        print("Height :" + str(int(widget.value)))
        print(self.heigh)

    def on_slide_age(self, widget):
        self.age = int(widget.value)
        print("Age :" + str(int(widget.value)))
        print(self.age)

    def on_switch_active(self, widget):
        if widget.active:
            print("Female")
            return True
        if not widget.active:
            print("Male")
            return False

    def bmi_calc(self, widget):
        print(self.weight, self.heigh)
        bm = round(((self.weight) / ((self.heigh/100) ** 2)), 1)
        if bm < 18.5:
            self.ids.output.text = str(f"Your BMI is  * {bm} * Kg/m² \n Your Weight Category is * UNDER-WEIGHT *")
        elif 18.5 <= bm < 25:
            self.ids.output.text = str(f"Your BMI is  * {bm} * Kg/m² \n Your Weight Category is * NORMAL-WEIGHT *")
        elif 25 <= bm <= 30:
            self.ids.output.text = str(f"Your BMI is  * {bm} * Kg/m² \n Your Weight Category is * OVER-WEIGHT *")
        elif bm > 30:
            self.ids.output.text = str(f"Your BMI is  * {bm} * Kg/m² \n Your Weight Category is * OBESE *")
        else:
            self.ids.output.text = str("An error occurred. Please try again!")

    def bmr_calc(self, widget):
        BMR_M = 88.362 + (13.397 * self.weight) + (4.799 * self.heigh) - (5.677 * self.age)
        BMR_F = 447.593 + (9.247 * self.weight) + (3.098 * self.heigh) - (4.330 * self.age)
        if self.on_switch_active():
            print(BMR_F)
        if not self.on_switch_active():
            print(BMR_M)


class FitnessApp(App):
    def build(self):
        return Meta_Function()


FitnessApp().run()
