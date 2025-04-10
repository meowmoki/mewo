import nextcord
from nextcord.ext import commands
from info import *

class Client(nextcord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'it\'s never lupus, {message.author}')
   
    async def on_raw_reaction_add(self, payload: nextcord.RawReactionActionEvent):
        if payload.guild_id == None:
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
        if payload.guild_id == None:
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


intents = nextcord.Intents.default()
intents.message_content = True
intents.reactions = True


client = Client(intents=intents)
client.run(BOT_TOKEN)

#i feel so sigma! (i have not used python since i was 16.... its been 3 years.. save me from this self-imposed nightmare)