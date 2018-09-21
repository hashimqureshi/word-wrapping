def wordWrapping(string, width):
    lines = []
    for text in string.split('\n'):
        line = []
        len_line = 0
        for word in text.split(' '):
            len_word = len(word)
            if len_line + len_word <= width:
                line.append(word)
                len_line += len_word + 1
            elif len(word) > width:
                for numberOfCharacters in range(0, len(word), width):
                    print(word[numberOfCharacters:numberOfCharacters+width])
            else:
                lines.append(' '.join(line))
                line = [word]
                len_line = len_word + 1
        lines.append(' '.join(line))
    return '\n'.join(lines)
print(wordWrapping("Superlongword and is longword longerword otherword is shorter", 8))