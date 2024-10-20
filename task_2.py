import re 
from typing import Callable

def generator_numbers(text: str):
    """
    Генератор, який ітерує по всіх дійсних числах у тексті , відлкремлених пробілами.
    """
    #регулярний вираз для пошуку дійсних чисел
    pattern = r'\b\d+\.\d+|\b\d+\b'
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    """
    Обчислює загальну суму чисел у тексті, викорситовуючи генератор чисел, переданий як аргумент.
    """
    return sum(func(text))
 
#Приклад використання   
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

#Загальний дохід: 1351.46
