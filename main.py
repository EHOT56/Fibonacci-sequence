import math
import time


class Fibonacci:
    def __init__(self) -> None:
        pass

    @staticmethod
    def number(n):
        a, b = 0, 1  # Инициализация: a — текущее число Фибоначчи, b — следующее
        for _ in range(n):  # Цикл выполняется n раз
            a, b = b, a + b  # Сначала обновляем a (текущее число), затем b (следующее)
        return a  # Возвращаем текущее число Фибоначчи
    
    @staticmethod
    def number_recursive(n): # Намного медленнее при больших числах
        if n <= 1:
            return n
        return Fibonacci.number_recursive(n - 1) + Fibonacci.number_recursive(n - 2)
    
    @staticmethod
    def fibonacci_binet(n):
        phi = (1 + math.sqrt(5)) / 2  # "Золотое сечение"
        return round((phi**n - (-phi)**-n) / math.sqrt(5))


fibonacci = Fibonacci()
n = 40

print("Первый вариант: ")
start = time.time()
print([fibonacci.number(i) for i in range(n)])
print("Время исполнения c генератором:", time.time() - start)

print("Второй вариант: ")
start = time.time()
print([fibonacci.number_recursive(i) for i in range(n)])
print("Время исполнения c рекурсией:", time.time() - start)

print("Третий вариант: ")
start = time.time()
print([Fibonacci.fibonacci_binet(i) for i in range(n)])
print("Время исполнения c формулой:", time.time() - start)
