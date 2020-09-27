from .. import loader, utils
import asyncio

import time
from uniborg.util import admin_cmd

@borg.on(admin_cmd("zaz ?(.*?)"))
async def _(event):
	await event.edit("ooh") 
	time.sleep(1)
	await event.edit("lol") 
	time.sleep(1) 
	await event.edit("fuck")
	time.sleep(1) 
	await event.delete()
	
@borg.on(admin_cmd("mem ?(.*?)"))
async def _(event):
  await event.edit("Скинь")
  time.sleep(1)
  await event.edit("Мемчики")
  time.sleep(1)
  await event.delete()

@borg.on(admin_cmd("gid ?(.*?)"))
async def _(event):
	event.edit(f"ID Чата:  {event.chat_id}")

@borg.on(admin_cmd("uid ?(.*?)"))
async def _(event):
	infa = str(event.sender_id)
	event.edit('ID Юзера: ' + infa)
