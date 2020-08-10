#by kamikadze3113 (Telegram)
from .. import loader, utils
import time
from telethon.tl.functions.channels import LeaveChannelRequest

@loader.tds
class TimeMod(loader.Module):
	strings = {"name": "Time Unix"}
	@loader.sudo
	async def tucmd(self, message):
	    """by kamikazde3113 (Telegram)"""
	    await message.edit("С начала эпохи прошло\n\n" + "<b>" + str(time.time()) + "</b>")
	async def yearcmd(self, message):
	    await message.edit("Сейсчас 2020 но он более известный как \n\n" + "<b>Короновирусный год</b>")
