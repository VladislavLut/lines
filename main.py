try:
    list_of_numbers = []
    while True:
        num = input("Введіть число: ")
        if num == "":
            break
        list_of_numbers.append(int(num))

    number = int(input("Введіть число, кількість появ якого необхідно порахувати: "))

    count = 0
    for n in list_of_numbers:
        if n == num:
            count += 1

    print("Кількість разів, коли число {} присутнє в списку: {}".format(
        num, count))
except Exception as e:
    print(e)