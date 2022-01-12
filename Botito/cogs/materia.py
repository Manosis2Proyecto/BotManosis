import discord
from discord.ext import commands
import numpy as np
import random as r
import os
os.getcwd()




class materia(commands.Cog):
  
    def __init__(self,client):
        self.client = client


    
    @commands.command()
    async def materia(self,ctx):
        
        resultado = 'Te dejo algunos cursos que recomiendo, ¡No olvides darle tu apoyo! ¡Like y suscribirse!'
        embed = discord.Embed(
            title = 'Los cursos que tengo para ti (de momento jeje)',
            description = f'{resultado}',
            colour = discord.Colour.blue(),
            )
        embed.add_field(name = ':book: Ecuaciones Diferenciales Ordinarias' ,value = 'selecciona con **!edo**')
        embed.add_field(name = ':magnet: Electromagnetismo' , value = 'selecciona con **!electro**')
        embed.add_field(name = ':triangular_ruler: Geometría Básica' ,value ='selecciona con **!geometria**')
        embed.add_field(name = ':abacus: Cálculo diferencial e integral', value ='selecciona con **!calculo**')
        await ctx.send(embed=embed,delete_after=300)

        
     # EDO MATERIA   
    @commands.command()
    async def edo(self,ctx):
        
        resultado1 = '¿Quieres recordar o aprender EDO? ¡Genial! te dejo aquí un muy buen curso de **Matefacil**'
        embed_edo = discord.Embed(
            title = 'Ecuaciones diferenciales materia',
            description = f'{resultado1}',
            colour = discord.Colour.blue(),
            )
        
        embed_edomateria = discord.Embed(
            title = 'Curso de Ecuaciones diferenciales de Matefacil',
            colour = discord.Color.green(),
            url = 'https://www.youtube.com/playlist?list=PL9SnRnlzoyX0RE6_wcrTKaWj8cmQb3uO6')
            
        await ctx.send(embed=embed_edo,delete_after=300)
        await ctx.send(embed=embed_edomateria, delete_after=300)

        
     # Geometría MATERIA   
    @commands.command()
    async def geometria(self,ctx):
        
        resultado2 = '¿Quieres recordar o aprender Geometría? ¡Genial! te dejo aquí un muy buen curso de **Matefacil**'
        embed_geom = discord.Embed(
            title = 'Geometría materia',
            description = f'{resultado2}',
            colour = discord.Colour.blue(),
            )
        
        embed_geommateria = discord.Embed(
            title = 'Curso de Geometría elemental de Matefacil',
            colour = discord.Color.green(),
            url = 'https://www.youtube.com/playlist?list=PL9SnRnlzoyX1pEm7b8wug-dzU2cCUiEl2')
        
        embed_geomanalitica = discord.Embed(
            title = 'Curso de Geometría analítica de Matefacil',
            colour = discord.Color.green(),
            url = 'https://www.youtube.com/playlist?list=PL9SnRnlzoyX2ksvCQ2e3_uIB5SxhnpbyF')    
        await ctx.send(embed=embed_geom,delete_after=300)
        await ctx.send(embed =embed_geomanalitica, delete_after=300)
        await ctx.send(embed=embed_geommateria, delete_after=300)

     # Electromagnetismo MATERIA   
    @commands.command()
    async def electro(self,ctx):
        
        resultado3 = '¿Quieres recordar o aprender Electromagnetismo? ¡Genial! te dejo aquí un muy buen curso de **César Izquierdo**'
        embed_electro = discord.Embed(
            title = 'Electromagnetismo materia',
            description = f'{resultado3}',
            colour = discord.Colour.blue(),
            )
        
        embed_electromateria = discord.Embed(
            title = 'Curso de Teoría Electromagnética Clásica de César Izquierdo',
            colour = discord.Color.green(),
            url = 'https://www.youtube.com/playlist?list=PLgeh_RfSoZhK6FbqP33mXtI7gV2zvhGne')
            
        await ctx.send(embed=embed_electro,delete_after=300)
        await ctx.send(embed=embed_electromateria, delete_after=300)


     # Calculo MATERIA   
    @commands.command()
    async def calculo(self,ctx):
        
        resultado4 = '¿Quieres recordar o aprender Cálculo Diferencial e Integral? ¡Genial! te dejo aquí un muy buen curso de **Matefácil**'
        embed_calculo = discord.Embed(
            title = 'Cálculo Diferencial e Integral materia',
            description = f'{resultado4}',
            colour = discord.Colour.blue(),
            )
        
        embed_calculodifmateria = discord.Embed(
            title = 'Curso de Cálculo diferencial de Matefácil',
            colour = discord.Color.green(),
            url = 'https://www.youtube.com/playlist?list=PL9SnRnlzoyX1kIbHdA7GN-6g-hvkyLbWp')
        
        embed_calculointmateria = discord.Embed(
            title = 'Curso de Cálculo integral de Matefácil',
            colour = discord.Color.green(),
            url = 'https://www.youtube.com/playlist?list=PL9SnRnlzoyX39hvLuyYgFEIdCXFXI3xaU')
            
        await ctx.send(embed=embed_calculo,delete_after=300)
        await ctx.send(embed=embed_calculodifmateria, delete_after=300)
        await ctx.send(embed=embed_calculointmateria, delete_after=300)

        
        
def setup(client):
    client.add_cog(materia(client))
