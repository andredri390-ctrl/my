result = []
data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
def divider(a, b):
    if a < b:
        raise ValueError("помилка: a кеньше b")
    if b > 100:
        raise IndexError("помилка: b більше 100")
    return a / b
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"зпіймали виключення: {type(e).__name__} -> {e}")
print("\nФінальний список результатів:")
print(result)