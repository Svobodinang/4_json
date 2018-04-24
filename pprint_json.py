import json
import sys
import os


def load_data(filepath):
    try:
        with open(filepath, encoding="utf-8") as json_file:
            return json.load(json_file)
    except json.decoder.JSONDecodeError:
        print("В файле не json текст")
        return None


def pretty_print_json(decoded_data):
    print(json.dumps(
        decoded_data,
        ensure_ascii=False,
        indent=4
    ))


def check_path_file(path):
    if os.path.isfile(path):
        return "ok"
    else:
        return None


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit("Вы не ввели путь к файлу")
    if check_path_file(sys.argv[1]) is None:
        exit("Такого файла не существует")
    if load_data(sys.argv[1]) is None:
        exit()

    pretty_print_json(load_data(sys.argv[1]))
