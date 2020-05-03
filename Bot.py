# Broadcast Chill Discord Server Automation Bot
# Written by Samuel Kapp
# https://github.com/skappDTCC/BroadcastChillDiscordBot
# https://www.linkedin.com/in/samuel-kapp-2b5130163/

# https://discordpy.readthedocs.io/en/latest/intro.html#basic-concepts
# https://issuehunt.io/blog/How-to-write-a-Discord-bot-in-Python-5bb1f0e3c556c5005573c508

# Imports the Discord module.
import discord
from discord.ext import commands

# Imports the .py python file containing the private Bot token string.
import Token

# Sets the bots command prefix
bot = commands.Bot(command_prefix='$')


# Bot Information log event upon boot
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


# Info command
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Broadcast Chill", description="Broadcast Chill Server Automation Bot", color=0x6441a5)

    # give info about you here
    embed.add_field(name="Author", value="Samuel Kapp")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite",
                    value="https://discordapp.com/api/oauth2/authorize?client_id=657860244843790336&permissions=8&scope=bot")

    await ctx.send(embed=embed)


bot.remove_command('help')


# help command
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Broadcast Chill Bot", description="List of commands:", color=0x6441a5)

    embed.add_field(name="$info", value="Gives Information about the bot", inline=False)
    embed.add_field(name="$help", value="Displays a list of commands", inline=False)

    await ctx.send(embed=embed)


# Runs the bot under the token string.
bot.run(Token.token)
