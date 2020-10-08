from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicNamesApp(App):
    status_text = StringProperty()
    name_for_list = ['Samuel Giles', 'Jake Perolta', 'Luke Skywalker']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.name_for_list:
            # create a button for each data entry, specifying the text and id
            # (although text and id are the same in this case, you should see how this works)
            self.status_text = "{}".format(name)


DynamicNamesApp().run()
