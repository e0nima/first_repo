import random


def generate_num():
    return random.randint(1, 100)


def is_valid(a):
    if a.isdigit() and 1 <= int(a) <= 100:
        return True
    return False


n = generate_num()
print("Добро пожаловать в числовую угадайку! <3")
while True:
    res = input()
    if not is_valid(res):
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue
    else:
        res = int(res)
        if n < res:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif n > res:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        else:
            print("Вы угадали, поздравляем!")
            break
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
