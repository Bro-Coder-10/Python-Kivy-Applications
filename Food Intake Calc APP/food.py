from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import requests


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Meta_Function(MainScreen):

    food_in = StringProperty("[b]Enter Food Here-->[/b]")
    def food_input(self, widget):
        self.food = (widget.text)
        print(self.food)

    def foodcal(self,widget):
        self.url = "https://food-calorie-data-search.p.rapidapi.com/api/search"
        self.querystring = {"keyword": f"{str(self.food)}"}

        self.headers = {
            'x-rapidapi-key': "f0c85de575msh07a91d3c3a0f9ecp167674jsn6f09eb3e1020",
            'x-rapidapi-host': "food-calorie-data-search.p.rapidapi.com"
        }

        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        x = response.json()
        print(x)
        y=x[0]
        self.ids.output1.text = f"The amount of calories in {self.food} is {y['energ_kcal']} Kilo Calories"


class xxxApp(App):
    def build(self):

        return Meta_Function()


xxxApp().run()
