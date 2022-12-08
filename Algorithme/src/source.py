from adafruit_crickit import crickit
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
        cmd.brosse_in()
    elif (cmd_i == 3):
        cmd.eject_dentifrisse()
    elif (cmd_i == 4):
        cmd.lumiere()
    elif (cmd_i == 6):
        cmd.pouce()
    elif (cmd_i == 7):
        cmd.timer()
    elif (cmd_i == 8):
        cmd.hand_button_check()
    elif (cmd_i == 9):
        cmd.capteur_distance_on()
    elif (cmd_i == 10):
        cmd.wait()
    elif (cmd_i == 11):
        cmd.music1()
    elif (cmd_i == 12):
        cmd.music2()
    elif (cmd_i == 13):
        cmd.music3()
    elif (cmd_i == 14):
        cmd.music4()
    cmd.var[0] = 0

def get_cmd(sensor):
    cmd = []
    colors = get_color(sensor)
    while len(cmd) < 3:
        last_colors = colors
        while colors == last_colors: # tant qu on est sur du blanc
            colors = get_color(sensor)  # recupère les couleurs
        # on est plus sur du blanc
        cmd.append(colors)
        while colors == cmd[-1]:  # tant qu'on est sur du blanc
            colors = get_color(sensor)  # recupère les couleurs
        # on est plus sur de la couleur
    command = format_command(cmd)
    del cmd
    return command

def get_color(sensor):
    global last_colors
    color = sensor.color_rgb_bytes
    while (color[0] == 0 and color[1] == 0 and color[2] == 0):
        color = sensor.color_rgb_bytes
    red = color[0] * 10
    green = color[1] * 10
    blue = color[2] * 10
    count = 0
    txt_color=-1
    if red > blue and red > green:
        txt_color = 0
    elif green > blue and red < green:
        txt_color = 1
    else:
        txt_color = 2
    last_colors.append(txt_color)
    if len(last_colors) > 11:
        last_colors[1:]
    count = []
    count.append(0)
    count.append(0)
    count.append(0)
    for i in last_colors:
            count[i] += 1
    if count[0] > count[1] and count[0] > count[2]:
        return 0
    if count[1] > count[0] and count[1] > count[2]:
        return 1
    del count
    return 2
    #print (str(median)+" "+str(red)+" "+str(green)+" "+str(blue)+" "+str(txt_color))
def motor12(intensity):
    global ntnst
    """
    Lance ou arrète les moteurs en fonction de intensity
    """
    crickit.dc_motor_1.throttle = intensity
