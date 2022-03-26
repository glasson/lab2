'''9. Напишите программу, которая запрашивает у пользователя числа до
тех пор, пока каждое следующее число больше предыдущего. В конце
программа сообщает, сколько чисел было введено.'''
def in_put(mas):
    while True:
        print("значение: ", end="")
        try:
            input_value = float(input())
        except ValueError:
            print("Неверный тип данных")
            continue
        if (len(mas)==0) or (input_value > mas[-1]):
            mas.append(input_value)
        else:
            break
    return mas,len(mas)

def create_l() -> float:
    mas = []
    mas,counter=in_put(mas)
    print(mas)
    return counter


def show_counter(f):
    print(f"Введено чисел: {f}")


def main():
    show_counter(create_l())


if __name__ == "__main__":
    main()

