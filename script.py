from itertools import product

import json
import os
import re


def parse_list(items):
    return list(filter(bool, [item.strip() for item in items]))


def parse_matrix(matrix_str):
    matrix_lines = parse_list(matrix_str.splitlines())
    matrix_items = []
    for line in matrix_lines:
        matches = re.findall(r"(([\w\-]+){1}(?:\s+)?\{(.+?(?=\})){1}\})+", line)
        assert len(matches)
        groups = {}
        for match in matches:
            assert len(match) == 3
            values = parse_list(match[2].split(","))
            assert len(values)
            group_name = match[1].strip()
            groups[group_name] = [{group_name: value.strip()} for value in values]
        for value in product(*groups.values()):
            matrix_item = {}
            for item in value:
                matrix_item.update(item)
            matrix_items.append(matrix_item)
    return matrix_items


def main():
    matrix_str = os.environ["INPUT_MATRIX"]
    matrix_items = parse_matrix(matrix_str)
    matrix_json = json.dumps(matrix_items)
    matrix_data = f"\nmatrix={matrix_json}\n".encode("utf-8")
    with open(os.environ["GITHUB_OUTPUT"], "ab") as file:
        file.write(matrix_data)


if __name__ == "__main__":
    main()
