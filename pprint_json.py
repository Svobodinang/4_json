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
            return 0
    else:
        print("Такого файла не существует")
        return 0


if __name__ == '__main__':
    inputh_path = input_json_path()
    if inputh_path!=0:
        pretty_print_json(load_data(inputh_path))
