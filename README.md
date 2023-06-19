# Street-Fighter-6-Frame-Data-Discord-Bot
Discord bot that post requested SF6 frame data.


This README provides an overview of your Discord bot project created in Python. The bot listens for user messages and responds to commands in the format !fd CHARACTER_NAME MOVE_AND_MOTION. The main functionality of the bot is to retrieve move data based on user inputs and post it to the Discord channel.
Prerequisites

To run this Discord bot project, you need to have the following:

    Python (version 3.6 or higher) installed on your machine.
    discord.py library installed. You can install it using pip install discord.py.
    dotenv library installed. You can install it using pip install python-dotenv.
    Discord API token. You can obtain the token by creating a bot application on the Discord Developer Portal.

Project Structure

The project consists of the following files:

    main.py: Contains the main code for the Discord bot.
    handle_user_inputs.py: Contains functions related to handling user inputs and data manipulation.
    character_data.py: Contains functions for retrieving move data based on user inputs.
    .env (not included): Contains the Discord API token. You should create this file in the project directory and add your token.

Getting Started

    Clone the repository to your local machine or download the source code files.

    Install the required dependencies by running the following command:

`pip install -r requirements.txt`

Create a .env file in the project directory and add the following line, replacing <DISCORD_TOKEN> with your Discord API token:

`DISCORD_TOKEN=<DISCORD_TOKEN>`

Run the bot by executing the following command:


    `python main.py`

      The bot should now be active and ready to respond to commands in your Discord server.

Bot Commands

The bot recognizes the following commands:

    `!fdhelp`: Displays information on how to use the bot. It provides the format for the command and examples.

    `!fd CHARACTER_NAME MOVE_AND_MOTION`: Retrieves move data for the specified character and motion/move. The character name should be provided in the command, followed by the motion or move notation. For moves with follow-ups, use a ~ delimiter between the move inputs. All data will be provided for moves with multiple differences. E.G. wind stock, held versions, FSE, etc.

    Some examples: `!fd ken lpdp`, `!fd dj Jroudhouse' `!fd zangief 720p`, `!fd dj 236236k`, `!fd jamie 2HK~HK~P`.

    Capitalization isn't required. 
    '5' is not required for neutral inputs.
    for jumping attacks add `j` to to move input. 
    for supers and ex moves use the appropriate button command (`p`, `k`, `pp`, `kk`).
    Commonly used aliases for moves and characters are supported. (roundhouse, gief, sim, lp, jab, etc)
    
Contributing

If you would like to contribute to this project, feel free to fork the repository and submit pull requests with your changes. Make sure to follow the existing code style and provide a clear description of your modifications.
License

This project is licensed under the MIT License.
Acknowledgments

    discord.py - The library used to create the Discord bot.
    dotenv - The library used for loading environment variables from the .env file.
    wiki.supercombo.gg - The source of frame data used in this bot.

Contact

If you have any questions or suggestions regarding this project, please feel free to contact me.
