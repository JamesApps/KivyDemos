from kivy.app import App
from kivy.lang import Builder

class milestokilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def calculate(self):
        miles = self.error_check_miles()
        kilometers = miles * 1.60934
        self.root.ids.output_label.text = str(kilometers)

    def handle_increment(self, increment):
        miles = self.error_check_miles() + increment
        self.root.ids.input_number.text = str(miles)
        self.calculate()

    def error_check_miles(self):
        try:
            miles = float(self.root.ids.input_number.text)
            return miles
        except ValueError:
            return 0



milestokilometers().run()