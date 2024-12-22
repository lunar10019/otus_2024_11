import json

from typing import Dict
from typing import List
from typing import Any


# Чтение данных из JSON
def read_users(path: str) -> List[Dict[str, Any]]:
    all_users = []
    with open(path, mode="r", encoding="utf-8") as f:
        users = json.load(f)
        users_list = users

        for user in users_list:
            all_users.append(user)
    return all_users
