import models as m
class LampController:

    def __init__(self):
        self.lamps = []
        self.arrays = []

    def add_lamp(self, lamp):
        self.lamps.append(lamp)

    def add_array(self, array):
        self.arrays.append(array)

    def get_lamp_object(self, lamp_ID):
        for lamp in self.lamps:
            if lamp.get_ID() == lamp_ID:
                return lamp

    def turn_on(self, lamp):
        lamp.set_on()

    def turn_off(self, lamp):
        lamp.set_off()

    def is_on(self, lamp):
        return lamp.get_state()

    def create_lamp(self, ID):
        lamp = m.Lamp()
        lamp.set_ID(ID)
        self.add_lamp(lamp)
        return lamp

    #### color lamp ###
    def create_color_lamp(self, color, ID):
        lamp = m.ColorLamp()
        lamp.set_ID(ID)
        lamp.set_color(color)
        self.add_lamp(lamp)
        return lamp

    def set_color(self, lamp, color):
        lamp.set_color(color)

    def get_color(self, lamp):
        return lamp.get_color()

    #### lamp array ###

    def create_array(self, ID):
        array = m.LampArray()
        array.set_ID(ID)
        self.add_array(array)
        return array

    def get_array_object(self, ID):
        for array in self.arrays:
            if array.get_ID() == ID:
                return array

    def is_lamp_in_an_array(self, lamp):
        for array in self.arrays:
            if lamp in array.get_conjunto():
                return True

    def get_object_by_id(self, ID):
        for lamp in self.lamps:
            if lamp.get_ID() == ID:
                return lamp
        for array in self.arrays:
            if array.get_ID() == ID:
                return array

