import discord
import os
from discord.ext import commands, tasks
import numpy as np
from itertools import cycle

TOKEN = 'OTI5OTgzNTYyNzcyNTMzMjUw.YdvQrw.QvawPE6lM-GfheDwf81cpdeyVyE'
client = commands.Bot(command_prefix='!')
status = cycle(['No olvidando(?' , 'Recordando lo que aprendí este año', 'Comiendo pasas'])

#### EVENTOS ####
## Cuando inicia el bot, y el estado del bot

@client.event
async def on_ready():
    change_status.start()


    print('Cerrado y cargado')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'Creo que no tengo ese comando:( ¿lo escribiste bien?')
        await ctx.send('Si tienes dudas, escribe **!help** u **!hola** :)')

## Inicio del loop para cambiar el estado
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


#### COMANDOS ####
#Cargar y recargar subarchivos (cogs)
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')





client.run(TOKEN)
