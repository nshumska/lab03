a = int(input("Введіть суму a: "))
b = int(input("Введіть добуток b: "))

found = False

for x in range(1, 1001):
    for y in range(1, 1001):
        if x + y == a and x * y == b:
            found = True
            break

    if found:
        break

if found:
    print(f"Знайдені числа: {min(x, y)} {max(x, y)}")
else:
    print("Числа не знайдені.")
