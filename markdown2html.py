#!/usr/bin/python3
import sys


def ol_parse(index, lines_read_list):
    """Parses ordered list lines into HTML."""
    list_ol = ['<ol>\n']
    while index < len(lines_read_list):
        if lines_read_list[index][0] != '*':
            break
        data = lines_read_list[index].strip()
        string_to_parsing = data.lstrip("*").strip()
        list_ol.append(f'  <li>{string_to_parsing}</li>\n')
        index += 1
    list_ol.append('</ol>\n')
    return index, list_ol


def ul_parse(index, lines_read_list):
    """Parses unordered list lines into HTML."""
    list_ul = ['<ul>\n']
    while index < len(lines_read_list):
        if lines_read_list[index][0] != '-':
            break
        data = lines_read_list[index].strip()
        string_to_parsing = data.lstrip("-").strip()
        list_ul.append(f'  <li>{string_to_parsing}</li>\n')
        index += 1
    list_ul.append('</ul>\n')
    return index, list_ul


def heading_parse(index, lines_read_list):
    """Parses heading lines into HTML."""
    list_heading = []
    while index < len(lines_read_list):
        if lines_read_list[index][0] != '#':
            break
        data = lines_read_list[index].strip()
        heading_level = len(data) - len(data.lstrip('#'))
        if 1 <= heading_level <= 6:
            string_to_parsing = data.lstrip("#").strip()
            list_heading.append(f'<h{heading_level}>{string_to_parsing}</h{heading_level}>\n')
        index += 1
    return index, list_heading


funtion_parsing = {
    '#': heading_parse,
    '-': ul_parse,
    '*': ol_parse,
}

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        htmlTagList = []
        with open(input_file, 'r') as markdownFile:
            lines_read_list = markdownFile.readlines()
            index = 0
            while index < len(lines_read_list):
                line = lines_read_list[index].strip()
                if not line:
                    index += 1
                    continue
                first_char = line[0]
                if first_char in funtion_parsing:
                    index, htmlTag = funtion_parsing[first_char](index, lines_read_list)
                else:
                    htmlTag = [f'<p>{line}</p>\n']
                    index += 1
                htmlTagList.append(htmlTag)

        with open(output_file, 'w', encoding="utf-8") as html:
            for htmlLines in htmlTagList:
                for html_tag in htmlLines:
                    html.write(html_tag)
        sys.exit(0)

    except FileNotFoundError:
        sys.stderr.write(f'Missing {input_file}\n')
        sys.exit(1)
