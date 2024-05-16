def fibonacci_series(max_value):
    series = [0, 1]
    a, b = 0, 1
    while a <= max_value:
        a, b = b, a + b
        series.append(a)
    return series

max_value = 500
fibonacci_series_list = fibonacci_series(max_value)
print("Série de Fibonacci até que o valor seja maior que 500:")
print(fibonacci_series_list)
