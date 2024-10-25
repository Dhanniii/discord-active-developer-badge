import discord
from discord.ext import commands
from datetime import datetime


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"bot is ready {bot.user}")

@bot.tree.command(
    name="badges", 
    description="Get my Badges"
)
async def badges(interaction: discord.Interaction):
    await interaction.response.defer() 
    timestamp = datetime.now().strftime("%B %d, %Y")
    
    embed = discord.Embed(
        title="Command run successfully",
        description="Successfully run the command, now you must wait to get the Active Developer Badge.",
        color=discord.Color.dark_grey()
    )
    embed.add_field(
        name="",
        value="Congratulations! The command has been successfully executed. To receive your Active Developer Badge, please click the claim link below. Please note that (it may take up to 24 hours for Discord to verify your eligibility and process your badge request) https://discord.com/developers/active-developer",
        inline=False
    )
    embed.set_author(name=f"{interaction.user.name}", icon_url=interaction.user.display_avatar.url)
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.set_footer(text=f"Requested on {timestamp}")
    
    await interaction.followup.send(embed=embed)

bot.run("") # <-- insert your discord token
