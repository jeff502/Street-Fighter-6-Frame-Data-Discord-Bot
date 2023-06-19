import os
import discord
from dotenv import load_dotenv

from handle_user_inputs import character_aliases, rearrange_input, replace_input
from character_data import get_move_data


load_dotenv()
CLIENT_KEY: str = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message: discord.message.Message):
    print(type(message))
    """
    Listens for user message. If a message contains "!fd", send that message to get_data()
    Post to discord if the requirements are met. ("!fd character_name motion input")
    :param message:
    :return:
    """
    username: str = str(message.author).split("#")[0]  # Username without the #nums on the end.
    user_message: str = str(message.content).lower()
    channel: str = str(message.channel.id)

    print(message)
    print(f"{username}: {user_message} | {channel}")
    if message.author == client.user or message.author.bot is True:
        return
    if message.content.startswith("!fdhelp"):
        await message.channel.send(
            f"{username} Use the format: `!fd character motion/move` E.G.: `!fd Ken DPLP`.\n"
            f"For moves with follow ups, use a `~` delimiter between the move inputs. E.G.: !fd Ken MP~HP \n"
            f"For moves with levels, add the appropriate number to the end of the input.\n"
        )
        return

    if message.content.startswith("!fd"):
        user_msg: list = user_message.split()

        user_character: str = user_msg[1].title()
        character: str = character_aliases(user_character)

        user_character_input: str = user_msg[2].upper()
        replace_user_input: str = replace_input(user_character_input)
        rearranged_user_input: str = rearrange_input(replace_user_input)

        bot_msg: str  = get_move_data(character, rearranged_user_input)

        # Split this into two different error msgs. One for move and one for character. Possibly 3 for input
        if bot_msg is False:
            await message.channel.send("Not a valid input notation or character name. Please use the format "
                                       "`!fd Character move notation`. E.G. `!fd Ken 2lp ")
            return
        await message.channel.send(f"@{username} {bot_msg}")
        # If "@" messages are desired, enable them in the bot creation. Otherwise, delete the "@" from the send message.
        return


def main():
    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == '__main__':
    main()
