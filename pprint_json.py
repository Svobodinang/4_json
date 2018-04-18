import json
import sys
import os

def load_data(filepath):
    with open(filepath, encoding="utf-8") as json_file:
        return json.load(json_file)


def pretty_print_json(data_unsorted):
    print(json.dumps(data_unsorted,
                     ensure_ascii=False,
                     indent=4))


def input_json_path():
    file_json = sys.argv[1]

    dirname, exname = os.path.splitext(file_json)

    if os.path.isfile(file_json):
        if exname == ".json":
            return file_json
        else:
            print("Данный файл имеет расширение не .json")
            exit(0)
    else:
        print("Такого файла не существует")
        exit(0)


if __name__ == '__main__':
    json_path = load_data(input_json_path())
    pretty_print_json(json_path)