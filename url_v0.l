%{
#include "y.tab.h"
#include <string.h>

int yywrap(void) { return 1; }
%}

%option noyywrap

COLON          ":"
SLASH          "/"
DOT            "."
LBRACKET       "\\["
RBRACKET       "\\]"
HTTP           "http"
HTTPS          "https"
FTP            "ftp"
IP_OCTET       [0-9]{1,3}
HEXSEG         [0-9a-fA-F]{1,4}
NUMBER         [0-9]+
NAME           [a-zA-Z_][a-zA-Z0-9_\-]*

%%

{HTTP}         { return HTTP; }
{HTTPS}        { return HTTPS; }
{FTP}          { return FTP; }

{COLON}        { return ':'; }
{SLASH}        { return '/'; }
{DOT}          { return '.'; }
{LBRACKET}     { return '['; }
{RBRACKET}     { return ']'; }

{IP_OCTET}     { yylval = strdup(yytext); return IP_OCTET; }
{HEXSEG}       { yylval = strdup(yytext); return HEXSEG; }
{NUMBER}       { yylval = strdup(yytext); return NUMBER; }
{NAME}         { yylval = strdup(yytext); return A; }

[ \t\r\n]+     { /* skip whitespace */ }

.              { return yytext[0]; }

