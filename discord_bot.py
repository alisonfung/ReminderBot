import discord
import responses
import settings


async def send_message(message, user_message, is_private):
    # message: the message that the bot will send
    # user_message: the message that the user sent
    # is_private: True if the user sent a DM
    try:
        # get bot response depending on user message
        response = responses.get_response(user_message)
        # if user sent a DM, reply in DM
        if is_private:
            await message.author.send(response)
        # otherwise, reply in the channel
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():

    # give discord bot permission to read messages 
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # on start, print in the console that the bot is running
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # if a message is sent and the author is the bot(client.user), ignore it
        if message.author == client.user:
            return
        
        # get details about the message that was sent
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # print message details
        print(f'{username} said: "{user_message}" ({channel})')


        # if the first character of the user's message was a ?
        if user_message[0] == '?':
            # get the user message without the ?
            user_message = user_message[1:]
            # send a message privately
            await send_message(message, user_message, is_private = True)
        else:
            # otherwise, if user message did not start with ?, send a message to the channel
            await send_message(message, user_message, is_private = False)

     
    client.run(settings.DISCORD_API_SECRET)



