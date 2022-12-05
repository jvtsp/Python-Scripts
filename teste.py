

# def hosts(ip,hostname):
#     print('Entrada do arquivo Hosts ' + ip + ' '+ hostname )
# with open('dns_novo', 'r') as re:
#     data = re.read()
#     for j in range(len(data.split('\n'))):
#         linha = data.split('\n')[j]
#         ip = linha.split(':')[0]
#         hostname = linha.split(':')[1]
#         hostname1 = hostname.split(',')[1]
#         hosts(ip,hostname1)
'''127.0.0.1   localhost
192.168.0.20    server.com
198.0.101.1    google.comm
'''
def hosts(ip,hostname):   
    print("---------")
    print("IP " + ip_hosts)
    print("Hosts " + hostname_hosts)

contador = 1

with open('hosts_test', 'r') as ho:
    data1 = ho.read()
for j in range(len(data1.split('\n'))):
    linha = data1.split('\n')[j]
    try:
        ip_hosts = linha.rstrip()
        hostname_hosts = linha.split(' ')[1]
        print(ip_hosts)
    except Exception as e:
        print(e)


# with open('hosts_test', 'r') as ho:
#     data1 = ho.read()
# for j in range(len(data1.split('\n'))):
#     linha = data1.split('\n')[j]
#     try:
#         ip_hosts = linha.split(' ')[0]
#         hostname_hosts = linha.split(' ')[1]
#         contador += 1
#         hosts(ip_hosts,hostname_hosts)
#     except:
#         print("Error")


