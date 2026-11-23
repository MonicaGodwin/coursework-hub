with open("province.txt", "rt") as file:
    file_content = []
    for item in file:
        stripped = item.rstrip("\n")
        if stripped == "AB":
            stripped = "Alberta"
        file_content.append(stripped)
    file_content.pop(0)
    file_content.pop(-1)
    if stripped == "Alberta":
        print(len(stripped))

        
    print(file_content)    