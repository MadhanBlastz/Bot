import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Get sensitive information from environment variables
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')

# Check if all required environment variables are set
if not (api_id and api_hash and bot_token):
    raise ValueError("API credentials or bot token are not set as environment variables.")

# Create a Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Store the message IDs for each state
message_ids = {}

# Define inline keyboard markup for the starting message
starting_keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("My Bots", callback_data="my_bots"),
        InlineKeyboardButton("Functions", callback_data="functions")
    ],
    [
        InlineKeyboardButton("Commands", callback_data="commands"),
        InlineKeyboardButton("Disclaimer", callback_data="disclaimer")
    ],
    [
        InlineKeyboardButton("Close", callback_data="close")
    ]
])

# Define a function to send or update a message
async def send_or_update_message(chat_id, message_text, keyboard=None):
    if chat_id in message_ids:
        await app.edit_message_text(chat_id, message_ids[chat_id], message_text, reply_markup=keyboard)
    else:
        message = await app.send_message(chat_id, message_text, reply_markup=keyboard)
        message_ids[chat_id] = message.message_id

# Define a function to handle /start command
@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    user_name = message.from_user.first_name
    start_message = (
        f"Hello {user_name}!\n\n"
        "I am YouTube Playlist Downloader.\n\n"
        "Many Useful functions are available with Max Option.\n\n"
        "More than 2GB file will Split in parts.\n\n"
        "If any issues arise, report them at 👉 @mygroup"
    )
    await send_or_update_message(message.chat.id, start_message, starting_keyboard)

# Define a function to handle callback queries for "Close"
@app.on_callback_query(filters.regex("^close$"))
async def callback_query_close(client, callback_query):
    await callback_query.edit_message_text("Closed ✅")

# Define a function to handle callback queries for "My Bots"
@app.on_callback_query(filters.regex("^my_bots$"))
async def callback_query_my_bots(client, callback_query):
    # Define the list of bots
    bots_list = [
        "@mybot1",
        "@mybot2",
        "@mybot3",
        "@mybot4",
        "@mybot5",
        "@mybot6"
    ]

    # Construct the message content with the list of bots
    new_message = "Here is the list of bots:\n\n" + "\n".join(bots_list)

    # Update the message content with the list of bots
    await callback_query.edit_message_text(new_message, reply_markup=starting_keyboard)

# Define a function to handle callback queries for "Functions"
@app.on_callback_query(filters.regex("^functions$"))
async def callback_query_functions(client, callback_query):
    # Define the list of functions
    functions_list = [
        "(1). Pytube Downloader (In Desired video & audio format)",
        "(2). 🖼️ Thumbnail Downloader",
        "(3). If your 🔗 url will be a direct link Then you can use Audio & Video related functions.",
        "(4). YouTube Subtitles Downloader",
        "(5). Fast Download: It Uploads YouTube video Without Downloading (Quality HD)",
        "(6). YouTube Video Trimmer ✂️, It Trims YouTube video (Quality HD)",
        "(7). YouTube Music & Video, You can download High Quality Music with YouTube Music link.",
        "(8). YouTube Playlist Downloader, with 3 options (Default, Specific Range, Custom Specific Range)."
    ]

    # Construct the message content with the corrected numbering
    new_message = "\n\n".join(functions_list)

    # Update the message content with the list of functions
    await callback_query.edit_message_text(new_message, reply_markup=starting_keyboard)

# Define a function to handle callback queries for "Commands"
@app.on_callback_query(filters.regex("^commands$"))
async def callback_query_commands(client, callback_query):
    # Define the list of commands
    commands_list = [
        "/example1",
        "/example2",
        "/example3",
        "/example4",
        "/example5",
        "/example6",
        "/example7",
        "/example8",
        "/example9",
        "/example10",
        "/example11"
    ]

    # Construct the message content with the list of commands
    new_message = "These are some Basic commands:\n\n" + "\n".join(commands_list)

    # Update the message content with the list of commands
    await callback_query.edit_message_text(new_message, reply_markup=starting_keyboard)

# Define a function to handle callback queries for "Disclaimer"
@app.on_callback_query(filters.regex("^disclaimer$"))
async def callback_query_disclaimer(client, callback_query):
    # Define the legal disclaimer text
    disclaimer_text = (
        "Legal Disclaimer\n\n"
        "This legal disclaimer ('Disclaimer') applies to the use of our Bot, its services, and interactions with the bot. "
        "By using Bot, you agree to the terms and conditions outlined in this Disclaimer.\n\n"
        "1. Purpose of Bot:\n"
        "    This Telegram bot is designed to facilitate the download of publicly available files from the internet, "
        "Some video and Audio related tools. We do not host or store any files, nor do we endorse or support any illegal activities.\n\n"
        "2. User Responsibilities:\n"
        "    You, the user, are solely responsible for ensuring the legality of the files you request and download through Bot. "
        "It is your responsibility to comply with all applicable laws and regulations.\n\n"
        "3. No Data Collection:\n"
        "    Bot does not collect, store, or have access to any incoming or outgoing user data. Your privacy is important to us, and we respect it.\n\n"
        "4. Prohibited Activities:\n"
        "    Bot strictly prohibits the use of the bot for illegal activities, including but not limited to downloading, distributing, "
        "or sharing illegal materials, copyrighted content without proper authorization, or any other activities that violate the law.\n\n"
        "5. Security and Disclaimer of Liability:\n"
        "    While we take reasonable steps to ensure the safety and functionality of Bot, we do not guarantee the security or safety of downloaded files. "
        "You use the bot at your own risk.\n\n"
        "    Bot and its developers are not liable for any damages or legal consequences resulting from your use of the bot.\n\n"
        "6. Changes to Disclaimer:\n"
        "    This Disclaimer may be updated or modified at any time without prior notice. It is your responsibility to review this Disclaimer regularly for any changes.\n\n"
        "7. Contact Information:\n"
        "    If you have any questions or concerns about Bot or this Disclaimer, please contact us at @myid"
    )

    # Update the message content with the legal disclaimer text
    await callback_query.edit_message_text(disclaimer_text, reply_markup=starting_keyboard)

# Run the bot
app.run()
