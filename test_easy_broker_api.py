import unittest
from easy_broker_api import EasyBrokerAPI

class TestEasyBrokerAPI(unittest.TestCase):
    
    def test_get_properties(self):
        api = EasyBrokerAPI()
        properties = api.get_properties()
        
        # Verificar que la respuesta contiene la clave "content"
        self.assertIn("content", properties)
        
        # Verificar que el contenido no esté vacío
        self.assertGreater(len(properties["content"]), 0)
        
        # Verificar que cada propiedad tenga un título
        for prop in properties["content"]:
            self.assertIn("title", prop)

if __name__ == '__main__':
    unittest.main()
