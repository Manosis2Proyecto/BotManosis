import os
from dotenv import load_dotenv
import datetime
import discord
from discord.ext import commands
from discord_components import *

from embedfiles import embedfiles


bot = commands.Bot(command_prefix='!') #prefijo para llamar al bot


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

@bot.command(name='cursos')
async def cursos(ctx):
  resultado = ':face_with_monocle: hola tarado jaja mira, estos son los cursos que tengo disponible para ti'
  embed = discord.Embed(title =f'{resultado}',
                        timestamp = datetime.datetime.utcnow(),
                        color = discord.Color.blue())
                        
  embed.add_field(name = ':books: Materia' ,value = 'selecciona con **!mat**')
  embed.add_field(name = ':brain: Ejercicios' , value = 'selecciona con **!eje**') 
  embed.add_field(name = ':woman_scientist: Divulgación' ,value ='selecciona con **!div**')
  embed.add_field(name = ':teacher: Canales', value ='selecciona con **!can**')
  await ctx.send(embed=embed, delete_after=300)
#cursos: ##############
### materias ###
@bot.command(name='mat')
async def materia(ctx):

  embed = discord.Embed(title = 'Tengo esta informacion de momento, espero que encuentres lo que buscas',
                        timestamp = datetime.datetime.utcnow(),
                        color = discord.Color.blue())
                        
                        #description ='[hola](https://www.youtube.com/watch?v=FqrlScCp1uc&ab_channel=UnPocoDeTodo)')
  embed.add_field(name = ':purple_square:Ecuaciones diferenciales', value = 'selecciona con **!edm**')
  embed.add_field(name = ':yellow_square:Electromagnetismo', value = 'selecciona con **!elm**')
  embed.add_field(name = ':blue_square:Geometría básica', value = 'selecciona con **!gem**')
  embed.add_field(name = ':green_square:Cálculo', value = 'selecciona con **!cam**')
  

  await ctx.send(embed = embed,delete_after=300)
  #curso edo materia
@bot.command(name ='edm')
async def edmateria(ctx):
  embed_edocurso = discord.Embed(title ='Curso de Ecuaciones diferenciales',
                                 color = discord.Color.purple(),
                                 url ='https://www.youtube.com/watch?v=q3PKNySW6LQ&list=PL9SnRnlzoyX0RE6_wcrTKaWj8cmQb3uO6&ab_channel=MateFacil'
  )
  await ctx.send(embed = embed_edocurso,delete_after=300)
#curso electromagnetismo
@bot.command(name='elm')
async def elemateria(ctx):
  embed_elecurso = discord.Embed(title ='Curso de Electromagnetismo',
                                 color = discord.Color.gold(),
                                 url = 'https://www.youtube.com/watch?v=cFaf1_P2Y8c&list=PLgeh_RfSoZhK6FbqP33mXtI7gV2zvhGne&ab_channel=CesarAntonioIzquierdoMerlo'
  )
  await ctx.send(embed = embed_elecurso,delete_after=300)

#curso geometria
@bot.command(name='gem')
async def geomateria(ctx):
  embed_geocurso = discord.Embed(title='Curso de geometría básica',
                                 color = discord.Color.blue(),
                                 url ='https://www.youtube.com/playlist?list=PL9SnRnlzoyX1pEm7b8wug-dzU2cCUiEl2'               
  )
  await ctx.send(embed = embed_geocurso, delete_after = 300)
  #curso calculo materia
@bot.command(name ='cam')
async def calmateria(ctx):
  embed_limit=discord.Embed(title = 'Curso de límites',
                            color = discord.Color.green(),
                            url ='https://www.youtube.com/watch?v=BlIqLvpRpHo&list=PL9SnRnlzoyX0grQboBKZetLlCA7LaiSOX&ab_channel=MateFacil'
  )
  embed_deriv=discord.Embed(title ='Curso de derivadas',
                            color = discord.Color.green(),
                            url = 'https://www.youtube.com/watch?v=ia8L26ub_pc&list=PL9SnRnlzoyX1kIbHdA7GN-6g-hvkyLbWp&ab_channel=MateFacil'
  )
  await ctx.send(embed = embed_limit, delete_after=300)
  await ctx.send(embed = embed_deriv, delete_after=300)
### ejercicios ####
@bot.command(name='eje')
async def ejerc(ctx):
  embed_ejercicios = discord.Embed(title ='¿Que te gustaría ejercitar?',
                                  color = discord.Color.blue()
  )
  embed_ejercicios.add_field(name = ':purple_square:Electromagnetismo', value = 'selecciona con **!ede**')
  embed_ejercicios.add_field(name = ':yellow_square:Electromagnetismo', value = 'selecciona con **!ele**')
  embed_ejercicios.add_field(name = ':blue_square:Geometría básica', value = 'selecciona con **!gee**')
  embed_ejercicios.add_field(name = ':green_square:Geometría básica', value = 'selecciona con **!cae**')
  await ctx.send(embed = embed_ejercicios, delete_after=300)

### ejercicios ed###
@bot.command(name ='ede')
async def edejercicio(ctx):
  embed_edejercicio = discord.Embed(title ='Ejercicio aleatorio de edo',
                                    color = discord.Color.purple(),
                                    url = 'https://www.youtube.com/watch?v=gU7OQwpVwc8&ab_channel=Upsocl'
  )
  await ctx.send(embed = embed_edejercicio, delete_after = 300)
  ### puede dejarlo así, o cambiar el embed por un link solamente###
  await ctx.send('https://www.youtube.com/watch?v=gU7OQwpVwc8&ab_channel=Upsocl')
### ejercicio electro ###
@bot.command(name='ele')
async def elejercicio(ctx):
  embed_elejercicio = discord.Embed(title = 'Ejercicio aleatorio de electro',
                                    color = discord.Color.gold(),
                                    url = 'https://www.youtube.com/watch?v=gU7OQwpVwc8&ab_channel=Upsocl'
  )
  await ctx.send(embed = embed_elejercicio, delete_after = 300)
### ejercicio geometria ###
@bot.command(name='gee')
async def geejercicio(ctx):
  embed_geejercicio = discord.Embed(title ='Ejercicio aleatorio de geometria',
                                      color = discord.Color.blue(),
                                      url = 'https://www.youtube.com/watch?v=gU7OQwpVwc8&ab_channel=Upsocl'
)
  await ctx.send(embed = embed_geejercicio, delete_after = 300)
### ejercicio calculo ###
@bot.command(name ='cae')
async def caejercicio(ctx):
  embed_caejercicio = discord.Embed(title ='ejercicio aleatorio de calculo',
                                    color = discord.Color.green(),
                                    url = 'https://www.youtube.com/watch?v=gU7OQwpVwc8&ab_channel=Upsocl'
  )
  await ctx.send(embed = embed_caejercicio,delete_after = 300)





my_secret = 'OTI5NDk5MTg5NzY1ODgxOTE3.YdoNlA.w9j7mGGzqn6_AkAqNnbQl0C20mA'
bot.run(my_secret)





#bot = EasyBot()
#bot.setCommand('!roblox','wena xoro')
#bot.setCommand(''.''')
#bot.run(os.environ['TOKEN'])