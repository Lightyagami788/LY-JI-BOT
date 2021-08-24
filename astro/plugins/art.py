# For astro
# By @AKASH_AM1 and @xditya
# Kangers keep cr eors
from astro.config import Config
from astro.utils import admin_cmd

NAME = Config.NAME

n = str(NAME) if NAME else "Set NAME in config vars in Heroku"

# @command(outgoing=True, pattern="^.ded$")


@astro.on(admin_cmd(pattern=r"ded"))
@astro.on(sudo_cmd(pattern=r"ded"))
async def bluedevilded(ded):
    await eor(
        ded,
        n + " ==             |\n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


M = (
    "▄███████▄\n"
    "█▄█████▄█\n"
    "█▼▼▼▼▼█\n"
    "██________█▌\n"
    "█▲▲▲▲▲█\n"
    "█████████\n"
    "_████\n"
)
P = (
    "┈┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)
K = r"_/﹋\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉ - -\n" r"_/﹋\_\n"
G = (
    "........___________________\n"
    "....../ `-___________--_____|] - - - - - -\n"
    " - - ░ ▒▓▓█D \n"
    "...../==o;;;;;;;;______.:/\n"
    ".....), -.(_(__) /\n"
    "....// (..) ), —\n"
    "...//___//\n"
)
D = (
    "╥━━━━━━━━╭━━╮━━┳\n"
    "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
    "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
    "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
    "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
    "╨━━┗┛┗┛━━┗┛┗┛━━┻\n"
)
H = (
    "▬▬▬.◙.▬▬▬ \n"
    "═▂▄▄▓▄▄▂ \n"
    "◢◤ █▀▀████▄▄▄▄◢◤ \n"
    "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
    "◥█████◤ \n"
    "══╩══╩══ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ Hello, my friend :D \n"
    "╬═╬☻/ \n"
    "╬═╬/▌ \n"
    "╬═╬/ \\n"
)
S = (
    "_/﹋\_\n"
    "(҂`_´)\n"
    "<,︻╦╤─ ҉ - -\n"
    "_/﹋\_\n"

)







    

@astro.on(admin_cmd(pattern=r"monster"))
@astro.on(sudo_cmd(pattern=r"monster"))
async def bluedevilmonster(monster):
    await eor(monster, M)


@astro.on(admin_cmd(pattern=r"pig"))
@astro.on(sudo_cmd(pattern=r"pig"))
async def bluedevipig(pig):
    await eor(pig, P)


@astro.on(admin_cmd(pattern=r"killer"))
@astro.on(sudo_cmd(pattern=r"killer"))
async def bluedevikiller(killer):
    await eor(killer, K)


@astro.on(admin_cmd(pattern=r"gun"))
@astro.on(sudo_cmd(pattern=r"gun"))
async def bluedevigun(gun):
    await eor(gun, G)


@astro.on(admin_cmd(pattern=r"dog"))
@astro.on(sudo_cmd(pattern=r"dog"))
async def bluedevidog(dog):
    await eor(dog, D)


@astro.on(admin_cmd(pattern=r"helicopter"))
@astro.on(sudo_cmd(pattern=r"helicopter"))
async def bluedevihmf(helicopter):
    await eor(helicopter, H)
    
@astro.on(admin_cmd(pattern=r"soilder"))
@astro.on(sudo_cmd(pattern=r"soilder"))
async def soilder(soilder):
    await eor(soilder, S)
