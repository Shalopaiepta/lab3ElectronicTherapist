import unittest
from src.therapist import Therapist


class TestTherapist(unittest.TestCase):

    def test_therapist_class_creation(self):
        therapist = Therapist()
        self.assertIsNotNone(therapist)


if __name__ == '__main__':
    unittest.main()