import discord
import env.config 
import asyncio
import platform
import os
from discord.ext.commands import Bot, Context 


async def load_cogs(bot):
    """
    The code in this function is executed whenever the bot will start.
    """
    for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


def run_bot():
    intents = discord.Intents.default() 
    intents.message_content = True
    intents.emojis_and_stickers = True
    intents.guild_messages = True
    intents.reactions = True
    intents.presences = True

    bot = Bot(command_prefix=">", intents=intents, help_command=None)

    @bot.event
    async def on_ready() -> None:
        print(f'Bot sucessfully logged in as {bot.user.name}!')
        print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
        print("Syncing commands globally...")
        await bot.tree.sync(guild=discord.Object(id="1057215852090507274"))

    asyncio.run(load_cogs(bot))
    bot.run(env.config.TOKEN)


