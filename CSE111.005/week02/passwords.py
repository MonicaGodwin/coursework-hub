
# Handled empty password input

def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as file:
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
    special_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

    func_call_1 = word_has_character(word, lower_case)
    func_call_2 = word_has_character(word, upper_case)
    func_call_3 = word_has_character(word, digit)
    func_call_4 = any(word_has_character(word, char)for char in special_char)

    if func_call_1:
        complexity += 1
    if func_call_2:
        complexity += 1   
    if func_call_3:
        complexity += 1
    if func_call_4:
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    if password == "":
        print("password cannot be empty")
        return 0
    
    if word_in_file(password, "wordlists.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0
        
    elif word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    func_call = word_complexity(password)

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    elif len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    else:
        score = 1 + func_call

        if score == 2:
            print("Password is weak")
        elif score == 3:
            print("Password has moderate strength")
        elif score == 4:
            print("Password is strong")
        elif score == 5:
            print("Password is very strong.")
        return score

def main():
    while True:
        user_input = input("Enter a password to check how secured it is: ")
        if user_input == "q" or user_input == "Q":
            return
        else:
            print(word_complexity(user_input))
            strength = password_strength(user_input)
        print(f"Password strength: {strength}/5")
if __name__ == "__main__":
    main()
