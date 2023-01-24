#!/usr/bin/env python3
# hoster-toaster.py
# Purpose: Update a machine's local hostname resolution file
#
# USAGE: ./hoster-toaster.py
#
# Author: * Renata Dos Santos *
# Date: * 08/01/2022 *

import os, sys, socket
from python_hosts import Hosts
import argparse

#hosts_file = '/etc/hosts'

hosts = Hosts(path='hosts_test')
hosts_file = 'hosts_test'


argumentos = len(sys.argv)
try:
    if len(sys.argv) == 2:
        argumento1 = str(sys.argv[1])
        with open(argumento1, 'r') as re:
            data = re.read()
        with open(hosts_file, 'w') as f:
            f.write(data)
            print("Entradas adicionadas")
            print (data)
    if len(sys.argv) >= 3:
        argumento2 = str(sys.argv[2])
        if argumento2 == '-s':
            argumento1 = str(sys.argv[1])
            print(argumento2)
            print("Entradas adicionadas")
            hosts.import_file(argumento1)
            hosts.write()
        elif argumento2 == '-c':   
            print(argumento2)
    if len(sys.argv) == 1:
        print('#'*40)
        print("Não se esqueça de informar os argumentos")
        print('#'*40)
except Exception as e: 
    print(e)
