command = []
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
            indice = 0
            indice_start = 0
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
                    if line[indice_start:indice] != "   " and line[indice_start:indice] != " ":
                        command.append(line[indice_start:indice].strip())
                        indice_start = indice
command_nbr = []
for cmd in command:
    if (cmd == "if"):
        command_nbr.append(0)
    elif(cmd == "while"):
        command_nbr.append(1)
    elif(cmd == "not"):
        command_nbr.append(5)
    elif(cmd == "and"):
        command_nbr.append(15)
    elif(cmd == "or"):
        command_nbr.append(16)
    elif(cmd == "end"):
        command_nbr.append(26)
    else:
        command_nbr.append(int(cmd))

bande = create_sensor(command_nbr)
del command
del command_nbr


with open("code.bande",'w',encoding = 'utf-8') as f:
    i = 0
    for line in bande:
        i += 1
        f.write(line)
        f.write(" ")
        if i % 6 == 0:
            f.write("\n")
