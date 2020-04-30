class Lamp:

    def __init__(self):
        self.state = False
        self.ID = None


    def set_on(self):
        self.state = True

    def set_off(self):
        self.state = False


    def get_state(self):
        return self.state

    def set_ID(self, ID):
        self.ID = ID

    def get_ID(self):
        return self.ID

class ColorLamp(Lamp):
    def __init__(self):
        Lamp.__init__(self)
        self.color = "White" #Default Color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

class LampArray(Lamp):
    def __init__(self):
        self.conjunto = []

    def append_lamp(self, lamp):
        self.conjunto.append(lamp)

    def remove_lamp(self, lamp):
        self.conjunto.remove(lamp)

    def set_on(self):
        for lamp in self.conjunto:
            lamp.set_on()

    def set_off(self):
        for lamp in self.conjunto:
            lamp.set_off()

    def get_conjunto(self):
        return self.conjunto

    def get_state(self):
        result = []
        for lamp in self.conjunto:
            result.append(lamp.get_state())
        return result[0]
