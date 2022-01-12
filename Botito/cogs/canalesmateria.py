import discord
from discord.ext import commands
import numpy as np
import random as r
import os
os.getcwd()




class canales(commands.Cog):
  
    def __init__(self,client):
        self.client = client


    
    @commands.command()
    async def canales(self,ctx):
        
        resultado = 'No solo se enseña en el aula de clases en persona, también hay quienes llevaron todo lo de la sala, a la red. Estas personas motivaron a mi creación y, en agradecimiento, te dejamos algunos canales que ayudaron a mis creadores a entender mejor ciertos contenidos.'
        embed = discord.Embed(
            title = 'Cursos de materia',
            description = f'{resultado}',
            colour = discord.Colour.blue(),
            )
        embed.add_field(name = 'Matefácil' ,value = '[Canal](https://www.youtube.com/c/Arquimedes1075 "Matefácil") con diversos cursos de matemática (avanzada y básica), de aquí es donde extraigo los ejercicios de EDO jeje.', inline=False)
        embed.add_field(name = 'César Izquierdo' , value = '[Canal](https://www.youtube.com/user/IzquierdoCesar "César Izquierdo") de un profesor que enseña diversos cursos de física. ',inline = False)
        embed.add_field(name = 'Academia Internet' ,value ='[Canal](https://www.youtube.com/c/AcademiaInternet "Academia Internet") repleto de ejercicios de matemática',inline = False)
        embed.add_field(name = 'JulioProfe', value ='[Canal](https://www.youtube.com/user/julioprofe "JulioProfe") donde se enseña contenido variado de matemática',inline = False)
        embed.add_field(name = 'Sergio Llanos', value ='[Canal](https://www.youtube.com/user/canalfisicaparatodos "Sergio Llanos") de física en general',inline = False)
        embed.add_field(name = 'Unicoos', value ='[Canal](https://www.youtube.com/c/unicoos "Unicoos") de física e ingeniería',inline = False)
        embed.add_field(name = 'Traductor de Ingeniería', value ='[Canal](https://www.youtube.com/c/ElTraductordeIngenier%C3%ADa "Traductor de Ingeniería") que toca diversos temas de física pero principalmente ingeniería',inline = False)
        embed.add_field(name = 'Lucas', value ='[Canal](https://www.youtube.com/channel/UCR-zOCvDCayyYy1flR5qaAg "Lucas") en inglés donde tienen distintos cursos de programación (dicen que de aquí aprendieron a crearme jeje)',inline = False)
        embed.add_field(name = 'Mate316', value ='[Canal](https://www.youtube.com/channel/UC5cM4UgfeUrNQ3xt17O0EEw "Mate316") de donde salen los ejercicios de geometría analítica',inline = False)
        await ctx.send(embed=embed,delete_after=300)
        

def setup(client):
    client.add_cog(canales(client))


