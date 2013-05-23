import re
import ez_epub

def parseBook(path, startLineNum, endLineNum):
    PATTERN = re.compile(r'Capitulo \d+$')
    sections = []
    paragraph = ''
    fin = open(path)
    lineNum = 0
    for line in fin:
        lineNum += 1
        if lineNum < startLineNum:
            continue
        if endLineNum > 0 and lineNum > endLineNum:
            break
        line = line.strip()
        if PATTERN.match(line):
            section = ez_epub.Section()
            section.title = line
            sections.append(section)
        elif line == '':
            if paragraph != '':
                section.text.append(paragraph)
                paragraph = ''
        else:
            if paragraph != '':
                paragraph += ' '
            paragraph += line
    if paragraph != '':
        section.text.append(paragraph)
    return sections
'''
if __name__ == '__main__':
    book = ez_epub.Book()
    book.title = 'Prueba'
    book.authors = ['Jane Austen']
    book.sections = parseBook(r'temp.txt', 1, 100)
    book.make(r'%s' % book.title)
'''
