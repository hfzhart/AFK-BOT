import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True   # Это обязательно для префикс-команд

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Бот {bot.user} запущен!")

@bot.command()
async def join(ctx):
    await ctx.send("Попытка подключения...")
    if not ctx.author.voice:
        await ctx.send("❌ Ты должен быть в голосовом канале!")
        return
    
    channel = ctx.author.voice.channel
    try:
        await channel.connect(self_deaf=True, self_mute=True)
        await ctx.send(f"✅ Успешно зашёл в **{channel.name}**")
    except Exception as e:
        await ctx.send(f"❌ Не смог зайти: {e}")

bot.run(os.getenv("TOKEN"))
