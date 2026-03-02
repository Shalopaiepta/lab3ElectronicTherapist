import unittest
from src.therapist import Therapist


class TestTherapist(unittest.TestCase):

    def test_therapist_class_creation(self):
        therapist = Therapist()
        self.assertIsNotNone(therapist)
    def test_ask_question_returns_string(self):
        therapist = Therapist()
        result = therapist.ask_question(0)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
    def test_ask_question_index_1(self):
        therapist = Therapist()
        result = therapist.ask_question(1)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
    def test_get_diagnosis_returns_string(self):
        therapist = Therapist()
        answers = [True, False]
        result = therapist.get_diagnosis(answers)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)


if __name__ == '__main__':
    unittest.main()