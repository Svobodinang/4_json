import json


def load_data(filepath):
    with open(filepath, encoding="utf-8", newline="") as f:
        return json.load(f)


def pretty_print_json(data):
    print(json.dumps(data,
                     ensure_ascii=False,
                     indent=4))


if __name__ == '__main__':
    filepath = input("введите путь к файлу: ")
    filepath
    data = load_data(filepath)
    pretty_print_json(data)