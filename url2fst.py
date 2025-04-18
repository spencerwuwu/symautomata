from sys import argv
import networkx as nx

from symautomata.flex2fst import Flexparser, mma_2_digraph
from symautomata.dfa import DFA

# https://en.wikipedia.org/wiki/List_of_Unicode_characters
def get_common_unicode():
    basic_latin = list(range(0x22, 0x7E+1))
    return [chr(a) for a in basic_latin]

    #return basic_latin + new_lines

def main():
    """
    Testing function for Flex Regular Expressions to FST DFA
    """
    if len(argv) < 2:
        print 'Usage: %s fst_file [optional: save_file]' % argv[0]
        return
    flex_a = Flexparser(get_common_unicode())
    mma = flex_a.yyparse(argv[1])

    print mma
    if len(argv) == 3:
        mma.save(argv[2]+".txt")

        graph = mma_2_digraph(mma)
        #p = nx.nx_pydot.to_pydot(graph)
        #p.write_png(argv[2] + '.png')

    print "F", mma.consume_input("aba")
    print "T", mma.consume_input("http://abcde.com/")
    print "F", mma.consume_input("aaaa://abcde.com/")
    print "T", mma.consume_input("http://abcde.com:88/")
    print "T", mma.consume_input("http://abcde.com:88/acf%123")

if __name__ == '__main__':
    main()
