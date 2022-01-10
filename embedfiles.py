import os
from dotenv import load_dotenv
import datetime
import discord
from discord.ext import commands
import json
import urllib.request
import numpy as np
from discord_easy_commands import EasyBot

titulos = ['Ecuaciones diferenciales',
           'Electromagnetismo',
           'Geometría básica',
           ]

def embedfiles(ti):
  return titulos[ti]

Metodos = ['Variación de parametros','']
  
   