class Therapist:
    """
    Электронный терапевт — ставит диагноз по симптомам

    Атрибуты:
        questions (list): список вопросов пациенту
    """

    def __init__(self):
        """
        Инициализация терапевта с базой вопросов
        """
        # todo: реализовать полную базу вопросов
        self.questions = [
            "У вас есть температура?",
            "Есть ли кашель?"
        ]

    def ask_question(self, index: int) -> str:
        """
        Задаёт вопрос пациенту по индексу

        Args:
            index (int): индекс вопроса в списке

        Returns:
            str: текст вопроса
        """
        # todo: реализовать метод ask_question позднее до конца
        if index == 0:
            return self.questions[0]
        if index == 1:
            return self.questions[1]
        return "Вопрос не найден"

    def get_diagnosis(self, answers: list) -> str:
        """
        Ставит диагноз по ответам на вопросы

        Args:
            answers (list): список булевых ответов (True=да, False=нет)

        Returns:
            str: текст диагноза
        """
        # todo: реализовать метод get_diagnosis позднее до конца
        if len(answers) > 0 and answers[0] == True:
            return "Возможна простуда"
        return "Здоровы"