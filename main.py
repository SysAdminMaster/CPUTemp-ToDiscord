import os
import asyncio
import datetime
import psutil
import discord
from discord import Embed
intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = ""
channelid = 0

@client.event
async def on_ready():
    await temp()
async def temp():
    channel = client.get_channel(channelid)
    message = await channel.send(embed=Embed(title='Fetching temperature...', color=0x00ff00))
    temperatures = []
    while True:
        temperature = round(float(str(psutil.sensors_temperatures()).split(" ")[2].replace("current=", "").split(".")[0]), 2)
        temperatures.append((datetime.datetime.now(), temperature))
        current_time = datetime.datetime.now()
        one_hour_ago = current_time - datetime.timedelta(hours=1)
        twelve_hours_ago = current_time - datetime.timedelta(hours=12)
        twenty_four_hours_ago = current_time - datetime.timedelta(hours=24)
        temperatures_last_hour = [x for x in temperatures if one_hour_ago <= x[0] <= current_time]
        temperatures_last_12_hours = [x for x in temperatures if twelve_hours_ago <= x[0] <= current_time]
        temperatures_last_24_hours = [x for x in temperatures if twenty_four_hours_ago <= x[0] <= current_time]
        avg_temperature_last_hour = sum([x[1] for x in temperatures_last_hour]) / len(temperatures_last_hour)
        avg_temperature_last_12_hours = sum([x[1] for x in temperatures_last_12_hours]) / len(temperatures_last_12_hours)
        avg_temperature_last_24_hours = sum([x[1] for x in temperatures_last_24_hours]) / len(temperatures_last_24_hours)
        embed = Embed(title='Temperature information', color=0x00ff00)
        embed.add_field(name='Current temperature', value=f'{temperature}°C')
        embed.add_field(name='Average temperature last hour', value=f'{avg_temperature_last_hour}°C')
        embed.add_field(name='Average temperature last 12 hours', value=f'{avg_temperature_last_12_hours}°C')
        embed.add_field(name='Average temperature last 24 hours', value=f'{avg_temperature_last_24_hours}°C')
        await message.edit(embed=embed)
        await asyncio.sleep(5) 

client.run(token)
