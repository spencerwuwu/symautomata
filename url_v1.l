
PROTOCOL     http|https|ftp
PORT         :[0-9]+
PATH         \/[a-zA-Z0-9_\-\.]*

%%
{PROTOCOL}:\/\/[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+({PORT})?({PATH})* {ACCEPT;}
%%

