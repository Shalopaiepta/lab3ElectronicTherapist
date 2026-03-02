import unittest

class TestTherapist(unittest.TestCase):
    
    def test_therapist_class_creation(self):
        from src.therapist import Therapist
        therapist = Therapist()
        self.assertIsNotNone(therapist)

if __name__ == '__main__':
    unittest.main()