from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM_CONVERSTION = 1.60934


class MilesToKilometersApp(App):
    """ MilesToKilometersApp is a Kivy App for converting miles to kilometres """
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ calculates the change from miles to kilometers"""
        value = self.get_valid_input()
        result = value * MILES_TO_KM_CONVERSTION
        self.root.ids.output_label.text = str(result)

    def handle_increase(self, change):
        value = self.get_valid_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_valid_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometersApp().run()
