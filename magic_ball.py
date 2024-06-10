import random

answers = [
    "Бесспорно",
    "Мне кажется - да",
    "Пока неясно, попробуй снова",
    "Даже не думай",
    "Предрешено",
    "Вероятнее всего",
    "Спроси позже",
    "Мой ответ - нет",
    "Никаких сомнений",
    "Хорошие перспективы",
    "Лучше не рассказывать",
    "По моим данным - нет",
    "Можешь быть уверен в этом",
    "Да",
    "Сконцентрируйся и спроси опять",
    "Весьма сомнительно",
]


def u_r_welcome():
    print('Hello World! I"m magic ball and i have answers for all of your questions')
    return input("What is your name?\n")


def main_loop():
    while 1:
        print("Ask me your question, please!")
        input()
        print(random.choice(answers))
        next = input("Do u wanna ask me smth more?\n")
        if next.lower() == "no":
            print("Come back if u will have new questions! cya\n")
            break


name = u_r_welcome()
print("Hello,", name)
main_loop()
