def caching_fibonacci():
    """
    Функція створює кеш для обчислення чисел Фібоначчі.
    Повертає:
        function: Функція fibonacci для обчислення n-го числа Фібоначчі. 
    """
    #створений пустий словник
    cache = {}
    
    def fibonacci(n):
        """ 
        Обчислює 'n' число Фібоначчі з кешуванням.
        
        Аргументи: 
            n(int): Індекс числа Фібоначчі.
        Повертає:
            int: 'n' число Фібоначчі.
        Пояснення:    
            Якщо n <= 0, повернути 0.
            Якщо n == 1, повернути 1.
            Якщо n є в cache, повернути cache[n].
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache [n]
        
        #Обчислюємо значення, зберігаємо в кеші і повертаємо
        cache [n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache [n]
    
    return fibonacci
     
# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610



