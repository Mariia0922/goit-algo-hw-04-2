def total_salary(path):
    total = 0
    count = 0
    with open(path, 'r') as file:
        for line in file:
            _, salary = line.strip().split(',')
            total += int(salary)
            count += 1
    average = total / count if count > 0 else 0
    return total, average

total, average = total_salary('salaries.txt')
print(f"Загальна сума заробітних плат: {total}")
print(f"Середня заробітна плата: {average:.2f}")
