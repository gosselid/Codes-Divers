from serial import Serial
from time import sleep


print("programme lance")


board = Serial()
board.baudrate = 9600
board.port = "COM7"


sleep(0.01)

try:
    board.open()
except:
    print("Connection impossible")

sleep(3)

if board.is_open:
    print("Arduino Connecte")
    while 1:
        print("______")
        print("liste des commandes")
        print("pin 13: a0/a1 pour allumer/éteindre")
        print("pince: p0/p1 pour allumer/éteindre")
        print("Q pour quitter")
        sig = input("saisir la commande: ")
        if sig=="Q":
        	exit(0)
        board.write(bytes(sig.encode()))
        #sleep(5)
        val = board.read(7)
        print(val.decode())
        val = board.read(7)
        print(val.decode())
