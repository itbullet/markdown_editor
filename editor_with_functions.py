def get_text():
    return input("Text: ")


def plain():
    return get_text()


def bold():
    return f"**{get_text()}**"


def italic():
    return f"*{get_text()}*"


def link():
    label = input("Label: ")
    url = input("URL: ")

    return f"[{label}]({url})"


def inline_code():
    return f"`{get_text()}`"


def new_line():
    return "\n"


def header():
    while True:
        lvl = input("Level: ")
        if len(lvl) == 1 and lvl in "123456":
            break
        else:
            print("The level should be within the range of 1 to 6")

    return f"{'#' * int(lvl)} {get_text()}\n"


def unordered_list():
    return '\n'.join(list(map(lambda line: '*' + line[2:], general_list()))) + '\n'


def ordered_list():
    return '\n'.join(general_list()) + '\n'


def general_list():
    while True:
        n = int(input("Number of rows: "))
        if n > 0:
            break
        else:
            print("The number of rows should be greater than zero")
    return [f"{i}. {input(f'Row #{i}: ')}" for i in range(1, n + 1)]


def save_to_file():
    with open("output.md", 'w') as f:
        f.write(''.join(result))


formatters = {"plain": plain,
              "bold": bold,
              "italic": italic,
              "link": link,
              "inline-code": inline_code,
              "new-line": new_line,
              "header": header,
              "ordered-list": ordered_list,
              "unordered-list": unordered_list,
              }

result = []
while True:
    formatter = input("Choose a formatter: ")
    if formatter == "!done":
        save_to_file()
        break
    elif formatter == "!help":
        print(f"Available formatters: {' '.join(formatters.keys())}\nSpecial commands: !help !done")
    elif formatter not in formatters:
        print("Unknown formatter or command. Please try again.")
    else:
        result.append(formatters[formatter]())
        print(*result, sep='')
