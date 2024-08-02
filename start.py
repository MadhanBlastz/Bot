import os
import string
import random
import re
from pyrogram import Client, filters
from pytube import Youtube
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Get sensitive information from environment variables
api_id = os.environ.get('API_ID','21661450')
api_hash = os.environ.get('API_HASH','79612bc71908f95372808520a7eeee74')
bot_token = os.environ.get('BOT_TOKEN','7463606692:AAFKceJNgKeY2x01NsgRTFok0ifynPkpGXQ')


REGEX_CB = re.compile(r'(\w+)-(\w+)')

# Store youtube links
links = {}


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

# Generate random string
def generate_random_string(length):
    # Define the characters from which to generate the random string
    characters = string.ascii_letters + string.digits

    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string

# Define a function to send or update a message
async def send_or_update_message(chat_id, message_text, keyboard=None):
    if chat_id in message_ids:
        await app.edit_message_text(chat_id, message_ids[chat_id], message_text, reply_markup=keyboard)
    else:
        message = await app.send_message(chat_id, message_text, reply_markup=keyboard)
        message_ids[chat_id] = message.id

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

# Define a function to handle messages containing a YouTube link
@app.on_message(filters.text & filters.regex(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/\S+'))
async def handle_youtube_link(client, message):
    # Reply with the message about actions to take with the YouTube link
    reply_text = (
        "🎵 YouTube Music : For Downloading Songs in High/Low Quality from YouTube\n\n"
        "🔗 Make Download/Stream Link : Generated link will Play/Download in Browser\n\n"
        "Please select your preferred action below 👇"
    )

    random_id = generate_random_string(10)
    links[random_id] = message.text
    
    # Define inline keyboard markup for the buttons
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Thumbnail Downloader 🖼️", callback_data=f"thumbnail-{random_id}"),
            InlineKeyboardButton("YouTube Video Trimmer ✂️", callback_data=f"trimmer-{random_id}")
        ],
        [
            InlineKeyboardButton("Fast Downloader ⏩", callback_data=f"fast_downloader-{random_id}"),
            InlineKeyboardButton("YouTube Music 🎶", callback_data=f"youtube_music-{random_id}")
        ],
        [
            InlineKeyboardButton("YouTube Video 🎥", callback_data=f"youtube_video-{random_id}")
        ],
        [
            InlineKeyboardButton("Cancel ❌", callback_data="cancel")
        ]
    ])
    
    # Send the reply with inline keyboard
    await message.reply_text(reply_text, reply_markup=keyboard)

# Define a function to handle callback queries for buttons
@app.on_callback_query()
async def callback_query(client, callback_query):
    # Get the data from the callback
    action = callback_query.data

    option = REGEX_CB.search(action)
    
    if option:
        action = option.group(1)
        random_id = option.group(2)
        youtube_url = links.get(random_id)
    
    # Perform different actions based on the callback data
    if action == "thumbnail":
        await callback_query.answer("Processing... 🔄")
        # Add your code to handle Thumbnail Downloader action
        
    elif action == "trimmer":
        await callback_query.answer("Processing... 🔄")
        # Add your code to handle YouTube Video Trimmer action
        
    elif action == "fast_downloader":
        await callback_query.answer("Processing... 🔄")
        # Add your code to handle Fast Downloader action
        
    elif action == "youtube_music":
        await callback_query.answer("Processing... 🔄")
        # Add your code to handle YouTube Music action
        
    elif action == "youtube_video":
        # Prompt the user to select their preferred resolution
        reply_text = "Please select your preferred resolution:"
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("240p", callback_data="resolution_240p"),
                InlineKeyboardButton("360p", callback_data="resolution_360p"),
                InlineKeyboardButton("480p", callback_data="resolution_480p"),
                InlineKeyboardButton("720p", callback_data="resolution_720p"),
                InlineKeyboardButton("1080p", callback_data="resolution_1080p"),
            ],
            [
                InlineKeyboardButton("2k", callback_data="resolution_2k"),
                InlineKeyboardButton("4k", callback_data="resolution_4k")
            ],
            [
                InlineKeyboardButton("Cancel ❌", callback_data="cancel")
            ]
        ])
        await callback_query.edit_message_text(reply_text, reply_markup=keyboard)
        
    elif action.startswith("resolution_"):
        resolution = action.replace("resolution_", "")
        await callback_query.answer(f"You selected {resolution} resolution! 📹")

    elif action == "cancel":
        await callback_query.answer("Action canceled! ❌")

# Run the bot
app.run()

