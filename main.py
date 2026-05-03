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
    print(f"✅ Бот {bot.user} успешно запущен на Railway!")

async def play_silence(vc):
    while vc.is_connected():
        try:
            # Простая тишина
            source = discord.FFmpegPCMAudio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", 
                                          options="-filter:a volume=0.001")  # почти тишина
            vc.play(source, after=lambda e: None)
            await asyncio.sleep(180)  # 3 минуты
        except:
            await asyncio.sleep(10)

@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        await ctx.send("❌ Ты не в войсе!")
        return
    channel = ctx.author.voice.channel
    try:
        vc = await channel.connect(self_deaf=True, self_mute=True)
        await ctx.send(f"✅ Зашёл в **{channel.name}**")
        asyncio.create_task(play_silence(vc))
    except Exception as e:
        await ctx.send(f"Ошибка: {e}")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Вышел")

bot.run(os.getenv("TOKEN"))
