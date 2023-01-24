#!/usr/bin/env python3
# hoster-toaster.py
# Purpose: Update a machine's local hostname resolution file
#
# USAGE: ./hoster-toaster.py
#
# Author: * Renata Dos Santos *
# Date: * 08/01/2022 *

import sys

hosts_file = 'hosts_test'
argumentos = len(sys.argv)


def modify_host_argument_s(hostname_hosts,hostname):
    with open(hosts_file, 'r') as ho:
        data1 = ho.read()
    for j in range(len(data1.split('\n'))):
        linha = data1.split('\n')[j]
        try:
            filedata = data1.replace(hostname_hosts, hostname)
            with open(hosts_file, 'w') as ro:
                ro.write(filedata)
        except Exception as e:
            print(e)

def hosts_add_ip_hostname_s(ip,hostname):
    with open(hosts_file, 'r') as ho:
        data1 = ho.read()
    for j in range(len(data1.split('\n'))):
        linha = data1.split('\n')[j]
        try:
            ip_hosts = linha.split(' ')[0]
            hostname_hosts = linha.split(' ')[1]
        except Exception as e:
            print(e)
        if ip == ip_hosts:
            modify_host_argument_s(hostname_hosts,hostname)
        else:
            with open(hosts_file, 'w') as h1:
                data2 = (ip + ' ' + hostname_hosts)
                print(data2)
                #h1.write(data2)

                
            

try:
    if len(sys.argv) ==  2:
        argumento1 = str(sys.argv[1])
        with open(argumento1, 'r') as re:
            data = re.read()
        with open(hosts_file, 'w') as f:
            f.write(data)
            print("Entradas adicionadas")
            #print (data)
    if len(sys.argv) >= 3:
        argumento2 = str(sys.argv[2])
        if argumento2 == '-s':
            argumento1 = str(sys.argv[1])
            #Leitura do conteudo do argumento 1 
            with open(argumento1, 'r') as re:
                data = re.read()
                for j in range(len(data.split('\n'))):
                    linha = data.split('\n')[j]
                    ip = linha.split(':')[0]
                    hostname = linha.split(':')[1]
                    #hostname1 = hostname.split(',')[0]
                    #print(ip + " " +  hostname)
                    hosts_add_ip_hostname_s(ip,hostname)
        elif argumento2 == '-c':   
            print(argumento2)
        else:
            print("Parametro incorreto")
    if len(sys.argv) == 1:
        print('#'*40)
        print("Não se esqueça de informar os argumentos")
        print('#'*40)
except Exception as e: 
    print(e)

