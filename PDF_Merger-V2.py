#
# PDF Merger-V2 (5/15-16/2023)
# Isaac B. Ernst
#

import os
from PyPDF4 import PdfFileMerger

files_order = []
page_order = []


class Command:
    positive = ['yes', 'y', 'yep']

    def __init(self):
        pass

    def check(self):
        correct = input('$ Correct? ').lower()
        return True if correct in self.positive else False

    def merge(self, filename) -> None:
        global files_order, page_order
        try:
            if not os.path.isfile(filename + '.pdf'):
                raise FileNotFoundError
            pagerange = input(f'$ Enter the pages to merge (e.g. 1-4 or 5): ').split(',')
            if self.check():
                page_order.append(pagerange)
                files_order.append(filename + '.pdf')
                print('Merge successful.')
            else:
                print('Merge stopped.')
        except FileNotFoundError:
            print('File not found.')

    @staticmethod
    def execute() -> None:
        try:
            merge = PdfFileMerger()
            for (file, pages) in zip(files_order, page_order):
                for page in pages:
                    if '-' in page:
                        start, end = map(int, page.split("-"))
                        merge.append(file, pages=(start - 1, end))
                    else:
                        page = int(page)
                        merge.append(file, pages=(page, page))
            merge.write('merged_file.pdf')
            merge.close()
            print('PDFs merged successfully.')
        except TypeError:
            print('Invalid input.')

    @staticmethod
    def clear() -> None:
        global files_order, page_order
        files_order = []
        page_order = []


def run_command(command) -> None:
    match command.split():
        case ['merge']:
            print('No file name given.')
        case ['merge', filename]:
            Command().merge(filename)
        case ['quit' | 'exit' | 'bye']:
            print('Quitting the program.')
            quit()
        case ['clear' | 'reset']:
            Command().clear()
            print('Clearing data.')
        case ['execute']:
            Command().execute()
            print('Merging pdfs.')
            quit()
        case _:
            print(f'Unknown command: {command!r}')


def main() -> None:
    """Main function."""
    commands = ['Commands:',
                '   merge (ex: merge {filename}, 1-4 or 5)',
                '   quit (exit and/or bye)',
                '   clear (clears current list of pdfs)',
                '   execute (combine pdfs in given order)',
                ]
    for val in commands:
        print(val)
    while True:
        command = input('$ ')
        run_command(command)


if __name__ == '__main__':
    main()
