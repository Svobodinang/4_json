import json
import sys
import os


def load_data(filepath):
    try:
        with open(filepath, encoding="utf-8") as json_file:
            return json.load(json_file)
    except json.decoder.JSONDecodeError:
        return None


def pretty_print_json(decoded_data):
    print(json.dumps(
        decoded_data,
        ensure_ascii=False,
        indent=4
    ))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit("Вы не ввели путь к файлу")
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
    	exit("Такого файла не существует")
        
    decoded_file = load_data(file_path)
    if decoded_file is None:
        exit("В файле не json текст")

    pretty_print_json(decoded_file)
