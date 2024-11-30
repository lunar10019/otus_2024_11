def calculate_average(nums):
    if not nums:  # Проверка на пустой список
        return "Список пуст"  # Возвращаем текст для пользователя
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


numbers = [10, 15, 20]
result = calculate_average(numbers)
print("The average is:", result)
