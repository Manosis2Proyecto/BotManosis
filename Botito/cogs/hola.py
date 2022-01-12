import discord
from discord.ext import commands
import numpy as np
import random as r
import os
os.getcwd()




class hola(commands.Cog):
  
    def __init__(self,client):
        self.client = client


    
    @commands.command()
    async def hola(self,ctx):
        
        resultado = ':face_with_monocle: Hola, ¡qué gusto verte! Estos son los comandos que tengo para ti'
        embed = discord.Embed(
            title = '¿En qué puedo ayudarte?',
            description = f'{resultado}',
            colour = discord.Colour.blue(),
            
            )
        embed.add_field(name = ':books: Materia' ,value = 'selecciona con **!materia**')
        embed.add_field(name = ':brain: Ejercicios' , value = 'selecciona con **!ejercicios**')
        embed.add_field(name = ':woman_scientist: Divulgación' ,value ='selecciona con **!divulgacion**')
        embed.add_field(name = ':teacher: Canales de Youtube que recomendamos', value ='selecciona con **!canales**')
        await ctx.send(embed=embed,delete_after=300)
        

def setup(client):
    client.add_cog(hola(client))






