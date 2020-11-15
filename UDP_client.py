#Zach Grasso
from socket import *


HOST = 'localhost'    # The remote host
PORT = 8080              # The same port as used by the server

clientSocket = socket(AF_INET, SOCK_DGRAM)
#Get usrinput
usrInput = ""
usrInput = input("Enter in Cal server name along with loan amount, years, and rate ")
if usrInput == "":
    pass

#splices and sets up for calculations
usable = usrInput.split(" ")
loan = int(usable[2].replace(",", "")[1:])
time = int(usable[3])
rate = float(usable[4].replace("%",""))

#encode and ship to host
clientSocket.sendto((bytes(str(loan), encoding= 'utf-8')), (HOST, PORT))
clientSocket.sendto((bytes(str(time), encoding= 'utf-8')), (HOST, PORT))
clientSocket.sendto((bytes(str(rate), encoding= 'utf-8')), (HOST, PORT))

#reveive from host
loan, HOST = clientSocket.recvfrom(1024)
monthly, HOST = clientSocket.recvfrom(1024)
yearly, HOST = clientSocket.recvfrom(1024)

#print functions
print("$" + loan.decode() + " loan")
print("monthly payment is $" + monthly.decode())
print("total payment is $" + yearly.decode())

clientSocket.close