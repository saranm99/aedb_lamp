import uittest
from controler import LampController

class TestLampController(unittest.TestCase):
    def setUp(self):
        self.controller= LampController()

    def test_turn_on(self):
        self.controller.turn_on()
        self.assertTrue(self.controller.is_on())

    def test_turn_off_after_on(self):
        self.controller.turn_on()
        self.controller.turn_off()
        self.assertFalse(self.controller.is_on())

    def test_set_ID(self):
        self.controller.set_ID("L1")
        self.assertTrue(self.controller.get_ID(),"L1")

    def test_set_color(self):
        self.controller.set_color("Black")
        self.assertTrue(self.controller.get_color(),"Black")

    def test_array_ID(self):
        self.controller.set_array_ID("L2")
        self.assertTrue(self.controller.get_array_ID(),"L3")

    def test_append_lamp(self):
        new_lamp =

if __name__ == '__main__':
    unittest.main()
