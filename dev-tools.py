from .. import loader, utils
import asyncio
import time

def register(cb):
	cb(DevTools())
class DevToolsMod(loader.Module):
	"""DevTools"""
	strings = {'name': 'DevTools'}
	
	async def basscmd(self, message):
		""".gid Id группы
		"""
		event.edit(f"ID Чата: {event.chat_id}")
