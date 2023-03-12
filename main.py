import discord
import random
from discord.ext import commands

TOKEN = "MTA4MDk2MDg4NTM2MDY5MzM1OA.GO8o0t.w4MhD1PhH24WMjxXT-Cndf4kBM_CUi7cVRd6NA"

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = "/", intents = intents)


class rng:
  def __init__(self):
    self.secret_number = random.randint(0,1000)

  def reset(self):
    self.secret_number = random.randint(0,1000)

random_number = rng()

@client.command(name = "guess")
async def guess(ctx,num):
  if int(num) == random_number.secret_number:
    await ctx.channel.send("Correct, I love you <3")
    random_number.reset()
  elif int(num) > random_number.secret_number:
    await ctx.channel.send("Guess Lower")
  else:
    await ctx.channel.send("Guess Higher")







client.run(TOKEN)
