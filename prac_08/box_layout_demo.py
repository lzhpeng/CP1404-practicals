from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy App that demonstrates BoxLayout and input handling."""
    def build(self):
        """Set up the app window and load the kv layout."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def submit_name(self):
        """Print a greeting using the entered name."""
        name_input = self.root.ids.name_input
        name = name_input.text.strip()
        if name:
            greeting = "Hello, {}!".format(name)
            print(greeting)

    def clear_name(self):
        name_input = self.root.ids.name_input
        name_input.text = ""


if __name__ == "__main__":
    BoxLayoutDemo().run()