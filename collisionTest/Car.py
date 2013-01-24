from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

class Car(Widget):
	x = NumericProperty(0)		
	
# x, y, sizeX, sizeY, maxSpeed, maxAcceleration, maxNegAcceleration