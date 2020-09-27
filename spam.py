from .. import loader, utils
import asyncio
def register(cb):
    cb(spamMod())
class spamMod(loader.Module):
    """spam"""
    strings = {'name': 'Spam'}

    async def spamcmd(self, message):
        """.spam <кол-во сообщений для спама> <текст>           
        """
        count = int(utils.get_args_raw(message))
        textt = str(utils.get_args_raw(message))
        
        for i in range(count):      
          await message.client.send_message(message.to_id,textt)
          asyncio.sleep(0,5)
