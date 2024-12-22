from src.files_lesson_5.distribute_books import distribute_books
from src.files_lesson_5.read_books import read_users
from src.files_lesson_5.read_users import read_books
from src.files_lesson_5.write_result_to_json import write_result_to_json

from files import JSON_RESULT_PATH
from files import JSON_FILE_PATH
from files import CSV_FILE_PATH


def create_file_result() -> None:
    # Читаем книги и пользователей из CSV/JSON файлов
    books_list = read_books(CSV_FILE_PATH)
    users_list = read_users(JSON_FILE_PATH)

    # Распределяем книги между пользователями
    combined_list = distribute_books(books_list, users_list)

    # Записываем результат в JSON файл
    write_result_to_json(combined_list, JSON_RESULT_PATH)


create_file_result()
