from serial import Serial
from time import sleep


print("programme lance")

# Parameter of the arduino board
board = Serial()
board.baudrate = 9600
board.port = "COM5"


sleep(0.01)

#Connection to the Adruino board
try:
    board.open()
except:
    print("Connection impossible")

sleep(3)
quitter = False

if board.is_open:#If connection is OK, let's work
    print("Arduino Connecte")
    while True:
        message="10" # Message to send
        board.write(bytes(message.encode()))  # Sending message

        toRead=board2.inWaiting() # Number of character  (sent by arduino) waiting to be read
        if toRead!=0: #If there is a message
            messageFromArd=board2.read(toRead) # Read the entire message

        print(val.decode(messageFromArd)) # Affiche le message reçu de l'arduino
