import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise ValueError("Formato inválido")

        with open(path_file, "r") as file:
            list_of_files = [line.rstrip() for line in file.readlines()]
            return list_of_files

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    except ValueError as e:
        print(e, file=sys.stderr)
