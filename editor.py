class Markdown:
    formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line']
    formatters_lists = ['ordered-list', 'unordered-list']

    def __init__(self):
        self.text = []

    def print_result(self):
        print(''.join(self.text))

    def help(self):
        print('Available formatters: ' + ' '.join(Markdown.formatters))
        print('Special commands: !help !done')

    def plain(self):
        entry = input('Text:')
        self.text.append(entry)

    def bold(self):
        entry = input('Text:')
        self.text.append('**' + entry + '**')

    def italic(self):
        entry = input('Text:')
        self.text.append('*' + entry + '*')

    def inline_code(self):
        entry = input('Text:')
        self.text.append('`' + entry + '`')

    def new_line(self):
        self.text.append('\n')

    def header(self):
        level = input('Level:')
        while True:
            try:
                level = int(level)
                if level in range(1, 7):
                    break
                else:
                    raise ValueError
            except ValueError:
                print('The level should be within the range of 1 to 6')
                level = input('Level:')

        entry = input('Text:')
        self.text.append('#' * level + ' ' + entry + '\n')

    def link(self):
        label = input('Label:')
        url = input('URL:')
        self.text.append('[' + label + '](' + url + ')')

    def mark_list(self, ordered):
        number_rows = input('Number of rows:')
        while True:
            try:
                number_rows = int(number_rows)
                if number_rows > 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('The number of rows should be greater than zero')
                number_rows = input('Number of rows:')

        for i in range(1, number_rows + 1):
            entry = input(f'Row #{i}:')
            point = f'{i}. ' if ordered else '* '
            self.text.append(point + entry + '\n')

    def start(self):

        while True:
            entry = input('Choose a formatter:')

            if entry == '!help':
                self.help()

            elif entry == '!done':
                file = open('output.md', 'w')
                file.writelines(self.text)
                file.close()
                exit()

            elif entry in Markdown.formatters:
                getattr(self, entry.replace('-', '_'))()
                self.print_result()

            elif entry in Markdown.formatters_lists:
                self.mark_list(entry == 'ordered-list')
                self.print_result()

            else:
                print('Unknown formatting type or command. Please try again.')


md = Markdown()
md.start()

