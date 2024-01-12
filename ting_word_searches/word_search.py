def exists_word(word, instance):
    result = instance.queue
    occurrences_list = list()

    for file_info in result:
        file_name = file_info["nome_do_arquivo"]
        file_lines = file_info["linhas_do_arquivo"]

        file_occurrences = list()

        for line_number, line in enumerate(file_lines, start=1):
            if word.lower() in line.lower():
                file_occurrences.append({"linha": line_number})

        if file_occurrences:
            occurrences_list.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": file_occurrences,
                }
            )

    return occurrences_list


def search_by_word(word, instance):
    result = instance.queue
    occurrences_list = list()

    for file_info in result:
        file_name = file_info["nome_do_arquivo"]
        file_lines = file_info["linhas_do_arquivo"]

        file_occurrences = list()

        for line_number, line in enumerate(file_lines, start=1):
            if word.lower() in line.lower():
                file_occurrences.append(
                    {"linha": line_number, "conteudo": line}
                )

        if file_occurrences:
            occurrences_list.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": file_occurrences,
                }
            )

    return occurrences_list
