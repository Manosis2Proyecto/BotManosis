import discord
from discord.ext import commands
import numpy as np
import random as r
import os
os.getcwd()




class divulgacion(commands.Cog):
  
    def __init__(self,client):
        self.client = client


    
    @commands.command()
    async def divulgacion(self,ctx):
        
        resultado = 'La divulgación es divertida y motivante, ¡No pierdas los ánimos y emociónate con esto!'
        embed = discord.Embed(
            title = 'Canales de divulgación',
            description = f'{resultado}',
            colour = discord.Colour.blue(),
            )
        embed.add_field(name = 'Robot de Platón' ,value = '[Divulgación](https://www.youtube.com/c/ElRobotdePlaton "El Robot de Platón") en general (te recomendamos sus otros canales también)**', inline=False)
        embed.add_field(name = 'Watop' , value = '[Canal](https://www.youtube.com/channel/UCPTlwyaEoJOVyvDLzHagzNQ "Watop") que trata temas de la fascinante vida animal ',inline = False)
        embed.add_field(name = 'QuantumFracture' ,value ='[Canal](https://www.youtube.com/user/QuantumFracture "QuantumFracture") dedicado a la física repleto de videos animados',inline = False)
        embed.add_field(name = 'Glóbulo Azul', value ='[Canal](https://www.youtube.com/c/Gl%C3%B3buloAzul "Glóbulo Azul") de un doctor en medicina explicando su área',inline = False)
        embed.add_field(name = 'Derivando', value ='[Canal](https://www.youtube.com/c/Derivando "Derivando") enfocado a explicar el amplio mundo de la matemática',inline = False)
        embed.add_field(name = 'Date un Vlog', value ='[Canal](https://www.youtube.com/c/DateunVlog "Date un Vlog") de un doctor en física',inline = False)
        embed.add_field(name = 'Antroporama', value ='[Canal](https://www.youtube.com/c/AntroporamaDivulgacion/about "Antroporama") dedicado a la divulgación de la neurociencia',inline = False)
        embed.add_field(name = 'Dot CSV', value ='[Canal](https://www.youtube.com/c/DotCSV/about "Dot CSV") dedicado a la computación sobre inteligencias artificiales IA',inline = False)
        await ctx.send(embed=embed,delete_after=300)
        

def setup(client):
    client.add_cog(divulgacion(client))


