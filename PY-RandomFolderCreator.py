import os
import random
import string
import socket

PcName = socket.gethostname()
Directory = "/home/kali/Desktop/"
counter = 0

for _ in range(6):
    counter += 1
    randomizer = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    FullDirectory = os.path.join(Directory, randomizer)
    
    if not os.path.exists(FullDirectory):
        os.makedirs(FullDirectory)
        
        with open(os.path.join(FullDirectory, "UPOZORNENIE.txt"), "w") as file:
            file.write("\n" + "+ " + "-"*60 + " +" + "\n")
            file.write("   Vas Pocitac menom: '" + PcName + "' je v NEBEZPECENSTVE" + "\n")
            file.write("   Prosim Restartujte Vas Pocitac a bude to v poriadku" + "\n")
            file.write("+ " + "-"*60 + " +" + "\n")
