"""
Squaring App
A simple Kivy app to square a number entered by the user.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """Kivy App that squares a user-entered number."""
    def build(self):
        """Set up the app window and load the kv layout."""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Calculate the square of the input value and display it."""
        try:
            result = int(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = ""


SquareNumberApp().run()