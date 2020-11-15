#Zach Grasso
from socket import *

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8080              # Arbitrary non-privileged port
serversocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind((HOST, PORT))
while True:
    loan, clientAddress  = serversocket.recv(1024).decode()
    time, clientAddress  = serversocket.recv(1024).decode()
    rate, clientAddress  = serversocket.recv(1024).decode()
    if not usrInput: break



    period_rate = rate/100/12
    num_payments = time *12

    monthly = period_rate*loan / (1 - (1 + period_rate) ** -num_payments)
    monthly = float("{0:.2f}".format(monthly))
    yearly = (monthly *12)

    conn.sendto(bytes(str(loan), encoding= 'utf-8'), addr)
    conn.sendto(bytes(str(monthly), encoding= 'utf-8'), addr)
    conn.sendto(bytes(str(yearly), encoding= 'utf-8'), addr)
    
    conn.close