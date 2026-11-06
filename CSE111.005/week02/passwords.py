
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

def word_has_character(word, character_list):
    for ch in word:
        if ch in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit = "0123456789"
    special_char = "!@#$%^&*"
    func_call_1 = word_has_character(word, lower_case)
    func_call_2 = word_has_character(word, upper_case)
    func_call_3 = word_has_character(word, digit)
    func_call_4 = word_has_character(word, special_char)
    if func_call_1:
        complexity += 1
    if func_call_2:
        complexity += 1   
    if func_call_3:
        complexity += 1
    if func_call_4:
        complexity += 1
    return complexity
