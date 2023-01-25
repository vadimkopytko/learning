import numpy as np

def random_predict_20(number:int=1) -> int:
    """Рандомно угадываем число за 20 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        проверяем на 2 условия: случайное число больше/ меньше загаданного и 
        разница между этими двумя числа больше 10/ меньше -10, 
        чтобы можно было корректировать случаное число на +/- 10 (отссекаем сразу десятки).
        Затем если разница между числам меньше 10, то проверяем на разницу больше 1/ меньше -1, 
        корректируя случайное число на 1.

    Returns:
        int: Число попыток
    """

    count = 0 # счетчик
    predict = np.random.randint(1, 101) # случайное число
    
    while number != predict:
        count += 1
        if number > predict and number - predict > 10:
            predict += 10
        elif number > predict and number - predict >= 1:
            predict += 1
        elif number < predict and number - predict < -10:
            predict -= 10
        elif number < predict and number - predict <= -1:
            predict -= 1
    return count 

def score_game_20(random_predict_20) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict_20 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_20(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# RUN
if __name__ == '__main__':
    score_game_20(random_predict_20)