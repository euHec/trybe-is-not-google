import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if any(item["nome_do_arquivo"] == path_file for item in instance.queue):
        return None

    new_text = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(new_text),
        "linhas_do_arquivo": new_text,
    }

    instance.enqueue(new_dict)

    print(new_dict)


def remove(instance):
    try:
        result = instance.dequeue()
        print(f"Arquivo {result['nome_do_arquivo']} removido com sucesso")
    except IndexError:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
