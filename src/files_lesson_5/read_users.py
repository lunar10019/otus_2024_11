from csv import DictReader

from typing import Dict
from typing import List
from typing import Any


# Чтение данных из csv
def read_books(path: str) -> List[Dict[str, Any]]:
    books = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = DictReader(f)
        for row in reader:
            books.append(row)
    return books
