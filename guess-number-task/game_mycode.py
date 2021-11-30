"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def find_number(number: int = 1, beg_num: int = 1, end_num: int = 101,
                step: int = 10) -> int:
    """Находим число в заданном интервале методом перебора
    
    Args:
        number (int, optional): Число, которое необходимо найти. Defaults to 1.
        beg_num (int, optional): Начало интервала. Defaults to 1.
        end_num (int, optional): Конец интервала. Defaults to 101.
        step (int, optional): Шаг. Defaults to 10.
        
    Returns:
        int: Количество попыток
    """
    count = 0
    found_num = beg_num
    
    while found_num <= number:
        count += 1
        found_num = found_num + step
        
    return count

#any_num = 7
#any_num_ones = any_num % 10
#any_num_tens = any_num - any_num_ones

#print(any_num_tens, any_num_ones)
#print(find_number(any_num_tens, 10, 101, 10))
#print(find_number(any_num_ones, 1, 11, 1))

def score_game_v3(find_number) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        find_number ([type]): функция нахождения числа в интервале

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        # Разделим число на десятки и единицы
        num_ones = number % 10
        num_tens = number - num_ones
        
        # Найдём, в каком интервале 0, 10, 20...100 находится наше число
        # далее внутри самого интервала найдём наше число
        count = (find_number(num_tens, 10, 101, 10) + 
                 find_number(num_ones, 1, 11, 1))
        
        count_ls.append(count)

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game_v3(find_number)

#print(predict_by_div2(70))