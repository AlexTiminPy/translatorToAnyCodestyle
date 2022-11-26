import argparse
import sys

import pyperclip


def start():
    """
    main funk
    :return:
    """
    namespace = parse()
    data = start_transform(namespace)
    result = ""

    if namespace.nameCodestyle == "camelCase":

        result = transform_to_camel_case(data)

    elif namespace.nameCodestyle == "PascalCase":

        result = transform_to_pascal_case(data)

    elif namespace.nameCodestyle == "snake_case":

        result = transform_to_snake_case(data)

    elif namespace.nameCodestyle == "kebab-case":

        result = transform_to_kebab_case(data)

    if namespace.copy:
        pyperclip.copy(result)

    print(result)


def parse() -> argparse.Namespace:
    """
    parse args from console
    :return: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description='Videos to images')

    parser.add_argument('-n', '--nameCodestyle', type=str,
                        help='camelCase\nPascalCase\nsnake_case\nkebab-case',
                        choices=["camelCase", "PascalCase", "snake_case", "kebab-case"])
    parser.add_argument('-s', '--string', type=str, help='string to convert')
    parser.add_argument('-c', '--copy', type=bool, default=False, help='copy to clipboard')

    try:
        namespace = parser.parse_args()
    except Exception as ex:
        print(ex)
        sys.exit()

    return namespace


def start_transform(namespace: argparse.Namespace) -> list:
    """
    clears the data from garbage and leads to a convenient format
    :param namespace: argparse.Namespace
    :return: list
    """
    data = str(namespace.string)
    data = data.replace("-", " ")
    data = data.replace(",", " ")
    data = data.replace(".", " ")
    data = data.replace("/", " ")
    data = data.split(" ")
    data = [i for i in data if i]

    return data


def transform_to_camel_case(string: list) -> str:
    result_string = ""

    result_string += string[0].lower()

    for i in string[1:]:
        t = i.lower().capitalize()
        result_string += t

    return result_string


def transform_to_pascal_case(string: list) -> str:
    result_string = ""

    for i in string:
        t = i.lower().capitalize()
        result_string += t

    return result_string


def transform_to_snake_case(string: list) -> str:
    result_string = ""

    for i in string[:-1]:
        t = i.lower()
        result_string += t + "_"

    result_string += string[-1].lower()

    return result_string


def transform_to_kebab_case(string: list) -> str:
    result_string = ""

    for i in string[:-1]:
        t = i.lower()
        result_string += t + "-"

    result_string += string[-1].lower()

    return result_string


if __name__ == "__main__":
    start()
