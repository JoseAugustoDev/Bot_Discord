import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} está Online!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello, world!")

    if message.content.startswith("!spfc"):
        await message.channel.send("O maior de todos!")
        
client.run("MTE0MDc3Nzk5NzM1NjUxMTI5Mw.G0nFv3.lALF7Q1EUBrqYeQTmWawpYLEnKL4mfCB7N7nt0")