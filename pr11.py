# Завдання 1. Оцінки за тест
grades = [85, 60, 90, 70, 55, 100, 40, 78, 88, 92, 65, 75, 80, 95]
high_grades = [grade for grade in grades if grade > 70]
print("Високі оцінки:", high_grades)
print("Кількість високих оцінок:", len(high_grades))

# Завдання 2. Список покупок
shopping_list = ["молоко", "хліб", "масло", "яйця", "сир", "яблука"]
long_names = [item for item in shopping_list if len(item) > 4]
print("\nТовари з назвою більше 4 символів:", long_names)
print("Кількість таких товарів:", len(long_names))

# Завдання 3. Пошук дубльованих значень
numbers = [1, 2, 3, 4, 3, 2, 5, 6, 5, 7]
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print("\nЧисла, що повторюються:", duplicates)
