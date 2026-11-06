
def word_in_file(word, filename, case_sensitive):
    with open(filename, "r") as file:
        for line in file:
            clean_line = line.strip()
            if case_sensitive:
                if word == clean_line:
                    return True
            else:
                if word.lower() == clean_line.lower():
                    return True
        return False

