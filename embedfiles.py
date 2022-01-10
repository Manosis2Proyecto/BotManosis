import os
from dotenv import load_dotenv
import datetime
import discord
from discord.ext import commands
#import json
#import urllib.request
import numpy as np
#from discord_easy_commands import EasyBot

materia = np.genfromtxt('edo_materia.txt',delimiter =',')

titulos = materia[0:,0]

def embedfiles(ti):
  return titulos[ti]

#def randommat(ti,ed):