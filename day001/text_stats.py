def analyse_text(text: str)->dict:
    """
    A function that accepts text and returns three counts
        Args text (str)
        Return dict
    """
    lines = 0
    words = text.split()
    word_count = len(words)
    characters = len(text)
    for character in text:
        if '\n' == character:
            lines += 1
    return {"lines": lines, "words": word_count, "characters": characters}

if __name__ == "__main__":
    print(analyse_text("A\r\nB\r\n"))