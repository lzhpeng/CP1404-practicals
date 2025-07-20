from kivy.app import App
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App that displays a label for each name in a list."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # List of names to display
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        """Let Kivy auto-load the kv file."""
        return super().build()

    def on_start(self):
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()