from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from Car import Car
from kivy.core.window import Window

class JunkieGame(Widget):
	jc = ObjectProperty(None)
	
	def update(self, dt):
		self.jc.move()

class InnerLine(Widget):
	inL = ObjectProperty(None)
	
class OuterLine(Widget):
	pass
		
class JunkieCar(Widget):
	inL = InnerLine()
	ouL = OuterLine()
	def move(self):
		self.x += self.speed
		self.y += self.speed
		if(self.inL.collide_point(self.x, self.y)):
			self.speed = 0
			print "STOP"

class JunkieApp(App):
    def build(self):
		game = JunkieGame()
		Clock.schedule_interval(game.update, 0.25 )
		return game


if __name__ == '__main__':
    JunkieApp().run()
