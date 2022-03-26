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
    return (mas,len(mas))

def create_mas() -> float:
    mas = []
    mas,counter=in_put(mas)
    return (mas,counter)

def show_counter(f):
    print(f"Введено чисел: {f[0]} , \n массив: {f[1]}")


def main():
    show_counter(create_mas())


if __name__ == "__main__":
    main()

