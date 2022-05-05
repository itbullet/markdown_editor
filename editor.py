commands_formatters = {'formatters': ['plain', 'bold', 'italic', 'header', 'link', 'inline-code',
                                      'ordered-list', 'unordered-list', 'new-line'],
                       'commands': ['!help', '!done']}
markdown_text = ''
while True:
    usr_command = input("Choose a formatter: ")
    if usr_command not in commands_formatters['formatters'] and usr_command not in commands_formatters['commands']:
        print("Unknown formatting type or command")
    elif usr_command == '!help':
        print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n'
              'Special commands: !help !done')
    elif usr_command == '!done':
        with open('output.md', 'w') as file:
            file.write(markdown_text)
            break
    elif usr_command == 'header':
        while True:
            level = int(input('Level: '))
            if level > 6 or level < 1:
                print('The level should be within the range of 1 to 6')
            else:
                text = input('Text: ')
                if len(markdown_text):
                    markdown_text += f'\n' + level * f'#' + f' {text}\n'
                else:
                    markdown_text += level * f'#' + f' {text}\n'
                break
    elif usr_command == 'plain':
        text = input('Text: ')
        markdown_text += f'{text}'
    elif usr_command == 'bold':
        text = input('Text: ')
        markdown_text += f'**{text}**'
    elif usr_command == 'italic':
        text = input('Text: ')
        markdown_text += f'*{text}*'
    elif usr_command == 'inline-code':
        text = input('Text: ')
        markdown_text += f'`{text}`'
    elif usr_command == 'new-line':
        markdown_text += f'\n'
    elif usr_command == 'link':
        label_text = input('Label: ')
        url_text = input('URL: ')
        markdown_text += f'[{label_text}]({url_text})'
    elif usr_command == 'unordered-list' or usr_command == 'ordered-list':
        rows_number = 0
        while rows_number < 1:
            rows_number = int(input('Number of rows: '))
            print('The number of rows should be greater than zero')
        else:
            for i in range(1, rows_number+1):
                text = input(f'Row #{i}: ')
                if usr_command == 'unordered-list':
                    markdown_text += f'* {text}\n'
                else:
                    markdown_text += f'{i}. {text}\n'

    print(markdown_text)

