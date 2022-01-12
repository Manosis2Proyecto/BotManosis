import discord
from discord.ext import commands
import numpy as np
import random as r
import os
os.getcwd()

# Ejercicios EDO
linkk_edo = np.genfromtxt('.\\edo_ejercicios.txt',dtype='str',delimiter=",",autostrip=True,usecols=0)
img_edo = np.genfromtxt('.\\edo_ejercicios.txt',dtype='str',delimiter=",",autostrip=True,usecols=1)
len_edo = len(linkk_edo)
inter_edo = np.arange(0,len_edo)

# Ejercicios derivada
linkk_derivada = np.genfromtxt('.\\derivada_ejercicios.txt',dtype='str',delimiter=",",autostrip=True,usecols=0)
img_derivada = np.genfromtxt('.\\derivada_ejercicios.txt',dtype='str',delimiter=",",autostrip=True,usecols=1)
len_derivada = len(linkk_derivada)
inter_derivada = np.arange(0,len_derivada)

# Ejercicios Integrales
linkk_integrales = np.genfromtxt('.\\integrales_ejercicios.txt',dtype='str',delimiter=",",autostrip=True,usecols=0)
img_integrales = np.genfromtxt('.\\integrales_ejercicios.txt',dtype='str',delimiter=",",autostrip=True,usecols=1)
len_integrales = len(linkk_integrales)
inter_integrales = np.arange(0,len_integrales)

# Ejercicios Geometría
linkk_geometria = np.genfromtxt('.\\geometria_ejercicios.txt',dtype='str',delimiter=",",autostrip=True,usecols=0)
img_geometria = np.genfromtxt('.\\geometria_ejercicios.txt',dtype='str',delimiter=",",autostrip=True,usecols=1)
len_geometria = len(linkk_geometria)
inter_geometria = np.arange(0,len_geometria)

# Ejercicio Aleatorio
linkk_aleatorio = np.concatenate((linkk_edo,linkk_integrales,linkk_geometria,linkk_derivada))
img_aleatorio = np.concatenate((img_geometria,img_integrales,img_derivada,img_edo))
len_aleatorio = len(linkk_aleatorio)
inter_aleatorio = np.arange(0,len_aleatorio)

class ejercicios(commands.Cog):
  
    def __init__(self,client):
        self.client = client


    
    @commands.command()
    async def ejercicios(self,ctx):     
        resultado = 'Selecciona la asignatura y te daremos un ejercicio para resolver.'

        embed = discord.Embed(
            title = '¿Quieres ejercitar? ¡Muy bien!',
            description = f'{resultado}',
            colour = discord.Colour.blue(),
            )
        embed.add_field(name = ':book: Ejercicio de EDO' ,value = 'selecciona con **!edoej**')
        embed.add_field(name = ':chart_with_upwards_trend: Cálculo diferencial' , value = 'selecciona con **!difej**')
        embed.add_field(name = ':triangular_ruler: Geometría Básica' ,value ='selecciona con **!geoej**')
        embed.add_field(name = ':abacus: Cálculo integral', value ='selecciona con **!intej**')
        embed.add_field(name = ':game_die: Ejercicio aleatorio :open_mouth:', value ='selecciona con **!aleatorio**')
        await ctx.send(embed=embed,delete_after=300)
        
# Ejercicios EDO
    @commands.command()
    async def edoej(self,ctx):
        t = np.random.choice(inter_edo)
        link = linkk_edo[t]
        imagen = img_edo[t]
        
        embed = discord.Embed(
            title = 'Resuelve este ejercicio',
            description = f'Cuando termines y si quieres comprobar, pincha [aquí]({link})',
            colour = discord.Colour.blue(),
            url = f'{link}'
            )
        embed.set_image(url = f'{imagen}')
        await ctx.send(embed=embed)

# Ejercicios Derivada
    @commands.command()
    async def difej(self,ctx):
        t = np.random.choice(inter_derivada)
        link = linkk_derivada[t]
        imagen = img_derivada[t]
        
        embed = discord.Embed(
            title = 'Resuelve este ejercicio',
            description = f'Cuando termines y si quieres comprobar, pincha [aquí]({link})',
            colour = discord.Colour.blue(),
            url = f'{link}'
            )
        embed.set_image(url = f'{imagen}')
        await ctx.send(embed=embed)


# Ejercicios Integrales
    @commands.command()
    async def intej(self,ctx):
        t = np.random.choice(inter_integrales)
        link = linkk_integrales[t]
        imagen = img_integrales[t]
        
        embed = discord.Embed(
            title = 'Resuelve este ejercicio',
            description = f'Cuando termines y si quieres comprobar, pincha [aquí]({link})',
            colour = discord.Colour.blue(),
            url = f'{link}'
            )
        embed.set_image(url = f'{imagen}')
        await ctx.send(embed=embed)

# Ejercicios Integrales
    @commands.command()
    async def geoej(self,ctx):
        t = np.random.choice(inter_geometria)
        link = linkk_geometria[t]
        imagen = img_geometria[t]
        
        embed = discord.Embed(
            title = 'Resuelve este ejercicio',
            description = f'Cuando termines y si quieres comprobar, pincha [aquí]({link})',
            colour = discord.Colour.blue(),
            url = f'{link}'
            )
        embed.set_image(url = f'{imagen}')
        await ctx.send(embed=embed)

# Ejercicios aleatorio
    @commands.command()
    async def aleatorio(self,ctx):
        t = np.random.choice(inter_aleatorio)
        link = linkk_aleatorio[t]
        imagen = img_aleatorio[t]
        
        embed = discord.Embed(
            title = 'Resuelve este ejercicio',
            description = f'Cuando termines y si quieres comprobar, pincha [aquí]({link})',
            colour = discord.Colour.blue(),
            url = f'{link}'
            )
        embed.set_image(url = f'{imagen}')
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(ejercicios(client))
