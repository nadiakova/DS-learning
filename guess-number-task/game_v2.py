"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def predict_by_div2(number: int = 1) -> int:
    """Угадываем число методом половинного деления
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    beg_num = 1
    end_num = 101

    while beg_num != end_num:
        count += 1
        predict_number = int((beg_num + end_num)/2)  # предполагаемое число
        
        #Сравниваем наше число с серединой интервала, затем корректируем интервал поиска
        if number <= predict_number:
            end_num = int((beg_num + end_num)/2)
        else:
            beg_num = int((beg_num + end_num)/2 + 1)   
    return count


def score_game(predict_by_div2) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_by_div2 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_by_div2(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict_by_div2)

#print(predict_by_div2(70))