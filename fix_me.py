def calculate_average(nums):
    if not nums:  # Проверка на пустой список
        return 0  # Возвращаем 0, если список пустой
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


numbers = [10, 15, 20]
result = calculate_average(numbers)
print("The average is:", result)
