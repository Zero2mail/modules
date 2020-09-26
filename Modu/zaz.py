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