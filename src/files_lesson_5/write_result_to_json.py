import json
from typing import Dict
from typing import List
from typing import Any


def write_result_to_json(data: List[Dict[str, Any]], file_path: str) -> None:
    with open(file_path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
