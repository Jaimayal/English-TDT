import random


def random_paragraph(level):
    file_level = level + 'Paragraphs.txt'

    with open(file_level, 'r') as file:
        text = file.read()
        paragraphs = text.split('\n\n')
        random_index = random.randrange(0, len(paragraphs) - 1)
        return paragraphs[random_index]
