import random


def random_paragraph(level):
    fileLevel = level + 'Paragraphs.txt'

    with open(fileLevel, 'r') as file:
        text = file.read()
        paragraphs = text.split('\n\n')
        randomIndex = random.randrange(0, len(paragraphs) - 1)
        return paragraphs[randomIndex]