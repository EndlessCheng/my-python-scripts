# -*- coding: utf-8 -*-
__author__ = 'Endless'

import re
import string


class Lexer:
    def __init__(self, file_name):
        self.file = open(file_name)

    def read_line(self):
        for line in self.file.readlines():
            for m in re.compile(r"\s*("
                                r"(//.*)|"  # commit
                                r"([0-9]+)|"  # number
                                r"(\"(\\\"|\\\\|\\n|[^\"])*\")|"  # string
                                r"[A-Z_a-z][A-Z_a-z0-9]*|"
                                r"<=|==|>=|&&|\|\||[%s])" % re.escape(string.punctuation)).findall(line):
                yield m  # .decode('string-escape')
        yield (r'\n', r'', r'', r'', r'')
