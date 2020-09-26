import time
from uniborg.util import admin_cmd

@borg.on(admin_cmd("zaz ?(.*?)"))
async def _(event):
await event.edit("Скинь")
time.sleep(2)
await event.edit("Мемчики")
time.sleep(2)
event.delete()
