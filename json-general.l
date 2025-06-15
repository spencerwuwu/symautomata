
INT      ([0]|[1-9][0-9]*)
EXP      ([Ee][+-]?[0-9]+)
         
NUMBER   (-?{INT}(.([0-9])+)?)({EXP})?
HEX      ([0-9a-fA-F])
UNICODE  (u{HEX}{HEX}{HEX}{HEX})
ESC      (\\(([\"bfnrt])|({UNICODE})))
STRING   (\"({ESC})+\")


%%
{STRING} {ACCEPT;}
%%
