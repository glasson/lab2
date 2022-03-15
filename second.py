#Напишите программу, вычисляющую сумму всех чётных чисел в диапазоне от 1 до 90 включительно
def generate_list():
    evenmas=[i for i in range(1,91) if i%2==0]
    return evenmas
def count(evenmas):
    return sum(evenmas)
def show(evenmas):
    print(evenmas)
def main():
    show(count(generate_list()))
if __name__=="__main__":
    main()


