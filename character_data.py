import json
import os


def get_move_data(character: str, character_input: str) -> str | bool:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    print(absolute_path)
    with open(f"{absolute_path}/character_json.json", "r") as file:
        content = json.loads(file.read())
        try:
            file_content = content[character][character_input]
            bot_message = " ".join(f"{key}: {value} | " for key, value in file_content.items())
            return bot_message
        except KeyError as e:
            return False
