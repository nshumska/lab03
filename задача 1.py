count = 0

while True:
    number = int(input("Введіть число (або 0 для завершення): "))
    
    if number == 0:
        break  
    # Завершення циклу при введенні 0
    
    count += 1

print(f"Кількість членів послідовності: {count}")
