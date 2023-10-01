try:
    list_of_numbers = []
    while True:
        number = input("Введіть число: ")
        if number == "":
            break
        list_of_numbers.append(int(number))

    sum_of_numbers = 0
    for number in list_of_numbers:
        sum_of_numbers += number

    average = sum_of_numbers / len(list_of_numbers)

    print("Сума всіх елементів списку: {}".format(sum_of_numbers))
    print("Середньоарифметичне всіх елементів списку: {}".format(average))

except Exception as e:
    print(e)