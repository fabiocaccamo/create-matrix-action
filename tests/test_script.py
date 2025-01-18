import pytest

from script import parse_matrix


@pytest.mark.parametrize(
    "input_matrix, expected_output_matrix",
    [
        (
            "",
            [],
        ),
        (
            "python-version{3.10,3.11,3.12},django-version{5.0,5.1},database{sqlite,postgres}",
            [
                {
                    "python-version": "3.10",
                    "django-version": "5.0",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.0",
                    "database": "postgres",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.1",
                    "database": "postgres",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.0",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.0",
                    "database": "postgres",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.1",
                    "database": "postgres",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.0",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.0",
                    "database": "postgres",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.1",
                    "database": "postgres",
                },
            ],
        ),
        (
            "python-version { 3.10, 3.11, 3.12 }, django-version { 5.0, 5.1 }, database { sqlite, postgres }",
            [
                {
                    "python-version": "3.10",
                    "django-version": "5.0",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.0",
                    "database": "postgres",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.1",
                    "database": "postgres",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.0",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.0",
                    "database": "postgres",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.1",
                    "database": "postgres",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.0",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.0",
                    "database": "postgres",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.1",
                    "database": "postgres",
                },
            ],
        ),
        (
            """
            python-version {3.10}, django-version {4.0, 4.1, 4.2, 5.0, 5.1}, database {sqlite, mysql, postgres}
            python-version {3.11}, django-version {4.1, 4.2, 5.0, 5.1}, database {sqlite, mysql, postgres}
            python-version {3.12}, django-version {4.2, 5.0, 5.1}, database {sqlite, mysql, postgres}
            python-version {3.13}, django-version {5.1}, database {sqlite, mysql, postgres}
            """,
            [
                {
                    "python-version": "3.10",
                    "django-version": "4.0",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.10",
                    "django-version": "4.0",
                    "database": "mysql",
                },
                {
                    "python-version": "3.10",
                    "django-version": "4.0",
                    "database": "postgres",
                },
                {
                    "python-version": "3.10",
                    "django-version": "4.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.10",
                    "django-version": "4.1",
                    "database": "mysql",
                },
                {
                    "python-version": "3.10",
                    "django-version": "4.1",
                    "database": "postgres",
                },
                {
                    "python-version": "3.10",
                    "django-version": "4.2",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.10",
                    "django-version": "4.2",
                    "database": "mysql",
                },
                {
                    "python-version": "3.10",
                    "django-version": "4.2",
                    "database": "postgres",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.0",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.0",
                    "database": "mysql",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.0",
                    "database": "postgres",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.1",
                    "database": "mysql",
                },
                {
                    "python-version": "3.10",
                    "django-version": "5.1",
                    "database": "postgres",
                },
                {
                    "python-version": "3.11",
                    "django-version": "4.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.11",
                    "django-version": "4.1",
                    "database": "mysql",
                },
                {
                    "python-version": "3.11",
                    "django-version": "4.1",
                    "database": "postgres",
                },
                {
                    "python-version": "3.11",
                    "django-version": "4.2",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.11",
                    "django-version": "4.2",
                    "database": "mysql",
                },
                {
                    "python-version": "3.11",
                    "django-version": "4.2",
                    "database": "postgres",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.0",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.0",
                    "database": "mysql",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.0",
                    "database": "postgres",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.1",
                    "database": "mysql",
                },
                {
                    "python-version": "3.11",
                    "django-version": "5.1",
                    "database": "postgres",
                },
                {
                    "python-version": "3.12",
                    "django-version": "4.2",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.12",
                    "django-version": "4.2",
                    "database": "mysql",
                },
                {
                    "python-version": "3.12",
                    "django-version": "4.2",
                    "database": "postgres",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.0",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.0",
                    "database": "mysql",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.0",
                    "database": "postgres",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.1",
                    "database": "mysql",
                },
                {
                    "python-version": "3.12",
                    "django-version": "5.1",
                    "database": "postgres",
                },
                {
                    "python-version": "3.13",
                    "django-version": "5.1",
                    "database": "sqlite",
                },
                {
                    "python-version": "3.13",
                    "django-version": "5.1",
                    "database": "mysql",
                },
                {
                    "python-version": "3.13",
                    "django-version": "5.1",
                    "database": "postgres",
                },
            ],
        ),
        (
            # https://github.com/fabiocaccamo/create-matrix-action/issues/7
            """
            python-version {3.8-1},              command {python3 --version}
            python-version {3.9-2.1},            command {python3 --version}
            python-version {custom-3.10},        command {python3 --version}
            python-version {3.11-custom},        command {python3 --version}
            python-version {custom-3.12-custom}, command {python3 --version}
            """,
            [
                {
                    "python-version": "3.8-1",
                    "command": "python3 --version",
                },
                {
                    "python-version": "3.9-2.1",
                    "command": "python3 --version",
                },
                {
                    "python-version": "custom-3.10",
                    "command": "python3 --version",
                },
                {
                    "python-version": "3.11-custom",
                    "command": "python3 --version",
                },
                {
                    "python-version": "custom-3.12-custom",
                    "command": "python3 --version",
                },
            ],
        ),
    ],
)
def test_parse_matrix_with_empty_string(input_matrix, expected_output_matrix):
    output_matrix = parse_matrix(input_matrix)
    try:
        assert output_matrix == expected_output_matrix
    except AssertionError:
        # print(output_matrix)
        raise


if __name__ == "__main__":
    pytest.main()
