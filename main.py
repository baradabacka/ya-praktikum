from typing import List


def subtracting_list(first_list: List[int], second_list: List[int]) -> List[int]:
    """
    Функция удаляет элементы из первого списка, если они присутствуют во втором
    Функция работает за O(n) по сложности и за O(n) по памяти

    :param first_list:
    :param second_list:
    :return:
    """
    black_listed_items = dict()

    # Заполняем black_list элементами второго списка
    # Данная операция выполнится за O(n) по сложности и памяти(если все элементы уникальны)
    for i in second_list:
        black_listed_items[i] = 1

    # Удаление выполнится за O(n) по сложности и O(1) по памяти
    i = 0
    deleted = 0  # Будем запоминать сколько элементов не подошло
    while i < len(first_list):
        if first_list[i] in black_listed_items:
            # Если элемент есть в black_list, то нам его необходимо удалить
            # что бы не менять размерность массива, мы через сдвиг его перезапишем
            deleted += 1
            i += 1
            continue
        # Перезаписываем ячейки с учетом сдвига удаленных объектов
        first_list[i - deleted] = first_list[i]
        i += 1

    return first_list[0:-deleted]


def delete_zero(arr: List[int]) -> List[int]:
    """
    Функция удаления нулей из массива
    Функция работает за O(n) по сложности и за O(1) по памяти

    :param arr: Список целочисленных чисел, который может содержать нули
    :return: Список целочисленных чисел очищенный от нулей
    """
    # Удаление выполнится за O(n) по сложности и O(1) по памяти
    i = 0
    deleted = 0  # Будем запоминать сколько элементов не подошло
    while i < len(arr):
        if arr[i] == 0:
            # Если элемент равен нулю, то нам его необходимо удалить
            # что бы не менять размерность массива, мы через сдвиг его перезапишем
            deleted += 1
            i += 1
            continue
        # Перезаписываем ячейки с учетом сдвига удаленных объектов
        arr[i - deleted] = arr[i]
        i += 1

    return arr[0:-deleted]
