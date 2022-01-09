import os
from dotenv import load_dotenv
from discord.ext import commands
import json
import urllib.request
import numpy as np
from discord_easy_commands import EasyBot

bot = EasyBot()
bot.setCommand('!roblox',input('escribe un numero '))

bot.run(os.environ['TOKEN'])