def read_dictionary(filename, length):
    f= open(filename,"r")
    words = []
    for lines in f:
        line = lines.strip()
        if len(line) == length:
            up = 0
            for i in line:
                if i.isupper():
                    up+=1
            if up == 0 and "'" not in line:
                words.append(line)
    # your code here
    return words # a list of the words in the dictionary which comprise only lower case letters and are of the correct length