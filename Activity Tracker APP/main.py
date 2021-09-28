import requests
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

    def on_slide_act(self, widget):
        self.act = int(widget.value)
        print("Activity Level :" + str(int(widget.value)))
        print(self.act)

    def on_slide_goal(self, widget):
        goal = ['maintain', 'mildlose', 'weightlose', 'extremelose', 'mildgain', 'weightgain', 'extremegain']
        self.goal = goal[int(widget.value)-1]
        print("Goal :" + goal[int(widget.value)-1])
        print(int(widget.value)+1)

    def on_slide_diet(self,widget):
        diet = ['balanced', 'lowfat', 'lowcarbs', 'highprotein']
        self.diet = diet[int(widget.value)-1]
        print("Goal :" + diet[int(widget.value) - 1])
        print(int(widget.value) + 1)

    def on_switch_active(self, widget):
        self.switch_state = 0
        if widget.active:
            print("Female")
            self.switch_state = 'female'
            return self.switch_state
        if not widget.active:
            print("Male")
            self.switch_state = 'male'
            return self.switch_state

    def bmi_calc(self, widget):
        print(self.weight, self.heigh)
        bm = round((self.weight / ((self.heigh / 100) ** 2)), 1)
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
        BMR_M = 78.362 + (13.397 * self.weight) + (4.799 * self.heigh) - (5.677 * self.age)
        BMR_F = 447.593 + (9.247 * self.weight) + (3.098 * self.heigh) - (4.330 * self.age)
        if self.switch_state == 'f':
            self.ids.output.text = str(f"Your Basal Metabolic Rate (BMR) is {BMR_F}")
        else:
            self.ids.output.text = str(f"Your Basal Metabolic Rate (BMR) is {BMR_M}")

    def act_calc(self, widget):
        self.url = "https://fitness-calculator.p.rapidapi.com/macrocalculator"
        self.querystring = {"age": f"{self.age}", "gender": f"{self.switch_state}", "height": f"{self.heigh}", "weight": f"{self.weight}",
                            "activitylevel": f"{self.act}", "goal": f"{self.goal}"}
        self.headers = {
            'x-rapidapi-key': "f0c85de575msh07a91d3c3a0f9ecp167674jsn6f09eb3e1020",
            'x-rapidapi-host': "fitness-calculator.p.rapidapi.com"
        }
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        x = response.json()
        d = x[self.diet]
        self.ids.output1.text = str(f"Your current daily calorie expenditure is {round(x['calorie'],2)} kcals/day-->\n"
                                    f"Your diet must contain these amounts of nutrients-->")
        self.ids.output2.text = str(d)


class FityApp(App):
    def build(self):
        return Meta_Function()


FityApp().run()
