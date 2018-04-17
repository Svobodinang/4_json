import json


def load_data(filepath):
    with open(filepath, encoding="utf-8", newline="") as json_file:
        return json.load(json_file)


def pretty_print_json(data_json):
    print(json.dumps(data_json,
                     ensure_ascii=False,
                     indent=4))


if __name__ == '__main__':
    filepath = input("введите путь к файлу: ")
    filepath
    data_json = load_data(filepath)
    pretty_print_json(data_json)