# -*- coding: utf-8 -*-

from itertools import product

import json
import os
import re


def main():
    matrix_str = os.environ["INPUT_MATRIX"]
    matrix_lines = list(
        filter(bool, [line.strip() for line in matrix_str.splitlines()])
    )
    matrix_items = []
    for line in matrix_lines:
        matches = re.findall(r"(([\w\-]+){1}(?:\s+)?\{(.+?(?=\})){1}\})+", line)
        assert len(matches)
        groups = {}
        for match in matches:
            assert len(match) == 3
            values = re.findall(r"([\w\-]+(?:\.[\d]+){0,2})+", match[2])
            assert len(values)
            groups[match[1]] = [{match[1]: value} for value in values]
        for value in product(*groups.values()):
            matrix_item = {}
            for item in value:
                matrix_item.update(item)
            matrix_items.append(matrix_item)
    matrix_json = json.dumps(matrix_items)
    matrix_data = f"\nmatrix={matrix_json}\n".encode("utf-8")
    with open(os.environ["GITHUB_OUTPUT"], "ab") as file:
        file.write(matrix_data)


if __name__ == "__main__":
    main()
