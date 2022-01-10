import os
from dotenv import load_dotenv
import datetime
import discord
from discord.ext import commands
import json
import urllib.request
import numpy as np
from discord_easy_commands import EasyBot
from embedfiles import embedfiles
#pip install discord_easy_commands
bot = commands.Bot(command_prefix='!') #prefijo para llamar al bot

@bot.command(name='asignatura')
async def asignaturas(ctx):
  resultado = ':face_with_monocle: hola tarado jaja mira, estos son los cursos que tengo disponible para ti'
  hola = 'macaco'
  embed = discord.Embed(title =f'{resultado}',
                        description = hola,
                        timestamp = datetime.datetime.utcnow(),
                        color = discord.Color.blue())
  embed.add_field(name = 'Ecuaciones diferenciales' , value = hola)                
  await ctx.send(embed=embed)
@bot.command(name ='try')
async def echo(self, ctx):
    await ctx.message.delete()
    embed = discord.Embed(title = 'roblox',
    description = 'juegos de medo')

    sent = await ctx.send(embed=embed)











@bot.command(name='edo')
async def edo(ctx):
  modulos = ["ecuaciones diferenciales de primer orden", 'ecuaciones diferenciales de segundo orden :cry:','para seleccionar presione !edo1 o !edo2','https://www.youtube.com/watch?v=pIA40qX0ymw&list=PL9SnRnlzoyX1pEm7b8wug-dzU2cCUiEl2&ab_channel=MateFacil']
  for i in range(0,len(modulos)):
    await ctx.send(modulos[i])
@bot.command(name='manual')
async def manual(ctx):
  des = """
  Comandos de EdBot\n
  > Roblox juegos de miedo \n
  > Sobrevive al asesino :cry: \n  
  """
  embed = discord.Embed(title=embedfiles(0),
  url='https://www.youtube.com/watch?v=cw8dcjSW3dg&ab_channel=MenuDocs',
  description= des,
  timestamp=datetime.datetime.utcnow(),
  color=discord.Color.blue())   
  await ctx.send(embed=embed)
@bot.command(name='edouno')
async def edo_1(ctx):
  des1 = """
  caca\n
  > popo \n
  """
  embed1 = discord.Embed(title="edo orden 1 chida",
  url="https://www.youtube.com/watch?v=pIA40qX0ymw&list=PL9SnRnlzoyX1pEm7b8wug-dzU2cCUiEl2&ab_channel=MateFacil",
  #description= des1,
  timestamp=datetime.datetime.utcnow(),
  color=discord.Color.blue())   
  await ctx.send(embed=embed1)




bot.run(os.environ['TOKEN'])










#bot = EasyBot()
#bot.setCommand('!roblox','wena xoro')
#bot.setCommand(''.''')
#bot.run(os.environ['TOKEN'])