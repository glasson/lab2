'''9. Напишите программу, которая запрашивает у пользователя числа до
тех пор, пока каждое следующее число больше предыдущего. В конце
программа сообщает, сколько чисел было введено.'''
def first_check_type(mas):
    while True:
        print("значение: ", end="")
        try:
            input_value = float(input())
        except ValueError:
            print("Неверный тип данных")
            continue
        mas.append(input_value)
        counter = 1
        break
    return mas,counter

def other_check_type(mas,counter):
    while True:
        print("значение: ", end="")
        try:
            input_value = float(input())
        except ValueError:
            print("Неверный тип данных")
            continue
        if input_value > mas[-1]:
            mas.append(input_value)
            counter += 1
        else:
            break
    return mas,counter

def create_l() -> float:
    mas = []
    mas,counter=first_check_type(mas)
    mas,counter=other_check_type(mas,counter)
    print(mas)
    return counter


def show_counter(f):
    print(f"Введено чисел: {f}")


def main():
    show_counter(create_l())


if __name__ == "__main__":
    main()

