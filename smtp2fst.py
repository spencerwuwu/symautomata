#!/usr/bin/env python
from sys import argv
import networkx as nx
import string

from symautomata.flex2fst import Flexparser, mma_2_digraph

# https://en.wikipedia.org/wiki/List_of_Unicode_characters
def get_common_unicode():
    basic_latin = list(range(0x00, 0x7E+1))
    return [chr(a) for a in basic_latin]
    #return  list(string.ascii_letters) + \
    #        list(string.digits) + \
    #        list(":/@#?=+-_.%&<>\"") + \
    #        list("\r\n \t")

    #return basic_latin + new_lines

def main():
    """
    Testing function for Flex Regular Expressions to FST DFA
    """
    if len(argv) < 2:
        print('Usage: %s fst_file' % argv[0])
        return
    flex_a = Flexparser(get_common_unicode())
    mma = flex_a.yyparse(argv[1])

    print("---")
    print(mma)
    model_name = "model_" + argv[1].replace('.', '_')
    mma.save(model_name + ".txt")

    print("---")
    request = "EHLO smtpgarden\r\nMAIL FROM:<root@google.com>\r\nRCPT TO:<user1@echo.smtp.garden>\r\nDATA\r\nHEADxxxTAIL\r\n\r\n.\r\nQUIT\r\n"

    print("T", mma.consume_input(request))

if __name__ == '__main__':
    main()
