#Zach Grasso
import socket


HOST = 'localhost'    # The remote host
PORT = 8080              # The same port as used by the server

while True:
    usrInput = ""
    usrInput = input("Enter in Cal server name along with loan amount, years, and rate ")
    if usrInput == "":
        s.close()
        break

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(usrInput.encode())
        loan = s.recv(1024)
        monthly = s.recv(1024)
        yearly = s.recv(1024)

    print("$" + loan.decode() + " loan")
    print("monthly payment is $" + monthly.decode())
    print("total payment is $" + yearly.decode())

