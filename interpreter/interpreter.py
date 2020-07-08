def lines_into_list(tiedosto):
    with open(tiedosto) as file:
        file_contents = file.read()

    lines_in_list = file_contents.split("\n")

    no_line_breaks = " ".join(lines_in_list)

    individual_words = no_line_breaks.split(" ")
    individual_words.pop()

    sorted_list = sorted(individual_words, key=len)
    return sorted_list

print(lines_into_list("Latin-Lipsum.txt"))








