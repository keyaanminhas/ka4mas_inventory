
import pyautogui as pg
from time import sleep
import discord
from discord.ext import commands
import os
global wait
wait = 0

client = commands.Bot(command_prefix="!")

TOKEN = 'OTAwMzYwNTI1MTQwMDcwNDAw.YXAMFQ.YFWeeyP8o7e11rjP-Yy1B-883Cg'
path = 'C:\\Users\\ka4ma\\Downloads\\screenshots\\'

@client.event
async def on_ready():
    print(f'{client.user} is connected to the following guild :\n')

@client.command()

async def chegg(ctx, arg):
    #try:
        global wait
        if "https://www.chegg.com/homework-help/" not in arg: 
            await ctx.channel.send(ctx.author.mention + "This is not a chegg link!")
            return
        else:
            if wait == 0:
                wait = 1
                pg.hotkey('win', 'r')
                sleep(0.4)
                pg.typewrite('msedge')
                pg.press('ENTER')
                sleep(0.4)
                pg.typewrite(arg)
                sleep(0.3)
                pg.press('ENTER')
                sleep(3)
                pg.hotkey('alt', 'shift', 'p')
                sleep(5)
                pg.hotkey('alt', 'f4')
                images = os.listdir(path)
                await ctx.author.send(file=discord.File(fr'C:\\Users\\ka4ma\\Downloads\\screenshots\\{images[0]}'))
                os.system(f'cd {path} && del **')
                wait = 0
            else:
                await ctx.channel.send(ctx.author.mention + "Please wait and type the command once the previous one is complete")
    #except:
        #await ctx.author.send("there is no text to send or something went wrong!")
        #pass

client.run(TOKEN)