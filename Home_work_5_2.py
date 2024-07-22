# У цій реалізації:

# Функція binary_search(arr, x) приймає відсортований масив arr і значення x, для якого потрібно знайти "верхню межу".
# Змінні left і right визначають початковий і кінцевий індекси для пошуку.
# Під час кожної ітерації обчислюється mid — середина поточного діапазону.
# Якщо arr[mid] менше x, змінюється ліва межа left.
# Якщо arr[mid] більше або рівне x, змінюється права межа right, і одночасно встановлюється значення arr[mid] як потенційна "верхня межа".
# Повертається кортеж з кількістю ітерацій та "верхньою межею".

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        mid = (left + right) // 2
        iterations += 1
        
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            upper_bound = arr[mid]
    
    return (iterations, upper_bound if upper_bound is not None else arr[left])

# Приклад використання:
sorted_arr = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
value = 0.6

iterations, upper_bound = binary_search(sorted_arr, value)
print(f"Кількість ітерацій: {iterations}")
print(f"Верхня межа для {value}: {upper_bound}")

