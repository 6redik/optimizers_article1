"""
Запускатор оптимизаторов.
"""
from typing import Dict, Any
from time import time
from functools import wraps
import pandas as pd


def timeit(function):
    "Измерение времени выполнения функции"
    @wraps(function)
    def wrapper(*args, **kwargs):
        t0 = time()
        result = function(*args, **kwargs)
        duration = time() - t0
        result['t'] = duration
        return result
    return wrapper


@timeit
def pricing_optimization(data: pd.DataFrame,
                         opt_model: Any,
                         ) -> Dict:
    """
    Запуск расчета оптимальных цен с помощью указанного класса оптимизатора и параметров
    :param sources: входные данные для оптимизации
    :param opt_model: класс модели оптимизатора
    :param opt_params: параметры оптимизации
    :param solver: солвер для оптимизации
    :return: словарь, возвращаемый моделью оптимизации
    """

    model = opt_model(data)

    model.init_objective()
    model.add_constraints()
    model.init_constraints()
    result = model.solve()
    result['model_class'] = model
    return result
