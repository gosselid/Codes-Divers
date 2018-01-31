from serial import Serial
from time import sleep


print("programme lance")


board = Serial()
board.baudrate = 9600
board.port = "COM5"


sleep(0.01)

try:
    board.open()
except:
    print("Connection impossible")

sleep(3)
quitter = False

if board.is_open:
    print("Arduino Connecte")
    while (not quitter):

        sig = input("1 pour allumer, 0 pour eteindre, 2 pour quitter : ")
        print(sig)
        if(sig=='1' or sig=='0'):
            board.write(bytes(sig.encode()))
            val = board.read(6)
            print("Etat:")
            print(val.decode())
        elif (sig=='2'):
            quitter = True
