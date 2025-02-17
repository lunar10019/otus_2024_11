from typing import Dict
from typing import List
from typing import Any


def distribute_books(
    books: List[Dict[str, Any]], users: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    # Создание нового списка словарей с объединёнными данными
    combined_data = []

    # Распределение книг между пользователями
    num_users = len(users)
    num_books = len(books)

    # Определяем, сколько книг каждому пользователю
    base_count = num_books // num_users
    extra_count = num_books % num_users

    # Индекс для книги
    book_index = 0

    for i, user in enumerate(users):
        user_books = []
        # Количество книг для текущего пользователя
        books_for_user = base_count + (1 if i < extra_count else 0)

        for _ in range(books_for_user):
            if book_index < num_books:
                user_books.append(books[book_index])  # Используем books, а не books1
                book_index += 1

        user_with_books = {
            "index": user["index"],
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": user_books,
        }

        combined_data.append(user_with_books)  # Добавляем пользователя в combined_data

    return combined_data  # Возвращаем полный список пользователей с книгами
