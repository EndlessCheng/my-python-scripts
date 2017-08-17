# -*- coding: utf-8 -*-

import re

import markdown2
from bs4 import BeautifulSoup

html_body_content = markdown2.markdown_path("help.md")
html = ''.join(['<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">',
                '<link rel="stylesheet" type="text/css" href="base_common.css">',
                '<link rel="stylesheet" type="text/css" href="markdownpad-github.css">',
                '<title>Title</title></head><body>' + html_body_content + '</body></html>'])

soup = BeautifulSoup(html, "html.parser")
for h_soup in soup.find_all(re.compile(r'h\d+')):
    h_soup['id'] = h_soup.text.lower().replace(' ', '-')

with open("help.html", 'w') as f:
    html = soup.prettify().encode('utf-8')
    f.write(html)
