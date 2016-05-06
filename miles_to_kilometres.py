from kivy.app import App
from kivy.lang import Builder

class milestokilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root





milestokilometers().run()