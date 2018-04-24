import json
import sys
import os


def load_data(filepath):
    with open(filepath, encoding="utf-8") as json_file:
        return json.load(json_file)


def pretty_print_json(data_decoder):
    print(json.dumps(
        data_decoder,
        ensure_ascii=False,
        indent=4
    ))


def check_json_file():
    try:
        load_data(sys.argv[1])
        return "ok"
    except json.decoder.JSONDecodeError:
        print("В файлене json текст")
        return None
    except IndexError:
        print("Вы не указали путь к файлу")
        return None
    except FileNotFoundError:
        print("Такого файла не существует")
        return None


if __name__ == '__main__':
    if check_json_file() is not None:
        pretty_print_json(load_data(sys.argv[1]))
