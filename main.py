from src.therapist import Therapist


def main():
    therapist = Therapist()
    answers = []

    print("=== Электронный Терапевт ===")

    for i in range(len(therapist.questions)):
        question = therapist.ask_question(i)
        print(f"\n{question}")
        response = input("Да/Нет: ").strip().lower()
        answers.append(response in ['да', 'd', 'yes', 'y'])

    diagnosis = therapist.get_diagnosis(answers)
    print(f"\nДиагноз: {diagnosis}")


if __name__ == '__main__':
    main()