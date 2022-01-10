import os
from dotenv import load_dotenv
import datetime
import discord
from discord.ext import commands
from discord_components import *
#import json
#import urllib.request
#import numpy as np
#from discord_easy_commands import EasyBot
from embedfiles import embedfiles
#from discord_buttons import *

#pip install discord_easy_commands
bot = commands.Bot(command_prefix='!') #prefijo para llamar al bot
#ddb = DiscordButton(bot)

@bot.event
async def in_ready():
  print('EdBot is Online')
  DiscordComponents(bot)

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = 'JulioProfe'))

@bot.command(name='hola')
async def saludar(ctx):
  await ctx.send('no toi')

@bot.command(name='asignatura')
async def asignaturas(ctx):
  resultado = ':face_with_monocle: hola tarado jaja mira, estos son los cursos que tengo disponible para ti'
  seleccion = ['selecciona con **!ed**', 'selecciona con **!ele**','selecciona con **!geo**']
  embed = discord.Embed(title =f'{resultado}',
                        timestamp = datetime.datetime.utcnow(),
                        color = discord.Color.blue(),
                        description ='hola')
  embed.add_field(name = ':purple_square: Ecuaciones diferenciales' ,value = seleccion[0])
  embed.add_field(name = ':yellow_square: Electromagnetismo' , value = seleccion[1]) 
  embed.add_field(name = ':blue_square: Geometría' , value = seleccion[2])
  await ctx.send(embed=embed)

@bot.command(name='ed')
async def edo(ctx):

  embed = discord.Embed(title = 'te dejare este problema',
                        timestamp = datetime.datetime.utcnow(),
                        color = discord.Color.purple()
  )
  embed.add_field(name = 'Ecuacion diferencial', value = 'metodo variacion de parametros')
  monito = discord.File('monito.jpg', filename ='monito.jpg')
  await ctx.send(embed = embed,delete_after=10)
  await ctx.send(file = monito, delete_after=10)














#con este se pone foto#
#@bot.command(name='edo')
#async def monito(ctx):
 # monito = discord.File('monito.jpg', filename='monito.jpg')
  #await ctx.send(content='mira el monito', file = monito)




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

async def button(ctx):
  DiscordComponents(bot)
  resultado = ':face_with_monocle: hola tarado jaja mira, estos son los cursos que tengo disponible para ti'
  seleccion = ['selecciona con **1**', 'selecciona con **2**','selecciona con **3**']
  embed = discord.Embed(title =f'{resultado}',
                        description = 'hola mi rei',
                        timestamp = datetime.datetime.utcnow(),
                        color = discord.Color.blue())
  embed.add_field(name = ':purple_square: Ecuaciones diferenciales' ,value = seleccion[0])
  embed.add_field(name = ':yellow_square: Electromagnetismo' , value = seleccion[1]) 
  embed.add_field(name = ':blue_square: Geometría' , value = seleccion[2])        
  await ctx.send(embed=embed,delete_after=15)
#@bot.command(name='boton')

  #interaction = await bot.wait_for('button_click', check = lambda i: i.component.label.startswith('Click'))
  #await interaction.send(embed = embed, content ='holaa')
  #await ctx.send(embed = embed,components =[Button(label='2', custom_id ='electro')],delete_after=10)

  #await interactionelectro.send(content = 'electro')
  #await interactiongeometria.send(content = 'geometria')
  #interactionedo = await bot.wait_for('button_click', check = lambda i: i.custom_id =='edo')
  #interactionelectro = await bot.wait_for('button_click', check = lambda i: i.custom_id =='electro')
  #interactiongeometria = await bot.wait_for('button_click', check = lambda i: i.custom_id =='geometria') 

#async def button(ctx):
#  m = await ctx.send(
#    'tocame ',
#    buttons=[
#     Button(style = ButtonStyle.blue, label = 'aqui'),
#      Button(style = ButtonStyle.red, label = 'aqui')
#    ],
#  )
#  res = await bot.wait_for_button_click(m)
#  await res.respond(
#    Type = InteractionType.ChannelMessageWithSource,
#    content = f'{res.button.label} hiciste click'
# )

my_secret = 'OTI5NDk5MTg5NzY1ODgxOTE3.YdoNlA.bMk7PEY98TjgfY7umXZx_LhAo20'
bot.run(my_secret)





#bot = EasyBot()
#bot.setCommand('!roblox','wena xoro')
#bot.setCommand(''.''')
#bot.run(os.environ['TOKEN'])