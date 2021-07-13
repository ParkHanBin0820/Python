import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")



@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.cgannel.send("ㅇ")


client.run("ODUwMzYwNjc5MTM5NTA4MjI0.YLomGA.bOwCUe9MTDFMTnBWrqX8nkll3Qo")