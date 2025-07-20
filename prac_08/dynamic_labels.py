from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        return Builder.load_file('dynamic_labels.kv')

    def on_start(self):
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

if __name__ == '__main__':
    DynamicLabelsApp().run()