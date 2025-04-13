S: A main
main: url

url: protocol "://" host port_opt path_opt

protocol: "http" | "https" | "ftp"

host: domain | ipv4

domain: label ("." label)+
label: name

ipv4: number "." number "." number "." number

port_opt: ":" number | ε

path_opt: "/" path | ε

path: segment ("/" segment)*
segment: name

number: DIGIT+
name: CHAR+

DIGIT: [0-9]
CHAR: [a-zA-Z0-9_\-]

