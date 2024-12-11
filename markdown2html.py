#!/usr/bin/python3

import sys
import os
import re

def markdown_to_html(markdown_text):
    # Basic conversion of Markdown to HTML
    html_text = markdown_text
    html_text = re.sub(r'^# (.*)', r'<h1>\1</h1>', html_text, flags=re.MULTILINE)
    html_text = re.sub(r'^## (.*)', r'<h2>\1</h2>', html_text, flags=re.MULTILINE)
    html_text = re.sub(r'^### (.*)', r'<h3>\1</h3>', html_text, flags=re.MULTILINE)
    html_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_text)
    html_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_text)
    return html_text

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, "r") as md_file:
        md_content = md_file.read()
        html_content = markdown_to_html(md_content)

    with open(output_file, "w") as html_file:
        html_file.write(html_content)

    sys.exit(0)
