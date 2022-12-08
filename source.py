#import adafruit_tcs34725
#from adafruit_crickit import crickit
ntnst = 0
indice = -1
def format_command(liste: any):
    """
    recoit une liste de nombre
    renvoie un nombre entre 0 et 26 etant donné que une commande
    est constitué de 4 bits
    """
    n = liste[0]
    n += 3 * liste[1] + 9 * liste[2]
    return n

def code_exit(cmd, el):
    """
    Retourne un TRUE ou FALSE en fonction de el
    """
    if cmd.var[10] == 1 and el <= 1:
        cmd.var[10] += 1
    elif el <= 1:
        cmd.var[10] += 2
    elif el == 26:
        cmd.var[10] -= 1
    if cmd.var[10] > 0:
        return 0
    cmd.var[10] = 1
    return 1

def exec_simple_command(cmd, cmd_i):
    """
    execute une commande sans boucle sans condition
    """
    if (cmd_i == 5):
        cmd.var[0] = 1
        return
    if (cmd_i == 2):
        cmd.fbrosse_out()
    elif (cmd_i == 3):
        cmd.feject_dentifrisse()
    elif (cmd_i == 4):
        cmd.flumiere()
    elif (cmd_i == 6):
        cmd.fpouce()
    elif (cmd_i == 7):
        cmd.ftimer()
    elif (cmd_i == 8):
        cmd.fmusic()
    elif (cmd_i == 9):
        cmd.fbuton_onclick()
    elif (cmd_i == 10):
        cmd.fbrosse_detect()
    elif (cmd_i == 11):
        cmd.fwait()
    cmd.var[0] = 0

def get_cmd(sensor):
    cmd = []
    colors = get_color(sensor)
    while len(cmd) < 3:
        while colors == "white": # tant qu on est sur du blanc
            colors = get_color(sensor)  # recupère les couleurs
        # on est plus sur du blanc
        if colors == "red":
            cmd.append(0)
        elif colors == "green":
            cmd.append(1)
        elif colors == "blue":
            cmd.append(2)
        while colors == "red" or colors == "blue" or colors == "green":  # tant qu'on est sur du blanc
            colors = get_color(sensor)  # recupère les couleurs
        # on est plus sur de la couleur
    command = format_command(cmd)
    del cmd
    return command

def error_music():
	###
	# execute une serie du signaux alarmant permetant a l'utilisateur de comprendre qu'il a fait une erreur
	###
	pass

def get_color(sensor):
    global ntnst,indice
    indice += ntnst
    return sensor[indice]
def test_again():
    global indice
    indice = -1
def motor12(intensity):
    global ntnst
    ntnst = intensity
"""
def get_color(sensor):
    color = sensor.color_rgb_bytes
    while (color[0] == 0 and color[1] == 0 and color[2] == 0):
        color = sensor.color_rgb_bytes
    red = color[0] * 10
    green = color[1] * 10
    blue = color[2] * 5
    median = ((red+1) * green * blue)**(1/3)
    valeur = 40
    count = 0
    txt_color=""
    for col in color:
        if col - median > valeur:
            count += 1
    if count > 1:
        txt_color = "white";
    elif red - median > valeur:
        txt_color = "red"
    elif green - median > valeur:
        txt_color = "green"
    elif blue - median > valeur:
        txt_color = "blue"
    print (str(red)+" "+str(green)+" "+str(blue)+" "+txt_color)
    return txt_color
def motor12(intensity):
    global ntnst
    """"""
    Lance ou arrète les moteurs en fonction de intensity
    """"""
    crickit.dc_motor_1.throttle = intensity
    crickit.dc_motor_2.throttle = intensity
"""
