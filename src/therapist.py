class Therapist:

    def __init__(self):
        self.questions = [
            "У вас есть температура?",
            "Есть ли кашель?"
        ]
    def ask_question(self, index: int) -> str:
        # todo: реализовать метод ask_question позднее до конца
        if index == 0:
            return self.questions[0]
        if index == 1:
            return self.questions[1]
        return "Вопрос не найден"