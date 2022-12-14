import time
def read_program(sensor):
    """
    algorithme permetant de lire la bande
    retourne une liste de nombre tous < 3^3 = 27
    """
    # SI BUFFER EST VIDE
    sc.motor12(1)
    Buf = []
    Buf.append(get_cmd(sensor))
    exit_nbr = 1
    while not code_exit(exit_nbr, Buffer_[-1]):
        Buf.append(get_cmd(sensor))
    motor12(0)  # arrete les moteurs
    ######################
    return Buf

def format_command(liste: any):
    """
    recoit une liste de nombre
    renvoie un nombre entre 0 et 26 etant donné que une commande
    est constitué de 3 bits
    """
    n = liste[0]
    n += 3 * liste[1] + 9 * liste[2]
    return n

def code_exit(end, el):
    """
    Retourne un TRUE ou FALSE en fonction de el
    """
    if el <= 1:
        end += 2
    elif el == 26:
        end -= 1
    if end > 0:
        return 0
    return 1

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
    color = sensor.color_rgb_bytes
    while (color[0] == 0 and color[1] == 0 and color[2] == 0):
        color = sensor.color_rgb_bytes
    red = color[0] * 10
    green = color[1] * 10
    blue = color[2] * 10
    count = 0
    txt_color=-1
    if red > blue and red > green:
        return 0
    elif green > blue and red < green:
        return 1
    return 2
    #print (str(median)+" "+str(red)+" "+str(green)+" "+str(blue)+" "+str(txt_color))
def motor12(intensity):
    """
    Lance ou arrète les moteurs en fonction de intensity
    """
    crickit.dc_motor_1.throttle = intensity
