import pandas as pd
import numpy as np

from statsmodels.stats.weightstats import ztest


chat_id = 522929689 # Ваш chat ID, не меняйте название переменной

def solution(x) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p = 0.04
    return ztest(x, value=300, alternative='smaller')[1] <= p # Ваш ответ, True или False
