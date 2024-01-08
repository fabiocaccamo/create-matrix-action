[![](https://img.shields.io/github/actions/workflow/status/fabiocaccamo/create-matrix-action/test-action.yaml?branch=main&label=build&logo=github)](https://github.com/fabiocaccamo/create-matrix-action)
[![](https://img.shields.io/github/stars/fabiocaccamo/create-matrix-action?logo=github&style=flat)](https://github.com/fabiocaccamo/create-matrix-action/stargazers)
[![](https://img.shields.io/github/sponsors/fabiocaccamo?color=blueviolet&logo=github)](https://github.com/sponsors/fabiocaccamo)
[![](https://img.shields.io/twitter/follow/fabiocaccamo)](https://twitter.com/fabiocaccamo)


# create-matrix-action

This action creates a non-square matrix from parsing a matrix configuration declared in the workflow file.

I wrote this action for my python/django testing needs, but it is very flexible and scalable, so it can be used in many other contexts.

## Matrix configuration

Example:
```
python-version {3.8}, django-version {3.0,3.1,3.2,4.0,4.1}, database {sqlite,mysql,postgres}
python-version {3.9}, django-version {3.0,3.1,3.2,4.0,4.1}, database {sqlite,mysql,postgres}
python-version {3.10}, django-version {3.2,4.0,4.1}, database {sqlite,mysql,postgres}
python-version {3.11}, django-version {4.1}, database {sqlite,mysql,postgres}
```

> **Note:** *In the above example, `python-version`, `django-version` and `database` are just the matrix variable names that we can access in the following step, so it is possible to name these variables as needed.*

## Workflow

Example:
```yaml
# ...

jobs:

  prepare:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout code
        uses: actions/checkout@v2

      - name: Create matrix
        id: create_matrix
        uses: fabiocaccamo/create-matrix-action@v3
        with:
          matrix: |
            python-version {3.8}, django-version {3.0,3.1,3.2,4.0,4.1}, database {sqlite,mysql,postgres}
            python-version {3.9}, django-version {3.0,3.1,3.2,4.0,4.1}, database {sqlite,mysql,postgres}
            python-version {3.10}, django-version {3.2,4.0,4.1}, database {sqlite,mysql,postgres}
            python-version {3.11}, django-version {4.1}, database {sqlite,mysql,postgres}

    outputs:
      matrix: ${{ steps.create_matrix.outputs.matrix }}

  test:

    needs: prepare
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        include: ${{fromJson(needs.prepare.outputs.matrix)}}

    # ...

    steps:

      # ...

      - name: Debug matrix
        run: |
          echo "Python ${{ matrix.python-version }} + Django ${{ matrix.django-version }} + Database ${{ matrix.database }}"
```

Check the full [test-action.yaml](https://github.com/fabiocaccamo/create-matrix-action/blob/main/.github/workflows/test-action.yaml) workflow file.

---

## License
Released under [MIT License](LICENSE).
