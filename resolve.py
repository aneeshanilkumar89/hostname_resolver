#!/usr/bin/env python3

import socket

txt_file = open("/path/to/file/assets.txt", "r")
content_list = txt_file.readlines()
final= []
for i in  content_list:
        final.append(i.strip())

for n in final:
    try:
        print(socket.gethostbyname(n), n, sep = '       \t')
        txt_file2.write(socket.gethostbyname(n)+' : \t'+ n + '\n')
    except:
        print("Hostname Not Live : ", '\t', n)
        continue

