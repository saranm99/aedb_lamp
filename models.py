class Lamp:
    def __init__(self):
        self.state = False
    
    def set_on(self):
        self.state = True
    
    def set_off(self):
        self.state = False
    
    def get_state(self):
        return self.state

class colourLamp:
    
    def __init__(self):
        self.colour = "White" #default colour
        Lamp.__init__(self)

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

class LampArray:
    def __init__(self):
        self.conjunto = []
    
    def append_lamp(self, lamp):
        self.conjunto.append(lamp)
    
    def turn_on(self):
        for lamp in self.conjunto:
            lamp.set_off()
    
    def get_conjunto_states(self):
        result = []
        for lamp in self.conjunto:
            result.append(lamp.get_state())
