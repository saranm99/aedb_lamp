import unittest
from controler import LampController

class TestLampController(unittest.TestCase):    
    def __init__(self,*args, **kwargs):
        super(TestLampController, self).__init__(*args, **kwargs) #Não percebo esta linha de código... Mas parece funcionar
        self.controller= LampController()

    def test_turn_on(self):
        self.controller.turn_on()
        self.assertTrue(self.controller.is_on())
        
    def test_turn_off_after_on(self):
        self.controller.turn_on()
        self.controller.turn_off()
        self.assertFalse(self.controller.is_on())

if __name__ == '__main__':
    unittest.main()
