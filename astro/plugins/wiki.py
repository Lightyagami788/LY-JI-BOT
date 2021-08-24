import wikipedia

from astro.utils import admin_cmd


@astro.on(admin_cmd(pattern="wiki (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    input_str = event.pattern_match.group(1)
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"> [{s}]({url}) \n"
    await event.edit(
        "WikiPedia **Search**: {} \n\n **Result**: \n\n{}".format(input_str, result)
    )