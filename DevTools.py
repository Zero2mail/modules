
from .. import loader, utils
import asyncio
import time

def register(cb):
	cb(DevTools())
class DevToolsMod(loader.Module):
	"""DevTools"""
	strings = {'name': 'DevTools'}
	
	async def gidcmd(self, message):
		""".gid Id группы
		"""
		await event.edit(f"ID Чата: {event.chat_id}")
	
	async def uidcmd(self, message):
		""".uid Id юзера
		"""
		idd = str(event.sender_id)
		await event.edit('ID Юзера: ' + idd)
