import discord
from discord.ext import commands
import numpy as np
import os
os.getcwd()

#d2 = np.genfromtxt('.\\txtfiles\\edo_ejercicios.txt',dtype='str',delimiter=",",autostrip=True)
d = np.genfromtxt('.\\edo_ejercicios.txt',dtype='str',delimiter=",",autostrip=True)

#Comenta la función que quiere crear.
class edo(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def edo(self,ctx):
        await ctx.send(f'hola {np.random.choice(d)}')

def setup(client):
    client.add_cog(edo(client))
