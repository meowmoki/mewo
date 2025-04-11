import nextcord
from nextcord.ext import commands
from info import *

class Client(nextcord.Client):
    async def on_ready(self):
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name='with my balls. have you seen my balls?'))
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        elif message.content.startswith('hello') and message.guild_id != 1331932295506034711:
            await message.channel.send(f'it\'s never lupus, {message.author}')
        elif 'i\'m going' in message.content.lower() or 'im going' in message.content.lower():
            if message.guild != None:
                await message.channel.send('are you?')
            await message.author.send('https://media.discordapp.net/attachments/1340628176136704060/1360026907386712184/gbd-dog.png?ex=67f99f42&is=67f84dc2&hm=5cc048ff7d65e30ed6b0682546dc532c28f4765701c171c80d0377610d0f8e88&=&format=webp&quality=lossless')
        elif ' sigma' in message.content.lower() or 'sigma ' in message.content.lower() or ' sigma ' in message.content.lower():
            if 'sigma attack' not in message.content.lower():
                if message.guild != None:
                    await message.channel.send('you know who else is sigma?')
                await message.author.send('https://tenor.com/view/muscle-man-you-know-who-else-my-mom-regular-show-funny-gif-9101122073397073314')

   
    async def on_raw_reaction_add(self, payload: nextcord.RawReactionActionEvent):
        if payload.guild_id == None or payload.guild_id == 1331932295506034711:
            return
        else:
            channel = payload.channel_id
            custom = payload.emoji.id
            dest = self.get_channel(channel)

            if custom != None:
                emoji = f'[{payload.emoji.name}]({payload.emoji.url})'
            else:
                emoji = payload.emoji

            print(f'{payload.member} (<@{payload.user_id}>) reacted to https://discord.com/channels/{payload.guild_id}/{channel}/{payload.message_id} with {payload.emoji.name} ({emoji})')
            await dest.send(f'{payload.member} (<@{payload.user_id}>) reacted to https://discord.com/channels/{payload.guild_id}/{channel}/{payload.message_id} with {payload.emoji.name} ({emoji})')

    async def on_raw_reaction_remove(self, payload: nextcord.RawReactionActionEvent):
        if payload.guild_id == None or payload.guild_id == 1331932295506034711:
            return
        else:
            guild = self.get_guild(payload.guild_id)
            channel = payload.channel_id
            messageid = payload.message_id
            user = payload.user_id
            username = await guild.fetch_member(user)
            custom = payload.emoji.id
            dest = await self.fetch_channel(channel)

            if custom != None:
                emoji = f'[{payload.emoji.name}]({payload.emoji.url})'
            else:
                emoji = payload.emoji

            print(f'{username} (<@{user}>) removed the {payload.emoji.name} ({emoji}) reaction from https://discord.com/channels/{payload.guild_id}/{channel}/{messageid}')
            await dest.send(f'{username} (<@{user}>) removed the {payload.emoji.name} ({emoji}) reaction from https://discord.com/channels/{payload.guild_id}/{channel}/{messageid}')
    


intents = nextcord.Intents.all()


client = Client(intents=intents)
client.run(BOT_TOKEN)

#i feel so sigma! (i have not used python since i was 16.... its been 3 years.. save me from this self-imposed nightmare)