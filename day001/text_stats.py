"""
A function that accepts text and returns three counts
    Args text (str)
    Return dict
"""
def analyse_text(text):
    lines = 0
    words = text.split()
    print('words', words)
    word_count = len(words)
    characters = len(text)
    for i in text:
        if '\n' in i:
            lines += 1
    return {"lines": lines, "words": word_count, "characters": characters}

print(analyse_text("A\r\nB\r\n"))