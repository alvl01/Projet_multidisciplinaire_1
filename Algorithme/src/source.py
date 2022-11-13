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

def code_exit(liste):
    """
    Retourne un TRUE ou FALSE en fonction de si le code 1 1 1 1 est lu par la machine
    de turing
    """
    i = len(liste) - 1  # longeur de la liste - 1
    if (i >= 2):  # si il y a 4 éléments dans la liste
        if (liste[i] == 2 and liste[i - 1] == 2 and liste[i - 2] == 2):
            # 1 == TRUE and 0 == FALSE ex: liste[1] = 1 = TRUE
            return 1
    return 0

def exec_simple_command(cmd, cmd_i):
    """
    execute une commande sans boucle sans condition
    """
    if (cmd_i == 5):
        cmd.negation = 1
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
    cmd.negation = 0

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
