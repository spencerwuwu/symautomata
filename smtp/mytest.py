#!/usr/bin/env python
from sys import argv
import networkx as nx
import string

from symautomata.flex2fst import Flexparser, mma_2_digraph, simplify_digraph

# https://en.wikipedia.org/wiki/List_of_Unicode_characters
def get_common_unicode():
    #basic_latin = list(range(0x00, 0x7E+1))
    #return [chr(a) for a in basic_latin]
    return  list(string.ascii_letters) + \
            list(string.digits) + \
            list(".<>@,:\\\"") + \
            list("!#$%&'*+/=?^_`{|}~-\r\n \t")

    #return basic_latin + new_lines

def get_base_unicode():
    basic_latin = list(range(0x00, 0x7E+1))
    return [chr(a) for a in basic_latin]


def main():
    """
    Testing function for Flex Regular Expressions to FST DFA
    """
    #if len(argv) < 2:
    #    print('Usage: %s fst_file' % argv[0])
    #    return
    filename = "addrspec.l"

    flex_a = Flexparser(get_base_unicode())
    mma = flex_a.yyparse(filename)

    print("---")
    print(mma)
    model_name = "model_b-" + filename.replace('.', '_')
    mma.save(model_name + ".txt")

    request = "root@google.com"
    print("T", mma.consume_input(request))

    request = "@router1,@router2:\"a+b=c\"@mail.host.net"
    print("T", mma.consume_input(request))

    #  ---------------------------------

    flex_a = Flexparser(get_common_unicode())
    mma = flex_a.yyparse(filename)

    print("---")
    print(mma)
    model_name = "model_" + filename.replace('.', '_')
    mma.save(model_name + ".txt")

    print("---")

    request = "root@google.com"
    print("T", mma.consume_input(request))

    request = "@router1,@router2:\"a+b=c\"@mail.host.net"
    print("T", mma.consume_input(request))

    graph = mma_2_digraph(mma)
    graph = simplify_digraph(graph, mma)
    p = nx.nx_pydot.to_pydot(graph)
    p.write_png(model_name + ".png")


if __name__ == '__main__':
    main()
