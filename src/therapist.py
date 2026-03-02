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
    def get_diagnosis(self, answers: list) -> str:
        # todo: реализовать метод get_diagnosis позднее до конца
        if len(answers) > 0 and answers[0] == True:
            return "Возможна простуда"
        return "Здоровы"