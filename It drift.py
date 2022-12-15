import platform
import shutil
import os
import socket
import subprocess


brukernavn = os.getlogin()
Os = platform.system()
OsVer = platform.platform()
totalt, brukt, ubrukt = shutil.disk_usage("/")
hostname = socket.gethostname()
Ip = socket.gethostbyname(hostname)
prog = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a=str(prog)

try:
    for i in range(len(a)):
        print("")
except IndexError as e:
    print("")

if FileExistsError == False:
    file = open(hostname + ".txt", 'x')
else:
    fil = open(hostname + ".txt", 'w')

fil.write("----------Pc informasjon---------- \n")
fil.write("Brukernavnet er: " + brukernavn + "\n")
fil.write("OS: " + Os + "\n")
fil.write("OS versjon: " + OsVer + "\n \n")

fil.write("----------Diskplass informasjon---------- \n")
fil.write("Totalt: %d GB" % (totalt // (2**30)) + "\n")
fil.write("Brukt: %d GB" % (brukt // (2**30)) + "\n")
fil.write("Ubrukt: %d GB" % (ubrukt // (2**30)) + "\n \n")

fil.write("----------IP informasjon---------- \n")
fil.write("IP adressen er: " + Ip + "\n \n")

fil.write("----------Installert programvare---------- \n")
try:
    for i in range(len(a)):
        fil.write((a.split("\\r\\r\\n")[6:][i])+"\n")
except IndexError as e:
    fil.write("Ferdig")
fil.close()