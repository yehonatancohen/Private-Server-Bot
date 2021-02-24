import discord
import json
import random
import os
from pathlib import Path
from discord.ext import commands
from importlib.machinery import SourceFileLoader


token = os.environ['DISCORD_TOKEN']

intents = discord.Intents.all()

c = commands.Bot(command_prefix = '.', intents=intents)
c.remove_command('help')

@c.event
async def on_ready():
    print(f"{c.user.name}")
    for guild in c.guilds:
        members = len(guild.members)

@c.command()
@commands.has_permissions(administrator = True)
async def move_channels(ctx):
    guild = ctx.message.guild
    category = discord.utils.get(guild.channels, name="חינם")
    category2 = discord.utils.get(guild.channels, name="חינם 2")
    curr_category = category
    index = 0
    channel_list = []
    for channel in guild.channels:
        if channel.category_id is None and channel.name != "חינם" and channel.name != "משלם" and channel.name != "בוסטר" and channel.name != "נעול" and channel.name != "Text Channels" and channel.name != "חינם 2":
            channel_list.append(channel)    
    channel_list = sorted([str(channel.name) for channel in channel_list])
    for channel in guild.channels:
        index += 1
        if index >= 50:
            curr_category = category2
        if channel.category_id is None and channel.name != "חינם" and channel.name != "משלם" and channel.name != "בוסטר" and channel.name != "נעול" and channel.name != "Text Channels" and channel.name != "חינם 2":
            await channel.edit(category=curr_category, nsfw=True)

@c.command()
@commands.has_permissions(administrator = True)
async def purge(ctx,* limit):
    member = ctx.message.author
    await ctx.message.delete()
    msg = []
    try:
        limit = int(limit)
    except:
        limit = 100
    if not member:
        await ctx.channel.purge(limit=limit)
        return await ctx.send(f"**מחקתי {limit} הודעות**", delete_after=2)
    async for m in ctx.channel.history():
        if len(msg) == limit:
            break
        msg.append(m)
    await ctx.channel.delete_messages(msg)
    await ctx.send(f"מחקתי {limit} הודעות", delete_after=2)

@c.command()
@commands.has_permissions(administrator = True)
async def setdelay(ctx, seconds: int):
    await ctx.message.delete()
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"שיניתי את הקולדאון ל{seconds} שניות",delete_after=3)

@c.command()
async def invite(ctx,* amount):
    channel = discord.utils.get(ctx.message.guild.channels, id=813778440846311475)
    try:
        amount = int(amount)
        if amount > 5:
            amount = 5
        else:
            amount = int(amount)
    except:
        amount = 1
    inv_link = await channel.create_invite(max_age=0, max_uses=amount, unique=True)
    await ctx.message.author.send(f"`יצרתי לינק לשרת עם {amount} מקומות לתמיד. תוכל\י לקבל עוד לינק בעוד 5 שעות.\n{inv_link}")
    

c.run(token)