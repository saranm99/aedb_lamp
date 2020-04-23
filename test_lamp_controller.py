import unittest
from controler import LampController

class TestLampController(unittest.TestCase):
    def setUp(self):
        self.controller = LampController()
        self.l1 = self.controller.create_lamp('L1')
        self.l2 = self.controller.create_color_lamp('RED', 'L2')
        self.l3 = self.controller.create_array('L3')
        self.l4 = self.controller.create_color_lamp('Black', 'L4')

    def create_array_with_3_lamps(self):
        self.l3.append_lamp(self.l1)
        self.l3.append_lamp(self.l2)
        self.l3.append_lamp(self.l4)

    def test_turn_on(self):
        self.controller.turn_on(self.l1)
        self.assertTrue(self.controller.is_on(self.l1))

    def test_turn_off_after_on(self):
        self.controller.turn_on(self.l2)
        self.controller.turn_off(self.l2)
        self.assertFalse(self.controller.is_on(self.l2))

    def test_set_ID(self):
        self.assertTrue(self.l1.get_ID(),"L1")

    def test_set_color(self):
        self.controller.set_color(self.controller.get_lamp_object('L4'),"Green")
        self.assertTrue(self.controller.get_color(self.controller.get_lamp_object('L4')),"Green")

    def test_add_lamps_to_array(self):
        self.l5 = self.controller.create_lamp('L5')
        self.l3.append_lamp(self.l5)
        self.assertTrue(self.l5 in self.l3.get_conjunto())

    def test_remove_lamp_from_array(self):
        self.create_array_with_3_lamps()
        self.l3.remove_lamp(self.l1)
        self.assertFalse(self.l1 in self.l3.get_conjunto())

    def test_turn_lamps_in_array_on(self):
        self.create_array_with_3_lamps()
        self.controller.turn_on(self.l3)
        for lamp in self.l3.get_conjunto():
            self.assertTrue(self.controller.is_on(lamp))

    def test_turn_off_lamps_after_being_turned_on(self):
        self.create_array_with_3_lamps()
        self.controller.turn_on(self.l3)
        self.controller.turn_off(self.l3)
        self.assertFalse(self.controller.is_on(self.l3))

    def test_get_array_by_id(self):
        self.create_array_with_3_lamps()
        self.l6 = self.controller.create_array('L6')
        self.assertEqual(self.controller.get_array_object('L6').get_conjunto(), [])

    def test_get_object_by_id(self):
        self.create_array_with_3_lamps()
        self.assertEqual(self.controller.get_object_by_id('L2'), self.l2)

    def test_is_lamp_in_an_array(self):
        self.create_array_with_3_lamps()
        self.assertTrue(self.controller.is_lamp_in_an_array(self.controller.get_lamp_object('L2')))
        self.l3.remove_lamp(self.controller.get_lamp_object('L2'))
        self.assertFalse(self.controller.is_lamp_in_an_array(self.controller.get_lamp_object('L2')))

if __name__ == '__main__':
    unittest.main()
