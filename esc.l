
ESC      (\\([\"bfnrt]))
STRING   (\"({ESC})\")


%%
{STRING} {ACCEPT;}
%%
