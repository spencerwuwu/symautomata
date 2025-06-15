#!/usr/bin/env python
from sys import argv
import networkx as nx
import string

from symautomata.flex2fst import Flexparser, mma_2_digraph, simplify_digraph
from symautomata.flex2fst import mma_trace_2_digraph

# https://en.wikipedia.org/wiki/List_of_Unicode_characters
def get_common_unicode():
    #return ['\\', '\n', "n", '\"', "b"]
    return  list(string.ascii_letters) + \
            list(string.digits) + \
            list(":/@#?=+-_.%&\\")

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


    graph = mma_2_digraph(mma)
    graph = simplify_digraph(graph, mma)

    p = nx.nx_pydot.to_pydot(graph)
    p.write_png(model_name + ".png")

    print("---")
    with open("input.txt", "r") as fd:
        i = fd.read()[:-1]
        #print(i, len(i))
    print(mma.consume_input(i))

    colors = [
            "aqua",
            "blue",
            "bisque",
            "brown",
            "chartreuse",
            "crimson",
            "darkorchid",
            "deeppink",
            "tomato",
            "lime",
            "orange",
            "cyan",
            "fuchsia",
            "gold"
            ]


if __name__ == '__main__':
    main()
