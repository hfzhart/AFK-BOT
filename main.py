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
    print(f"✅ Бот {bot.user} запущен на Railway!")

@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        await ctx.send("❌ Ты не в голосовом канале!")
        return
    
    channel = ctx.author.voice.channel
    try:
        await channel.connect(self_deaf=True, self_mute=True)
        await ctx.send(f"✅ Зашёл в **{channel.name}** и буду сидеть")
        
        # Простой keep-alive
        while True:
            await asyncio.sleep(300)  # каждые 5 минут проверка
    except discord.ClientException:
        await ctx.send("Я уже в войсе!")
    except Exception as e:
        await ctx.send(f"❌ Ошибка: {e}")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Вышел из войса")
    else:
        await ctx.send("Я не в войсе")

bot.run(os.getenv("TOKEN"))
