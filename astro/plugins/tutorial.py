from astro.utils import admin_cmd 
from astro import CMD_HELP

@astro.on(admin_cmd(pattern="tut ?(.*)"))
async def tut(astro):
        await astro.edit("Below is Tutorial To Deploy ASTRO-UB\n\n[Tutorial](https://youtu.be/vIrfR_tTmls)", link_preview=False)
        
CMD_HELP.update({"tut": "➟ .tut\nUse - Get the tutorial of AstroUB."})
