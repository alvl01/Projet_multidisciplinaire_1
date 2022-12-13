command = []
import time
def create_sensor(nb):
    c = []
    for n in nb:
        a = []
        a.append(n // 9)
        a.append((n - a[0] * 9) // 3)
        a[0] = n - a[0] * 9 - a[1] * 3
        a.append(n // 9)
        for b in a:
            if b == 0:
                c.append("red")
            elif b == 1:
                c.append("green")
            else:
                c.append("blue")
            c.append("white")
    return c
with open("code.crickit") as f:
        for line in f:
            line = line[: line.find("#")].strip()
            print(line)
            indice = 0
            indice_start = 0
            line += " "
            for i in line:
                if i == "{" or i == "}":
                    command.append("end")
                    break
                line = line.lstrip()
                if(len(line) <= 2):
                    command.append(line)
                    break
                indice += 1
                if i == " ":
                    if line[indice_start:indice] != "   " and line[indice_start:indice] != " " and line[indice_start:indice]:
                        command.append(line[indice_start:indice].strip())
                        indice_start = indice
command_nbr = []
print(command)
liste_command = ["if","while","brosse_in","eject_dentifrisse","lumiere","not","pouce","timer","hand_button_check","button_dentifrice","wait","music1","music2","music3","music4","and","or","final","","","","","","","","","end"]
for cmd in command:
        for i in range(0,len(liste_command)):
            a = (i if cmd == liste_command[i] else -1)
            if a >= 0:
                command_nbr.append(a)
                break
bande = create_sensor(command_nbr)
for i in range(0,len(bande)-3):
    print(bande[i])
    if (bande[i+1] == "white"):
        if bande[i] != "red" and bande[i+2] != "red":
            bande[i+1] = "red"
        elif bande[i] != "green" and bande[i+2] != "green":
            bande[i+1] = "green"
        else:
            bande[i+1] = "blue"
print(command_nbr)
del command
del command_nbr


with open("code_"+str(int(time.time())%1000000)+".bande",'w',encoding = 'utf-8') as f:
    i = 0
    for line in bande:
        i += 1
        f.write(line)
        f.write(" ")
        if i % 6 == 0:
            f.write("\n")
