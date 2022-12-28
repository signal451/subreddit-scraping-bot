import discord

from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context

# @tree.command(name = "meme", description = "grabs meme from subreddit", guild=discord.Object(id="1057215852090507274"))
# async def slashing_commanding(int: discord.Interaction):
#     # okie this respond text message
#     await int.response.send_message("command")


class cmd(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="meme", description="gets meme from r/meme subreddit")
    async def meme(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hey here's your meme boi")



async def setup(bot):
    await bot.add_cog(cmd(bot), guilds = [discord.Object(id="1057215852090507274")])