
SCHEME      ([a-zA-Z][a-zA-Z0-9+.-]*)
LABEL       ([a-zA-Z0-9\-]+)
HOSTNAME    ({LABEL}(\.{LABEL})+)
IPV4        ([0-9]{1,3}(\.[0-9]{1,3}){3})
IPV6        (\[([0-9a-fA-F:]+)\])   
PORT         :[0-9]+
PATH        (\/[a-zA-Z0-9_\-\.%&]*)
QUERY       (\?[a-zA-Z0-9._~%!$&'()*+,;=:@/?-]*)
FRAGMENT    (\#[a-zA-Z0-9._~%!$&'()*+,;=:@/?-]*)

%%
{SCHEME}:\/\/({HOSTNAME}|{IPV4}|{IPV6})({PORT})?({PATH})*({QUERY})?({FRAGMENT})? {ACCEPT;}
%%

