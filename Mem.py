import time
from uniborg.util import admin_cmd

@borg.on(admin_cmd("mem ?(.*?)"))
async def _(event):
  await event.edit("Скинь")
  time.sleep(1)
  await event.edit("Мемчики")
  time.sleep(1)
  await event.delete()
