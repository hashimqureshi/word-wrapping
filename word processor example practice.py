def wordWrapping(string, width):

    text = string.split()
    for word in text:
        if len(word) + len(text[text.index(word)-len(text)+1]) <= width:
            print(word + " " +text[text.index(word)-len(text)+1])
        elif len(word) > width:
            for numberOfCharacters in range(0, len(word), width):
                print(word[numberOfCharacters:numberOfCharacters+width])
        elif len(word) == width:
            print(word)



wordWrapping("Superlongword and is longword longerword otherword is shorter", 8)