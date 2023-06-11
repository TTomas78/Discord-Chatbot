import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from services.MessageDeliverService import MessageDeliverService
from services.AssistantService import AssistantService
from services.PineconeService import PineconeService
from services.LoggerService import LoggerService

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENV = os.getenv('PINECONE_ENV')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ALLOWED_USERS = os.getenv('ALLOWED_USERS').split(',')
TARGET_USER = os.getenv('TARGET_USER')
LOG_FOLDER = os.getenv('LOG_FOLDER')
LOG_FILE = os.getenv('LOG_FILE')
TIME_TO_ANSWER = int(os.getenv('TIME_TO_ANSWER'))

intents = discord.Intents.default()


client = commands.Bot(command_prefix='!',intents=intents)

pinecone_service = PineconeService(PINECONE_API_KEY, PINECONE_ENV)
pinecone_service.set_database()
assistant = AssistantService(pinecone_service)
logger_service = LoggerService(LOG_FOLDER, LOG_FILE)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        if (message.author == client.user):
            #To avoid aswering to itself
            return None        
        if str(message.author.id) in ALLOWED_USERS:
            # The message was sent through a direct conversation
            print(f'Message received from {message.author.id}: {message.content}')
            message_deliver.add_message(message.content)

        else:
            await message.author.send('You are not autorized to use this bot')
        await client.process_commands(message)

message_deliver = MessageDeliverService(TIME_TO_ANSWER, assistant, TARGET_USER, client, logger_service)

client.run(TOKEN)

