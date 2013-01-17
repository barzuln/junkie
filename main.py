from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class JunkieGame(Widget):
    pass

class JunkieApp(App):
    def build(self):
        game = JunkieGame()
        return game


if __name__ == '__main__':
    JunkieApp().run()
