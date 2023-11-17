#!/usr/bin/env python3

import socket
import sys

final = []







class Assets:
    def __init__(self, text_file):
        for n in text_file:
            try:
                print(socket.gethostbyname(n), n, sep = ' :    \t')
                write_file = open("./livehosts.txt", "a")
                
                write_file.write(socket.gethostbyname(n)+' : \t'+ n + '\n')
                write_file2 = open("./live_IPs.txt","a")
                write_file2.write(socket.gethostbyname(n)+'\n')




            except:
               print("Hostname Not Live : ", '\t', n)
               continue



txt_file = open(sys.argv[1], "r")
content_list = txt_file.readlines()

for i in  content_list:
        final.append(i.strip())
Assets(final)




# Open file with filename as argument
#usage: python3 resolve.py filename


# Read all the lines or subdomains in the file
#Create a list called final


#Add contents of file to the list final




'''
for n in final:
    try:
        print(socket.gethostbyname(n), n, sep = '       \t')

# Create a file called livehosts and add the resolvable hosts to the file

        write_file = open("./livehosts", "a")
        write_file.write(socket.gethostbyname(n)+' : \t'+ n + '\n')

    except:
        print("Hostname Not Live : ", '\t', n)
        continue

'''
