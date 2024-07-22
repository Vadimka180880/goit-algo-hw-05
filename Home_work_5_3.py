import timeit

# Реалізація алгоритмів
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1

    # Зміщення за символами (bad character heuristic)
    bad_char = [-1] * 256
    for i in range(m):
        bad_char[ord(pattern[i])] = i

    # Зміщення для паттерна
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    return -1

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def knuth_morris_pratt(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)

    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Завантаження текстів з локальних файлів з обробкою різних кодувань
def read_file_with_multiple_encodings(filename, encodings=['utf-8', 'latin1', 'cp1252']):
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Could not read the file {filename} with the given encodings")

text1 = read_file_with_multiple_encodings('article1.txt')
text2 = read_file_with_multiple_encodings('article2.txt')

# Вибір підрядків
existing_substring = text1[:30]  # Вибрати перші 30 символів з тексту як існуючий підрядок
non_existing_substring = 'non-existing substring that is definitely not in the text'

# Вимірювання часу виконання
time_bm_text1_existing = timeit.timeit(lambda: boyer_moore(text1, existing_substring), number=100)
time_bm_text1_non_existing = timeit.timeit(lambda: boyer_moore(text1, non_existing_substring), number=100)

time_kmp_text1_existing = timeit.timeit(lambda: knuth_morris_pratt(text1, existing_substring), number=100)
time_kmp_text1_non_existing = timeit.timeit(lambda: knuth_morris_pratt(text1, non_existing_substring), number=100)

time_rk_text1_existing = timeit.timeit(lambda: rabin_karp(text1, existing_substring), number=100)
time_rk_text1_non_existing = timeit.timeit(lambda: rabin_karp(text1, non_existing_substring), number=100)

time_bm_text2_existing = timeit.timeit(lambda: boyer_moore(text2, existing_substring), number=100)
time_bm_text2_non_existing = timeit.timeit(lambda: boyer_moore(text2, non_existing_substring), number=100)

time_kmp_text2_existing = timeit.timeit(lambda: knuth_morris_pratt(text2, existing_substring), number=100)
time_kmp_text2_non_existing = timeit.timeit(lambda: knuth_morris_pratt(text2, non_existing_substring), number=100)

time_rk_text2_existing = timeit.timeit(lambda: rabin_karp(text2, existing_substring), number=100)
time_rk_text2_non_existing = timeit.timeit(lambda: rabin_karp(text2, non_existing_substring), number=100)

# Висновки
conclusions = f"""
# Висновки щодо ефективності алгоритмів

## Текст 1

- Боєр-Мур (існуючий підрядок): {time_bm_text1_existing} секунд
- Боєр-Мур (вигаданий підрядок): {time_bm_text1_non_existing} секунд

- Кнут-Морріс-Пратт (існуючий підрядок): {time_kmp_text1_existing} секунд
- Кнут-Морріс-Пратт (вигаданий підрядок): {time_kmp_text1_non_existing} секунд

- Рабін-Карп (існуючий підрядок): {time_rk_text1_existing} секунд
- Рабін-Карп (вигаданий підрядок): {time_rk_text1_non_existing} секунд

## Текст 2

- Боєр-Мур (існуючий підрядок): {time_bm_text2_existing} секунд
- Боєр-Мур (вигаданий підрядок): {time_bm_text2_non_existing} секунд

- Кнут-Морріс-Пратт (існуючий підрядок): {time_kmp_text2_existing} секунд
- Кнут-Морріс-Пратт (вигаданий підрядок): {time_kmp_text2_non_existing} секунд

- Рабін-Карп (існуючий підрядок): {time_rk_text2_existing} секунд
- Рабін-Карп (вигаданий підрядок): {time_rk_text2_non_existing} секунд

## Загальні висновки

...
"""

with open('conclusions.md', 'w', encoding='utf-8') as file:
    file.write(conclusions)
