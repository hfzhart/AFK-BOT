import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Бот {bot.user} запущен!")

@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        await ctx.send("❌ Ты не в голосовом канале!")
        return
    
    channel = ctx.author.voice.channel
    try:
        await channel.connect(self_deaf=True, self_mute=True)
        await ctx.send(f"✅ Зашёл в **{channel.name}**")
        print(f"Подключился к {channel.name}")
        
        # Keep alive
        while True:
            await asyncio.sleep(60)
    except Exception as e:
        await ctx.send(f"❌ Ошибка: {e}")
        print(f"Ошибка: {e}")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Вышел")
    else:
        await ctx.send("Не в войсе")

bot.run(os.getenv("TOKEN"))
