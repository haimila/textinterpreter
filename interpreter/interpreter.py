def lines_into_list(tiedosto):
    with open(str(tiedosto)) as file:
        file_contents = file.read()

    lines_in_list = file_contents.split("\n")

    no_line_breaks = " ".join(lines_in_list)

    individual_words = no_line_breaks.split(" ")
    individual_words.pop()

    individual_words.sort(key=lambda x: (len(x), x))
    return individual_words


def write_to_file(tiedosto):

    new_file = open("uusitesti.txt", "w+")

    for word in tiedosto:
        new_file.write(word)
        new_file.write("\n")

    new_file.close()

try:
    write_to_file(lines_into_list("Latin-Lipsum.txt"))

except:
    print("File not found, try again!")












