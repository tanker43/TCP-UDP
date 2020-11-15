#Zach Grasso
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8080              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #using s for simplicity bind and connect with a client TCP
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            #Get usrinput from client
            usrInput = conn.recv(2048).decode()
            if not usrInput: break

            #splices and sets up for calculations
            usable = usrInput.split(" ")
            loan = int(usable[2].replace(",", "")[1:])
            time = int(usable[3])
            rate = float(usable[4].replace("%",""))

            #Begin transition for calculations
            period_rate = rate/100/12
            num_payments = time *12

            #Calculations being made and ready to ship
            monthly = period_rate*loan / (1 - (1 + period_rate) ** -num_payments)
            monthly = float("{0:.2f}".format(monthly))
            yearly = (monthly *12)

            #Encoded and shipped back to client
            conn.send(bytes(str(loan), encoding= 'utf-8'))
            conn.send(bytes(str(monthly), encoding= 'utf-8'))
            conn.send(bytes(str(yearly), encoding= 'utf-8'))
            
            conn.close