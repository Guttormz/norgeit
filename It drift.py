import platform
import shutil
import os
import socket
import subprocess


brukernavn = os.getlogin() #Finner brukernavnet på personen som er logget inn på pc-en
Os = platform.system() #Viser hvilket operativsystem pc-en bruker
OsVer = platform.platform() #Finner hvilken versjon av operativsystemet pc-en bruker
totalt, brukt, ubrukt = shutil.disk_usage("/") #Gir en verdi til 3 forskjellige variabler, basert på hvor mye plass det er på pc-en. Uansett hva som står kommer det til å gå i rekkefølgen av: Totlat hvor mye plass som er på pc-en, hvor mye som er brukt, og hvor mye som er ledig.
hostname = socket.gethostname() #Finner navnet på pc-en
Ip = socket.gethostbyname(hostname) #Finner IP-en på pc-en
prog = subprocess.check_output(['wmic', 'product', 'get', 'name']) #Finner alt maskinvare som er lastet ned
a=str(prog) #Gjør om variabelen over til ett string

if FileExistsError == False: #Sjekker om det kommer en FileExistError eller ikke. Om det kommer en, så lager den ikke en ny fil og hopper rett til write, og hvis den er false, så blir det laget en ny fil.
    file = open(hostname + ".txt", 'x') #Lager en fil med samme navn som pc-en.
else:
    fil = open(hostname + ".txt", 'w') #Åpner filen i write, sånn at jeg kan putte tekst inn i den

fil.write("----------Pc informasjon---------- \n") #All fil.write putter tekst inn i .txt filen som ble lagd over.
fil.write("Brukernavnet er: " + brukernavn + "\n")
fil.write("OS: " + Os + "\n")
fil.write("OS versjon: " + OsVer + "\n \n")

fil.write("----------Diskplass informasjon---------- \n")
fil.write("Totalt: %d GB" % (totalt // (2**30)) + "\n") #%d er en placeholder for ett tall, og % er hvor mye plass det er på pc-en, i byte, som er gurnnen til at jeg deler det på 2^30 for å gjøre det om til Gigabyte
fil.write("Brukt: %d GB" % (brukt // (2**30)) + "\n")
fil.write("Ubrukt: %d GB" % (ubrukt // (2**30)) + "\n \n")

fil.write("----------IP informasjon---------- \n")
fil.write("IP adressen er: " + Ip + "\n \n")

fil.write("----------Installert programvare---------- \n")
try:
    for i in range(len(a)): #Gir i en egen verdi basert på lengden på a, og kjører koden en gang per lengde
        fil.write((a.split("\\r\\r\\n")[6:][i])+"\n") #Skriver inn a som en liste der hvert ord er ett eget ord i lista.
except IndexError as e: #Når du får IndexError betyr det at koden prøver å finne en index som ikke eksisterer. Når dette skjer, så vil den kjøre koden under
    fil.write("Ferdig")
fil.close()