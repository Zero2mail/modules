from .. import loader, utils
import asyncio

def register(cb):
    cb(pidorMod())
class pidorMod(loader.Module):
    """pidor"""
    strings = {'name': 'SpamPidor'}

    async def pidorcmd(self, message):
        """.pidor <кол-во сообщений для спама>           
        """
        count = int(utils.get_args_raw(message))
        
        for i in range(count):      
          await message.client.send_message(message.to_id,"ты пидор")
          asyncio.sleep(0,5)
